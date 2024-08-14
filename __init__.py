from flask import Flask, render_template
from Card import *

app = Flask(__name__)


@app.route('/')
def home():
    # insert code here
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
