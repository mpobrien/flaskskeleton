from flask import Flask, session, g, render_template
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
app = Flask(__name__)
app.secret_key = '\xff\x19\xf4\xde\xc4T\n\x8a\xb7\x02h}\xadD\xe2\xa1\x86\x9b\xe3\xbf-\x95.\xa8'

app.config['MONGO_URL'] = 'mongodb://localhost:27017/'
app.config['CSS_FRAMEWORK'] = 'foundation'; # foundation
login_manager = LoginManager()

login_manager.anonymous_user = AnonymousUser
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

login_manager.setup_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from flaskskeleton.views import usermgmt
from flaskskeleton.views import general
app.register_blueprint(usermgmt.mod)
app.register_blueprint(general.mod)

from flaskskeleton.database import *

