from flask import Flask

app = Flask(__name__)

from api import routes

if __name__ == '__main__':
  app.run(port=5000, debug=True)


