'''
Created on Sep 22, 2016

@author: lic31
'''
from flask_restful import Resource
from app.logger import Logger
logger = Logger(__name__).log()

class HelloWorld(Resource):

    def get(self):
        logger.warning('get resource: %s', __name__)
        return {'hello': 'world'}


