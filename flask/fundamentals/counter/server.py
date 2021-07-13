from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret to keep it safe'    


@app.route('/')
def num_entry():
    print()
    if 'entry' in session:
        session['entry'] = session.get('entry') +1
    else:
        session['entry'] =1
    return render_template('index.html')

# @app.route('/users', methods=['POST'])
# def user():
#     print(request.form)
#     session['x'+1] = request.form['x'+1]
#     time = session['x'+1]
#     return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    session.pop("time")
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)