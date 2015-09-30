from flask import (Flask, g, url_for, redirect, flash, render_template)

from models import models
from forms import forms

app = Flask(__name__)
app.secret_key = 'secret'

# Configuration Settings
DEBUG = True
HOST = '0.0.0.0'
PORT = 8000


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    posts = models.Post.select()
    return render_template('blog.html', posts=posts)


@app.route('/new-post', methods=('GET', 'POST'))
def create_post():
    form = forms.PostForm()
    if not (form.validate_on_submit()):
        pass
        return redirect(url_for('.blog'))
    return render_template('create_post.html', form=form)


@app.route('/b/<post_name>')
def show_post(post_name):
    required_post = (models.Post.select()
                    .where(models.Post.post_name == post_name)
                    .get())
    return render_template('blog_page.html', post=required_post)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
