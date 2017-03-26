from flask import render_template
from restapi import restapi

@restapi.route('/index')
def index():
    user = {'name' : 'Miguel'}
    return render_template('Index.html', title='Home',user=user)
