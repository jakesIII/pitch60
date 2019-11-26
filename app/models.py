from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id =db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255), unique = True, index = True)
    bio=db.Column(db.String(255))
    avatar=db.Column(db.String())
    # posts=db.Column(db.String())
    posts=db.relationship('Posts', backref='user', lazy="dynamic")
    password_hash=db.Column(db.String(255))



    @property
    def password(self):
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self, password):
        self.password_hash= generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'User {self.username}'

class Posts(db.Model):
    __tablename__='posts'

    id=db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String())
    description=db.Column(db.String())
    author=db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments=db.relationship('Comments', backref='post', lazy="dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts=Posts.query.all()
        return posts

    @classmethod
    def get_user_posts(cls, user_id):
        user_posts=Posts.query.filter_by(user_id=user_id).all
        return user_posts


    @classmethod
    def view_posts(cls, category):
        post_category=Posts.query.filter_by(category=category).all()

        return post_category


class Comments(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String)
    user = db.Column(db.String)
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments = Comments.query.filter_by(post_id).all()
        return comments
