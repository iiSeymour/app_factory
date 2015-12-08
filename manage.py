from app import create_app
from flask.ext.script import Manager

manager = Manager(create_app)

manager.add_option('-c', '--config', dest='config', required=False)
manager.run()
