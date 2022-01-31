from turtle import color
from flask import Flask, render_template 


app = Flask(__name__)


@app.route('/play')
def hello():
    return render_template('index.html', num=3, color='blue')


@app.route('/play/<int:num>')
def route_two(num):
    return render_template('index.html', num=num, color='blue')


@app.route('/play/<int:num>/<string:color>')
def route_three(num, color):
    return render_template('index.html', num=num, color=color)

@app.route('/ball')
def circle_route():
    return render_template('ball.html', num=3, color='blue')

@app.route('/ball/<int:num>/<string:color>')
def route_four(num,color):
    return render_template('ball.html', num=num, color=color)













if __name__=="__main__":
    app.run(debug=True)