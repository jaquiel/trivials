from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/about')
def about():
    return 'The about page'

if app == "__main__":
    app.run()