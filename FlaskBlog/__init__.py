from flask import Flask, current_app, app, g
from FlaskBlog.bluepaints.blog import blog_bp
from FlaskBlog.bluepaints.user import user_bp
import os
from flask_bootstrap import Bootstrap
from FlaskBlog.setting import config
from FlaskBlog.until.assets import assets
from flask_debugtoolbar import DebugToolbarExtension
from FlaskBlog.extensions import db, login_manger
import click
from FlaskBlog.models import Admin, Post, Category, Comment, Link
from FlaskBlog.form import LoginForm

bootstrap = Bootstrap()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('FlaskBlog')
    app.config.from_object(config[config_name])
    db.init_app(app)
    login_manger.init_app(app)
    bootstrap.init_app(app)
    assets.init_app(app)
    register_loginForm(app)
    debugbar = DebugToolbarExtension(app)
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)
    register_commands(app)
    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='login name')
    @click.option('--password', prompt=True, help='password', confirmation_prompt=True, hide_input=True)
    def initadmin(username, password):
        click.echo('管理员账户生成中')
        admin = Admin.query.first()
        if admin:
            click.echo('已有账户更新管理员信息')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('账户生成中')
            admin = Admin(username)
            admin.set_password(password)
            db.session.add(admin)
        db.session.commit()
        click.echo('添加完成')


def register_loginForm(app):
    @app.before_request
    def addloginform():
        g.loginform = LoginForm()
