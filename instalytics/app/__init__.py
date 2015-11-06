from flask import Flask
from instalytics.app.instagram_routes import instagram_blueprint

app = Flask(__name__)
app.register_blueprint(instagram_blueprint)