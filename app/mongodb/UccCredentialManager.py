'''
Created on Aug 8, 2016

@author: lic31
'''
from app import mongo


class CredentialManager(object):

    '''
    this class is responsible for persisting 
    credentials for Ucc application
    '''

    
    def __init__(self, params):

        '''
        Constructor
        '''

    def persistCredential(self, credential):

        mongo.db.zipfiles.create(credential)
    

    