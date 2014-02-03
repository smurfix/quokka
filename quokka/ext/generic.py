# coding: utf-8

#from flaskext.markdown import Markdown
from flask.ext.misaka import Misaka
from flask_wtf.csrf import CsrfProtect


def configure(app):
    # Markdown(app)
    Misaka(app,
           fenced_code=True,
           autolink=True,
           no_intra_emphasis=True,
           strikethrough=True,
           superscript=True,
           tables=True,
           hard_wrap=True,
           safelink=True)
    CsrfProtect(app)
    if app.config.get('GRAVATAR'):
        from flask.ext.gravatar import Gravatar
        Gravatar(app, **app.config.get('GRAVATAR'))
