from app import db, app
from app.postgres import models as modles
from flask_restful import Api, Resource, url_for, marshal_with, fields

resource_fields = {
    'job_id': fields.String,
    'sn': fields.String,
    'job_status': fields.String,
    'sn': fields.String,
    'created_time': fields.DateTime(dt_format='rfc822'),
    'last_updated_time': fields.DateTime(dt_format='rfc822')
}
class UccJob(Resource):
    @marshal_with(resource_fields, envelope='job')
    def get(self, job_id):
	   job=modles.UccDataJob.query.filter_by(job_id=job_id).all()
	   print " joboo"+str(job)+"\n"
	   if job is None:
		  return {'error': 'not found'}, 404	
	   else:
		  return job

