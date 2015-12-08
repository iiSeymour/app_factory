from flask import Blueprint
core = Blueprint('core', __name__)
import routes
import filters
