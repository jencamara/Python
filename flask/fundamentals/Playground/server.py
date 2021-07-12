from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/play')
def play():
    return render_template('index.html')


@app.route('/play/<int:xx>')
def play_multiply(xx):
    return render_template('lvltwo.html', xx=xx)

if __name__=="__main__":
    app.run(debug=True)