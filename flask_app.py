"""
Author: Onur Talu
"""

from flask import Flask, request
from flask import render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    # name = input("Your Name")
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # error = None
    print(request.method)
    if request.method == 'POST':
        inputfn = request.form['firstname']
        inputln = request.form['lastname']
        inputage = request.form['age']
        # render_template('error_page.html')
        if valid_login(inputfn, inputln, inputage):
            print('valid login')
            return redirect(url_for('profile'))
        else:
            print('invalid login')
            return redirect(url_for('error_page'))
    else:
        print('method is not post')
        return redirect(url_for('error_page'))
    # render_template('error_page.html')
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('profile.html', error=error)


@app.route('/error_page')
def error_page():
    return render_template('error_page.html')


def valid_login(inputfn, inputln, inputage):
    firstname = 'Inigo'
    lastname = 'Montoya'
    age = '10'
    # if firstname == inputfn and lastname == inputln and age == inputage:
    #     render_template('profile.html')
    # else:
    #     render_template('error_page.html')
    return firstname == inputfn and lastname == inputln and age == inputage


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
