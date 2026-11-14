"""Self-contained synthetic control for the cross-archive identity checker."""
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_cross_archive_identity import check


def zbytes(files):
    out = BytesIO()
    with ZipFile(out, 'w', ZIP_DEFLATED) as z:
        for name, data in files.items():
            z.writestr(name, data if isinstance(data, bytes) else json.dumps(data))
    return out.getvalue()


def build(mismatch=False):
    editions={}
    files={}
    for edition in ('PERSONAL','COMMERCIAL','ENTERPRISE'):
        name='PCP_1.0_'+edition.title()+'_Edition.zip'
        p='PCP_1.0_'+edition.title()+'_Edition/'
        b=21 if mismatch and edition=='ENTERPRISE' else 22
        version={"name":"pcp","version":"1.0.22"}
        versionos={"name":"pcp-os","version":"1.0.22"}
        fileset={p+'EDITION.json':{'build':b},p+'MANIFEST.json':{'build':b},p+'PCP_1.0_Plugins/plugins/pcp/.claude-plugin/plugin.json':version,p+'PCP_1.0_Plugins/plugins/pcp-os/.claude-plugin/plugin.json':versionos}
        raw=zbytes(fileset)
        pname='PCP_1.0_Plugins_'+edition.title()+'_Edition.zip'
        q='PCP_1.0_Plugins_'+edition.title()+'_Edition/'
        plugin=zbytes({q+'PLUGINS.json':{'build':22},q+'MANIFEST.json':{'build':22},q+'PCP_1.0_Plugins/plugins/pcp/.claude-plugin/plugin.json':version,q+'PCP_1.0_Plugins/plugins/pcp-os/.claude-plugin/plugin.json':versionos})
        files[name]=raw; files[pname]=plugin
        editions[edition]={'file':name,'sha256':sha256(raw).hexdigest(),'plugins_archive':{'file':pname,'sha256':sha256(plugin).hexdigest()}}
    files['PCP_1.0_Source.zip']=b'SYNTHETIC SOURCE'
    files['PCP_1.0_Release_Record.zip']=b'SYNTHETIC RECORD'
    idx={'build':22,'plugins':{'version':'1.0.22'},'source':{'file':'PCP_1.0_Source.zip','sha256':sha256(files['PCP_1.0_Source.zip']).hexdigest()},'record':{'file':'PCP_1.0_Release_Record.zip','sha256':sha256(files['PCP_1.0_Release_Record.zip']).hexdigest()},'editions':editions}
    files['RELEASE.json']=idx
    return zbytes({'PCP_1.0_Release/'+name: data for name,data in files.items()})

with TemporaryDirectory() as td:
    good=Path(td)/'good.zip';good.write_bytes(build(False))
    bad=Path(td)/'bad.zip';bad.write_bytes(build(True))
    assert check(good)['summary']=={'checked_archives':8,'hashes_passed':8,'build_labels_checked':24,'build_labels_matched':24,'problems':0},check(good)['summary']
    assert check(bad)['summary']=={'checked_archives':8,'hashes_passed':8,'build_labels_checked':24,'build_labels_matched':22,'problems':2},check(bad)['summary']
    print('POSITIVE: 8/8 archive hashes and 24/24 labels, 0 problems')
    print('NEGATIVE: 8/8 archive hashes but 2/24 labels mismatch, 2 problems')
