'''
Created on Aug 18, 2016

@author: lic31
'''
import unittest

from hdfs.AvroUtil import AvroUtil


class AvroUtilTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMakeObject(self):
        avroUtil=AvroUtil()
        avroObject=avroUtil.makeObject('sn', 'NA', 'NA', 'NA', 'helloworlld.txt', 'helloworld.txt', '../..helloworld.txt', 100, 'dfdfdfd', 'hello.zip', 'hello.zip', 1000, 'hhlerd', 4, 'ucc_vmx_r_00001.seq')
        print avroObject
     
    def testBuildAvroObject(self):
        avroUtil=AvroUtil()
        avroSchema=avroUtil.makeSchema("../app/hdfs/Metadata.avsc")
        fileMetadata={
                       "sn": "12234sde",
                       "dataType": "vmx", 
                       "division":"ucc", 
                       "ingestionLocation":"hello.zip", 
                       "fileName":"systpool.xml", 
                       "filePath":"hello.zip/systpool.xml", 
                       "extractedFilePath":"hello/systpool.xml", 
                       "fileSize":1234, 
                       "fileCheckSum":"DDFDKEQQ1234", 
                       "archiveFileName":"hello.zip",
                       "archiveFilePath":"hello.zip",
                       "archiveFileSize":12345, 
                       "archiveFileChechSum":"wewSDSDFwew123", 
                       "totalExtractedFileCount":5, 
                       "sequenceFileName":"ucc_vmx_r_00001.seq"
                       }
        avroObject=avroUtil.buildAvroObject(fileMetadata, avroSchema)
        print avroObject
        avroUtil.readAvroObject(avroObject)
      
    def testavro2Json(self):
        avroUtil=AvroUtil()
        avroUtil.avro2Json()
        
    def testBuildAvroObjectFromExistingData(self):
        data='''{  
         business_metadata:{   
            "party_id":null,  
            "serial_number":null,  
            "user_defined_values":null  
         }, 
         operational_metadata:{  
            "is_chunked":null,                        
                                                             
            "data_type":"symmetrix-rma",                 
            "division":"MFG",                           
            "entity":null,                       
            "ingestion_metadata":{  
               "ingestion_type":"continuous",    
               "extracted_timestamp":1453998971,
               "version":"TEST_MAVEN_VERSION",   
               "end_timestamp":1454005608382,  
               "start_timestamp":1454005608382, 
               "ingestion_location":{  
                  "path":"\/ingest\/continuous\/10.253.136.172-2708\/PROD.#1454003329286",  
                  "offset":42415231,  
                  "key":null  
               },  
               "ingestion_process":[
                  {  
                     "os":"Linux",  
                     "jvm":"1.7.0_65",  
                     "pid":"2708",  
                     "host":"bdlsxdprd02.isus.emc.com",  
                     "ip":"10.253.136.172",  
                     "log_path":null  
                  }  
               ],  
               "started_by":null  
            },  
            "file_metadata":{  
               "timestamp":1453998928000,  
               "name":"legacy_logall_date160125_time110534.log",
               "path":"RmaData_disk_JZX0UYNJ_zip\/legacy_logall_date160125_time110534.log",  
                                                                           
               "extracted_path":"\/landingzone\/archiveExpansionZone\/1453998962777-384-2678-10.253.72.65\/FEPAPPDRMPRD02_1_15119_20160127T145711442_RSC_195702944_012716_165139828_rmadata_zip\/RmaData_disk_JZX0UYNJ_zip\/legacy_logall_date160125_time110534.log",  
                                                                            
               "size":2636011,                                              
               "magic_number":"text\/x-log",                                 
               "file_checksum":{  
                  "type":"SHA-256",                                                                   
                  "value":"0bc6ffb64d0e0edd42162f0e8822021f351c6474d884c99799669b6bfd0994b3"          
               },  
               "file_permissions":{  
                  "group":"svc_gclm_cp1",  
                  "user":"svc_pclm_cp1"  
               }  
            },  
            "archive_metadata":{  
               "timestamp":1453998927000,  
               "name":"FEPAPPDRMPRD02_1_15119_20160127T145711442_RSC_195702944_012716_165139828_rmadata.zip",  
                                                                              
               "path":"\/landingzone\/customer\/MFG\/symmetrix-rma\/landed\/FEPAPPDRMPRD02_1_15119_20160127T145711442_RSC_195702944_012716_165139828_rmadata.zip",  
                                                                              
               "size":1270016,                                               
               "magic_number":"application\/octet-stream",  
               "archive_checksum":{  
                  "type":"MD5",  
                  "value":"6a54ff27f54ac592629bbc576beb8a02"  
               },  
               "total_extracted_file_count":7,                                
               "archive_permissions":{  
                  "group":"svc_gclm_cp1",  
                  "user":"svc_pclm_cp1"  
               }  
            },  
            "chunk_metadata":null,  
            "data_transformation_metadata":[                                  
               {  
                  "job_id":"job_1449034112285_26980",  
                  "stage":"Co-Location",  
                  "input_parameters":"\/ingest\/continuous\/, \/tmp\/colocationJobTmp\/, colocatedSequenceFile, \/2016\/01\/28\/17\/",  
                  "job_name":"Co-location",  
                  "version":null,  
                  "end_timestamp":1454020893,  
                  "start_timestamp":1454020849,  
                  "data_transformation_output":{  
                     "path":"\/system-of-record\/MFG\/symmetrix-rma\/2016\/01\/28\/17\/colocatedSequenceFile-r-00000",  
                     "offset":null,  
                     "key":null  
                  },  
                  "data_transformation_process":[  
                     {  
                        "os":"Linux_2.6.32-431.59.1.el6.x86_64",  
                        "jvm":"1.7.0_65",  
                        "pid":"33927",  
                        "host":"bdlhdccprd05.isus.emc.com",  
                        "ip":"10.253.76.133",  
                        "log_path":"\/data\/1\/mapred\/local,\/data\/2\/mapred\/local,\/data\/3\/mapred\/local\/userlogs\/job_1449034112285_26980"  
                     }  
                  ],  
                  "started_by":"yarn"  
               }  
            ],  
            "message_id":"1453998962777-384-2678-10.253.72.65",  
            "is_big_file":false,                                          
            "big_file_path":null  
         }
      }'''
        import cStringIO    
        from avro import schema
        from avro.datafile import DataFileWriter, DataFileReader
        from avro.io import DatumWriter, DatumReader
        output = cStringIO.StringIO()
        avroUtil=AvroUtil()
        avroSchema=avroUtil.makeSchema("../app/hdfs/Metadata.avsc")
        writer = DataFileWriter(output, DatumWriter(), avroSchema)
        writer.append(data)
        writer.flush()
        avroObject = output.getvalue()
        output.close()
        return avroObject
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()