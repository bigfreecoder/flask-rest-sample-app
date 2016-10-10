'''
Created on Aug 8, 2016

@author: lic31
'''
import json
import unittest
print(unittest.__file__)
from app import app
from app import mongo



class MongodbTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.ctx = self.app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        self.ctx.pop()
    
    def testFindMetadata(self):
        metadata = mongo.db.metadata.find_one_or_404({'_id' : 'vmax_000195700255_2016-06-01_18-15-24'})
        # print metadata
        print json.dumps(metadata, sort_keys=True,
                  indent=4, separators=(',', ': '))
    
    
    def testSaveMetadata(self):
        metadata = {
                    "_id": "vmax_000195700255_2016-06-01_18-55-27",
                    "location": "/shared/storage/ucc/testdir_fromucc",
                    "md5": "73e2cacccf3a5c499e1fd58dd845c414",
                    "name": "CUSTOMER_SYMMETRIX-VMAX_vmax-test_2016-06-01_18-55-27.zip",
                    "status": "NA"
                    }
        metadataId = mongo.db.metadata.insert_one(metadata).inserted_id
        print metadataId;
        
    def testUpdateFileStatus(self):
        result = mongo.db.metadata.update_one({"_id": "vmax_000195700255_2016-06-01_18-55-27"}, {'$set':{"status": "landed"}})
        print result.modified_count

if __name__ == "__main__":
    # import sys;
    # sys.argv = ['', 'Test.testName']
    unittest.main()
