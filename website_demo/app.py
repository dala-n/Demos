# Import Flask framework
# Creating app
# Setting the route the "main directory"


from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    return render_template('index.html')

@app.route('/home')
def home():
        return 'Wow new page!'

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')