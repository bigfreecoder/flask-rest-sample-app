# Import flask and template operators
from flask import Flask, render_template,request
from web.views import health_check as health_check
from web.views import zip_files as zip_files

from flask.ext.bootstrap import Bootstrap
from flask.ext.pymongo import PyMongo

import os
#Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__)

#flask restful services
from flask_restful import Resource, Api

rest = Api(app)


# Configurations
# when run in docker container, get system evvironment to load correct cofig
config_name=os.environ.get('flask_environ')
app.config.from_object(config_name)

# Define the database object which is imported
# by modules and controllers
from sqlalchemy import MetaData
meta = MetaData(schema="ucc")
db = SQLAlchemy(app, metadata=meta)

# create pymongo object
mongo = PyMongo(app, config_prefix='MONGO')

# import bootstrap
bootstrap = Bootstrap(app)
# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module
# Register blueprint(s)
app.register_blueprint(health_check)
#app.register_blueprint(zip_files)
# app.register_blueprint(xyz_module)
# ..

#register api blueprint
from api import api_bp
app.register_blueprint(api_bp)

# register restful resources'
#from api.HelloWorld import HelloWorld
#rest.add_resource(HelloWorld, '/resources/hello')
#from api.UccJobList import UccJobList
#rest.add_resource(UccJobList, '/ucc/jobs')
#from api.UccJob import UccJob
#rest.add_resource(UccJob, '/ucc/jobs/<job_id>')



# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()
