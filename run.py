from app import app
from app.models import User, Post
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
#app.run(debug = True)
if __name__== '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,  
        debug = True 
    )
