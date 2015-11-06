from flask import Blueprint, redirect
from webargs.flaskparser import use_kwargs
from webargs import fields
from instagram.client import InstagramAPI

from instalytics import settings

INSTAGRAM_REDIRECT_PATH = '/redirect'
BLUEPRINT_NAME = 'instagram'

instagram_blueprint = Blueprint(BLUEPRINT_NAME, __name__)


@instagram_blueprint.route('/auth', methods=['GET'])
def instagram_auth():
    scope = ['basic', 'likes', 'comments', 'relationships']
    api = InstagramAPI(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=settings.HOST + '/' + BLUEPRINT_NAME + INSTAGRAM_REDIRECT_PATH
    )

    return redirect(api.get_authorize_login_url(scope=scope), code=302)


@instagram_blueprint.route(INSTAGRAM_REDIRECT_PATH, methods=['GET'])
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