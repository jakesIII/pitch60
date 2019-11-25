from flask import render_template
from . import main

@main.app_errorhandler(404)
def error_handler(error):

    return render_template('fourhundo.html'), 404
