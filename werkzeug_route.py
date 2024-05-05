from flask import Flask
from werkzeug.routing import Map, Rule

app = Flask(__name__)

url_map = Map([
  Rule('/user/<username>', endpoint='show_profile')
])

@app.endpoint('show_profile')
def show_profile(username):
  return f'{username}'

if __name__ == '__main__':
  app.run(debug=True)