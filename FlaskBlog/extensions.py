from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manger = LoginManager()


@login_manger.user_loader
def load_user(user_id):
    from FlaskBlog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
