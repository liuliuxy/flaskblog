from flask_assets import Bundle, Environment
from FlaskBlog import blog_bp

home_js = Bundle(
    'js/jquery-3.4.1.js',
    'js/bootstrap.js',
    'js/bootstrap.bundle.js',
    'js/popper.min.js',
    'js/base.js',
    filters='jsmin',
    output='public/js/common.js'
)

home_css = Bundle(
    'css/bootstrap.css',
    'css/bootstrap-grid.css',
    'css/bootstrap-reboot.css',
    'css/base.css',
    filters='cssmin',
    output='public/css/common.css'
)

assets = Environment()
assets.register('home_css', home_css)
assets.register('home_js', home_js)
