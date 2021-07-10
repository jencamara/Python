from flask import Flask
app = Flask(__name__)    

    
@app.route('/')                           
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    print(name)
    return "Hi " + name 

@app.route('/repeat/<int:xx>/<word>')
def repeat(xx, word):
    return xx * word 

if __name__=="__main__":   


    app.run(debug=True)  
