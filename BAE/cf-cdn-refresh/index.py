from bottle import Bottle, run

import qiniu_operation

app = Bottle()
 
@app.route('/')
def index():
    return "It works!"
    
@app.route('/force_refresh')
def force_refresh():
    cnt = qiniu_operation.clear_all("codeforce-cdn")
    return "Deleted %d static file(s)" % cnt
 
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

#run(app, host='localhost', port=8080)
