from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "名無し"
    return render_template('index.html', title='flask test', name=name)

@app.route('/<name>')
def good(name):
    return render_template('index.html', title='flask test', name=name)

if __name__ == "__main__":
    app.run(debug=True)