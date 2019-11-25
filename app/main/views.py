from flask import render_template
# , request, redirect, url_for
from . import main
# from ..models import Review, User
from flask_login import login_required

@main.route('/')
def index():

    title = 'Home - 60 mins pitch'

    return render_template('index.html')

@main.route('/post/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    pass
