import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.environ.get("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///event"

db = SQLAlchemy(app)


from myvenue import routes  # noqa
