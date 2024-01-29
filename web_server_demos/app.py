# Import Flask framework
# Creating app
# Setting the route the "main directory"


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/home')
def home():
    return 'Wow new page!'

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')