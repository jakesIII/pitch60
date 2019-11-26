from flask import render_template, request, redirect, url_for, abort
from ..models import User, Posts, Comments
from . import main
from .forms import UpdateProfile, PostForm, CommentForm
from flask_login import login_required
from .. import db, photos

@main.route('/', methods=['GET'])
def index():

    title = 'Home - minute/pitch'

    posts = Posts.get_posts()

    return render_template('index.html', title=title, posts=posts )

@main.route('/posts_comments', methods=['GET'])
def view_comment(post_id):

    comments=Comments.get_comments(post_id)

    return render_template('view_comment.html', comments = comments)





@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort (404)

    return render_template("profile/profile.html", user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar= path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/new_posts', methods = ['GET', 'POST'])
@login_required
def new_posts():

    form = PostForm()

    if form.validate_on_submit():
        new_post = Posts (category=form.category.data, description= form.description.data, author=form.author.data)

        new_post.save_post()

        return redirect(url_for('main.index'))

    return render_template('posteth.html', PostForm=form )

@main.route('/new_comment', methods=['GET', 'POST'])
@login_required
def new_comment():

    form = CommentForm()

    if  form.validate_on_submit():
        new_comment = Comments (comment = form.comment.data, user = form.user.data )

        new_comment.save_comment()

        return redirect (url_for('main.index'))

    return render_template('commenteth.html', CommentForm = form )
