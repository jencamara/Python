from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/')
def checkerboard():
    return render_template('index.html')

@app.route('/<int:num>')
def checkerboard2(num):
    return render_template('second.html', num="4")

@app.route('/<int:x>/<int:y>')
def checkerboard3(x,y):
    return render_template('third.html', x=x,y=y)


if __name__=="__main__":
    app.run(debug=True)