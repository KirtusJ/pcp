/* OVMF diagnostic. The host supplies only the ELF's page-aligned physical footprint. */
#include <efi.h>
#include <efilib.h>
#include "footprint.h"

/* QEMU's debug console captures bytes without calling firmware or changing the memory map. */
static void emit(char c) {
    __asm__ volatile("outb %0, %1" : : "a"((unsigned char)c), "Nd"(0xe9));
}

static void record(const char *name, UINT64 value) {
    static const char hex[] = "0123456789abcdef";
    while (*name) emit(*name++);
    emit('=');
    for (int shift = 60; shift >= 0; shift -= 4) emit(hex[(value >> shift) & 15]);
    emit('\n');
}

EFI_STATUS efi_main(EFI_HANDLE image, EFI_SYSTEM_TABLE *system) {
    InitializeLib(image, system);
    EFI_BOOT_SERVICES *bs = system->BootServices;
    EFI_PHYSICAL_ADDRESS fixed = KERNEL_BASE;
    EFI_PHYSICAL_ADDRESS chosen = 0x3fffffff; /* The kernel initially maps the first GiB. */
    EFI_STATUS status;

    record("fixed_base", fixed);
    record("pages", KERNEL_PAGES);
    status = uefi_call_wrapper(bs->AllocatePages, 4, AllocateAddress, EfiLoaderData, KERNEL_PAGES, &fixed);
    record("fixed_status", status);
    if (status == EFI_SUCCESS)
        record("fixed_free", uefi_call_wrapper(bs->FreePages, 2, fixed, KERNEL_PAGES));

    status = uefi_call_wrapper(bs->AllocatePages, 4, AllocateMaxAddress, EfiLoaderData, KERNEL_PAGES, &chosen);
    record("chosen_status", status);
    if (status == EFI_SUCCESS) {
        EFI_PHYSICAL_ADDRESS same = chosen;
        record("chosen_base", chosen);
        status = uefi_call_wrapper(bs->AllocatePages, 4, AllocateAddress, EfiLoaderData, KERNEL_PAGES, &same);
        record("occupied_status", status);
        record("chosen_free", uefi_call_wrapper(bs->FreePages, 2, chosen, KERNEL_PAGES));
        same = chosen;
        status = uefi_call_wrapper(bs->AllocatePages, 4, AllocateAddress, EfiLoaderData, KERNEL_PAGES, &same);
        record("reacquire_status", status);
        if (status == EFI_SUCCESS)
            record("reacquire_free", uefi_call_wrapper(bs->FreePages, 2, same, KERNEL_PAGES));
    }
    record("done", 1);
    uefi_call_wrapper(system->RuntimeServices->ResetSystem, 4, EfiResetShutdown, EFI_SUCCESS, 0, NULL);
    return EFI_DEVICE_ERROR;
}
