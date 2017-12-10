from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized and Spinnaker and testing'

@app.route('/test')
def test():
    return 'this is a new test route'

@app.route('/third/<name>')
def third(name):
    return "hello {{name}}. nice to meet you"
           
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
