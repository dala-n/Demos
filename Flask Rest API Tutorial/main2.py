from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app) # Wraps our app in an API, inistializes it as a REST API

class HelloWorld(Resource):                       ### Define class inherited from Resource, handles requests
	# def get(self):                                # Override the get() method
	# 	return {"data": "Hello World"}              # Infomation MUST be json SERIALIZABLE, hence we use a DICT
	
	def get(self, name, test):                      # Override the get() method, now with parameters
		return {"name": name, "test" : test}  
	
	def post(self):                                 # Override the post() method
		return {"data": "Posted"}


### ADDING RESOURCES TO API ###
### We can add resources to our api, accessible through /helloworld endpoint, root of the resource
	# param1: class HelloWorld -> Resource
	# param2: root, <parameters>

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")     # 2. string, int, boolean, etc

if __name__ == "__main__":                      # Starts our server, flask application
	app.run(debug=True)                         # allows us to see any logging information, development environment