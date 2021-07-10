from flask import Flask, render_template  
app = Flask(__name__)    


@app.route('/success')
def success():
    return "success"
    
@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<int>/<word>')
def repeat(int, word):
    print(int())
    print(word)
    return int("") * word


if __name__=="__main__":   


    app.run(debug=True)  

    
    


