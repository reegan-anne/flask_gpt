from flask import Flask, redirect, url_for
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello World'

###

# @app.route('/hello/<name>')
# def hello_name(name):
#     #Can be found at http://localhost:5000/hello/Developer
#    return 'Hello %s!' % name

###

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#     #Can be found at http://localhost:5000/blog/11
#    return 'Blog Number %d' % postID

###

# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#    #Can be found at http://localhost:5000/rev/1.1
#    return 'Revision Number %f' % revNo

###

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

# app.add_url_rule('/', 'hello', hello_name)

if __name__ == '__main__':
   app.run(debug=True)