from flask import Blueprint
from flask_restful import Api
from HelloWorld import HelloWorld
from UccJob import UccJob
from UccJobList import UccJobList
api_bp = Blueprint('api', __name__, url_prefix='')
api = Api(api_bp)
#api.add_resource(HelloWorld, '/api/hello')
api.add_resource(UccJob, '/api/jobs/<string:job_id>')
api.add_resource(UccJobList, '/api/jobs')
