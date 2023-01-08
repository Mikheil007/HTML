from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/kawasaki/')
def kawasaki():
    return render_template('kawasaki.html')
@app.route('/honda/')
def honda():
    return render_template('honda.html')
@app.route('/practice/')
def practice():
    return render_template('practice.html')
if __name__ == '__main__':
    app.run()
