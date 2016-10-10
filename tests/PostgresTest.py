'''
Created on Aug 22, 2016

@author: lic31
'''
import unittest
from app import db
from app.unity.System import System

class PostgresTest(unittest.TestCase):


    def setUp(self):
        #self.app = app
        #self.ctx = self.app.app_context()
        #self.ctx.push()
        pass
       


    def tearDown(self):
        #self.ctx.pop()
        pass


    def testConnect(self):
        system_info=System('FNM00154600480', 'FNM00154600480', 'Oberon_DualSP');
        db.session().add(system_info)
        db.session.commit()
        


if __name__ == "__main__":
    unittest.main()