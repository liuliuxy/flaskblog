from flask import Flask, render_template, Blueprint, flash
from FlaskBlog.models import Post
from flask import request, current_app
from FlaskBlog.form import LoginForm

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('index.html', pagination=pagination, posts=posts)


@blog_bp.route('/post/<int:post_id>/')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)
