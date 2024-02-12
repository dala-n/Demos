from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):               # Handle different inputs, doesnt exist
	if video_id not in videos:
		abort(404, message = "Could not find video...")
		
def abort_if_video_id_already_exists(video_id):               # Handle different inputs, duplicate
	if video_id in videos:
		abort(404, message = "Video already exists!")

class Video(Resource):
	def get(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		return videos[video_id]
	def put(self, video_id):
		args = video_put_args.parse_args()          # Ensure the video we want to add is a valid argument
		abort_if_video_id_already_exists(video_id)  # Abort if it already exists
		videos[video_id] = args                     # Add video in from put request
		return videos[video_id] , 201               # Pass status code through, 200 by default

api.add_resource(Video, "/video/<int:video_id>") # Video sent through put request, make video id

if __name__ == "__main__":
	app.run(debug=True)