from os import environ, path
from flask import current_app as app

class Config:
	# General Config
	FLASK_APP = environ.get("FLASK_APP")
	FLASK_ENV = environ.get("FLASK_ENV")
	PROPAGATE_EXCEPTIONS = True
	DEBUG = True
