'''
Created on Sep 23, 2016

@author: lic31
'''
from app import db
class UccDataJob(db.Model):	
    job_id = db.Column(db.String(60), primary_key = True, nullable=False)
    sn = db.Column(db.String(60), index = True, unique = True,nullable=False)
    job_status = db.Column(db.String(20), unique =False, nullable=True)
    created_time = db.Column(db.DateTime, unique =False, nullable=False)
    last_updated_time = db.Column(db.DateTime, unique =False, nullable=True)
    def __init__(self, job_id, sn, job_status, created_time, last_updated_time):
        self.job_id=job_id
        self.sn=sn
        self.job_status=job_status
        self.created_time=created_time
        self.last_updated_time=last_updated_time
    def __repr__(self):
        return '<job request %r>' % (self.job_id)