import sys
import qiniu.rsf
import qiniu.conf
import qiniu.rs

qiniu.conf.ACCESS_KEY = 'ACCESS_KEY'
qiniu.conf.SECRET_KEY = 'SECRET_KEY'


def clear_all(bucket, rs=None, prefix=None, limit=None):
    if rs is None:
        rs = qiniu.rsf.Client()
    marker = None
    err = None
    files = []
    while err is None:
        ret, err = rs.list_prefix(bucket, prefix=prefix, limit=limit, marker=marker)
        marker = ret.get('marker', None)
        for item in ret['items']:
            files += ret['items']
    if err is not qiniu.rsf.EOF:
        sys.stderr.write('error: %s ' % err)
    else:
        keys = [qiniu.rs.EntryPath(bucket, x['key']) for x in files]
        rets, err = qiniu.rs.Client().batch_delete(keys)
    return len(files)
