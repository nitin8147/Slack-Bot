from flask import Flask
from flask_restful import Resource, Api
from SlackTestBot.resources.slash import HelloWorld
from SlackTestBot.operations.slack import SlackOperations
import os




app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
