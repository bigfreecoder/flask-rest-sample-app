'''
Created on Aug 12, 2016

@author: lic31
'''
import unittest

from hdfs.SeqFileUtil import SeqFileUtil


class SequnceFileTest(unittest.TestCase):


    def setUp(self):
        self.seqFileUtil=  SeqFileUtil()


    def tearDown(self):
        self.seqFileUtil=None


    def testCreateSequenceFile(self):
        seqFileLocation='test.seq'
        ingestedFile1='test.txt'
        ingestedFile2='why.txt'
        fileMetadata=dict()
        fileMetadata['hello']='world'
        fileMetadata['is']='not simple'
        fileMetadata2=dict()
        fileMetadata2['we']='world'
        fileMetadata2['are']='the'
        print str(fileMetadata)
        ingestedFiles=[ingestedFile1, ingestedFile2]
        fileMetadatas=[str(fileMetadata),str(fileMetadata2)]
        self.seqFileUtil.createSequenceFile(seqFileLocation, ingestedFiles, fileMetadatas)
    
    
    def testReadSequenceFile(self):
        #seqFileLocation='test.seq'
        seqFileLocation='/Users/lic31/xtremio-file/colocatedSequenceFile-r-00000'
        self.seqFileUtil.readSequenceFile(seqFileLocation)

if __name__ == "__main__":
    #import sys;
    #sys.argv = ['', 'Test.testName']
    unittest.main()