from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('home.html')

@app.route('/register')
def register():
    return ('register.html')

@app.route('/task')
def task():
    return ('createTask.html')


if __name__ == '__main__':
    app.run(debug=True)