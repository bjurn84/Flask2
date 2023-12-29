from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']
   
    resp = make_response(render_template('welcome.html', name=name))
    resp.set_cookie('user_data', f'name={name}&email={email}')
   
    return resp

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('user_data', expires=0)
   
    return resp

if __name__ == '__main__':
    app.run(debug=True)