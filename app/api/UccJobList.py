from app import db
from app.postgres  import models
import uuid
from flask_restful import Resource
from flask import request, jsonify
from datetime import datetime, date
from app.postgres.models import UccDataJob
class UccJobList(Resource):
    def post(self):
        sn_arr=request.json.get('sn')
        request_id=str(uuid.uuid4())
        data_request=UccDataJob(request_id, sn_arr, 'INITIAL', datetime.utcnow(), datetime.utcnow())
        db.session.add(data_request)
        db.session.commit() 
        return jsonify( { 'job_id': request_id } )
