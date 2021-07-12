from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:x>')
def play(x):
    return render_template('lvl_2_index.html', box = x)

if __name__=="__main__":
    app.run(debug=True)