from flask import Flask

app = Flask(__name__)

@app.route('/Case1')
def softserve():
    return 'Welcome to Softserve'

@app.route('/Case2')
def devops():
    return 'Welcome to DevOps'

if __name__ == '__main__':
    app.run(debug=True)
