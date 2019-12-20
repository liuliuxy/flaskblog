from flask import Flask, render_template, blueprints, flash, redirect, url_for, Blueprint, request, g, abort
from FlaskBlog.form import PostForm, CategoryForm, LoginForm
from FlaskBlog.models import Post, Category, Admin
from FlaskBlog.extensions import db
from flask_login import login_user, current_user, logout_user
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from FlaskBlog.util import redirect_back

user_bp = Blueprint('user', __name__)


@user_bp.route('/manager')
def manager():
    flash('445', 'info')
    return render_template('manager.html')


@user_bp.route('/manager/addpost', methods=['GET', 'POST'])
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = Category.query.get(form.category.data)
        post = Post(title=title, body=body, category=category)
        db.session.add(post)
        db.session.commit()
        flash('文章添加中', 'info')
        return redirect(url_for('blog.show_post', post_id=post.id))
    return render_template('addpost.html', form=form)


@user_bp.route('/manager/addclass', methods=['GET', 'POST'])
def addclass():
    form = CategoryForm()
    if form.validate_on_submit():
        categoryname = form.name.data
        category = Category(name=categoryname)
        db.session.add(category)
        db.session.commit()
        flash('分类添加成功', 'info')
        return redirect(url_for('.manager'))
    return render_template('addclass.html', form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = g.loginform
    if form.validate_on_submit():
        user_name = form.username.data
        user_password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if user_name == admin.username and admin.validate_password(user_password):
                login_user(admin, remember)
                flash('登录成功', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('账号或密码错误', 'warning')
    flash(current_user.is_authenticated, 'info')
    return redirect_back()


@user_bp.route('/loginout')
def loginout():
    logout_user()
    flash('登出成功', 'info')
    return redirect(url_for('blog.index'))
