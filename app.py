from calc import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <a href="/calculator"> 계산기 </a>
    '''


@app.route('/calculator')
def calculator():
    return render_template('calc_web.html')

if __name__=="__main__":
    app.run(debug=True)