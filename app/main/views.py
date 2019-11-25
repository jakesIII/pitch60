from flask import render_template
# , request, redirect, url_for
from . import main
# from ..models import Review, User

@main.route('/')
def index():

    title = 'Home - 60 mins pitch'

    return render_template('index.html')
