from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
@app.route('/play/<int:times>/<string:color>')
def color_coded_boxs(times, color):
    # times = int(times)
    return render_template('index.html', times = times, color = color)
    # return 'hello' 
@app.route('/play')
def welcome():
    return render_template('index.html' , times = 3, color = "blue")
@app.route('/play/<int:times>')
def boxs(times):
    return render_template('index.html' , times = times, color = "blue")
if __name__=="__main__":   
    app.run(debug=True)   
