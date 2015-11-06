from flask import Flask, redirect
from webargs.flaskparser import use_kwargs
from webargs import fields
from instagram.client import InstagramAPI

from instalytics import settings

app = Flask(__name__)

INSTAGRAM_REDIRECT_PATH = '/instagram/redirect'


@app.route('/instagram/auth', methods=['GET'])
def instagram_auth():
    scope = ['basic', 'likes', 'comments', 'relationships']
    api = InstagramAPI(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=settings.HOST + INSTAGRAM_REDIRECT_PATH
    )

    return redirect(api.get_authorize_login_url(scope=scope), code=302)


@app.route(INSTAGRAM_REDIRECT_PATH, methods=['GET'])
@use_kwargs({
    'code': fields.Str(required=True)
}, locations=('query',))
def instagram_redirect(code):
    api = InstagramAPI(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=settings.HOST + INSTAGRAM_REDIRECT_PATH
    )
    access_token = api.exchange_code_for_access_token(code)
    # TODO - save access token on user model

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)