from flask import Flask, render_template
FlaskApp = Flask(__name__)

@FlaskApp.route('/')
def home():
    return render_template('home.html')

@FlaskApp.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    FlaskApp.run(debug=True)
