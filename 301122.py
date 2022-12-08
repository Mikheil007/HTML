from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/teo/')
def teo():
    return render_template('teo.html')
@app.route('/honda/')
def honda():
    return render_template('honda.html')
if __name__ == '__main__':
    app.run()