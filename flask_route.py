from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/about')
def about():
  return 'This is the about page'

@app.route('/hello/<name>')
def hello_name(name):
  return f'Hello {name}'

@app.route('/rev/<int:postID>')
def show_blog(postID):
  return f'Blog Number {postID}'

@app.route('/rev/<float:revNo>')
def revision(revNo):
  return f'Revision Number {revNo}'

if __name__ == '__main__':
  app.run(debug=True)