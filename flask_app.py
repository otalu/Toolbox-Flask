"""
Produces a website that has an index page, and profiles for three users,
as well as a "hello" page. The profiles can only be reached if the user
inputs correct information about themselves in the index page.

After running in the terminal, go to 127.0.0.1:5000 to access the index page,
and ~/hello/<your_name> to reach the "hello" page.

Author: Onur Talu
"""

import os.environ
from flask import Flask, request
from flask import render_template, redirect, url_for
import database
app = Flask(__name__)

user_db = database.user_db


@app.route('/')
def index():
    """
    Renders the template index.html, which directs the user to a page with a
    form that redirects the user to a profile or error page, dpeending on the
    input.
    """
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """
    The "hello" page. Can be accessed through the URL.
    """
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Requests the information provided by the user and compares it to the
    database, redirects the user to a profile page or an error page,
    depending on the input.
    """
    if request.method == 'POST':
        inputfn = request.form['firstname']
        inputln = request.form['lastname']
        inputage = request.form['age']
        for i in range(len(user_db)):  # checks if the credentials check out
            if user_db[i] == [inputfn, inputln, inputage]:
                print('Valid Login')
                return redirect(url_for('profile', user_no=str(i+1)))
        print('Invalid Login')
        return redirect(url_for('error_page'))
    else:
        print('Method is not Post')  # Useful to keep when debugging
        return redirect(url_for('we_messed_up'))


@app.route('/sorry')
def sorry():
    """
    Returns an error page that notes that the problem is not in the input of
    the user, but in the code and apologizes.
    """
    return render_template('we_messed_up.html')


@app.route('/error_page')
def error_page():
    """
    Error page for when the input from the user does not match the database.
    """
    return render_template('error_page.html')


@app.route('/profile')
@app.route('/profile/<user_no>')
def profile(user_no=None):
    """
    Returns the profile page for the user.
    """
    user_info = user_db[int(user_no)-1]
    info_dict = {'firstname': user_info[0],
                 'surname': user_info[1],
                 'age': user_info[2]}
    return render_template('profile.html', **info_dict)


if __name__ == '__main__':
    app.debug = True  # updates the page as the code is saved
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000)))
    app.run(host=HOST, port=PORT)
