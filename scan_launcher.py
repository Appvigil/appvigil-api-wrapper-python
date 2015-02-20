import sys
#sys.path.append('./classes')
sys.path.append('./')
from classes.fetchparameter import FetchParameter
from classes.accesstoken import AccessToken
from classes.upload import Upload
from classes.scan import Scan
import argparse
import time
import logging
import json
import re




class ScanLauncher(object):

    def start(self):

        fetchParameter = FetchParameter()
        fetchParameter.takeParameter()

        print fetchParameter.api_key + " " + fetchParameter.api_secret + " " 
        print ('[INFO] Generating AccessToken.......')
        
        accessTokenHandle = AccessToken(fetchParameter.api_key,fetchParameter.api_secret)
        returnData = {}
        if fetchParameter.ttl is None:
            returnData=accessTokenHandle.requestNewAccessToken()
        else:
            returnData=accessTokenHandle.requestNewAccessToken(ttl=fetchParameter.ttl)        
        
        
        accessToken = returnData["access_token"]

        if(accessToken is not None):
        
            print ('[INFO] AccessToken Generated :)')
            print ('[INFO] AccessToken is:'+accessToken)
            print ('[INFO] Uploading APK file to Appvigil Cloud...This may take a while')

            uploadHandle = Upload(accessToken)
            resultData = uploadHandle.newUpload(fetchParameter.app_loc,fetchParameter.app_name)
            print resultData
            uploadId = resultData['upload_id']
        
        
        if(uploadId is not None):
                
            print ('[INFO] App has been uploaded successfully... ')
            print ('[INFO] Upload ID is:'+str(uploadId))                     
            print ('[INFO] Launching vulnerability scan..  ')
            


            scanHandle = Scan(accessToken)           
            resultData = scanHandle.startScan(uploadId,credential_id=fetchParameter.credentials,scan_type=fetchParameter.scan_type)
            #resultData = scanHandle.startScan(uploadId)
            scanId = resultData['scan_id'] 
        
        
        if(scanId is not None):
            
            
                print ('[INFO] Scan launched successfully... ')
                print ('[INFO] Scan ID is:'+scanId)
                print ('[INFO] Scan running...it will be over in few minutes  ')
                print ('[INFO] Please wait...  ')
                
                status = None

                print "Check Scan list...."

                resultData = scanHandle.listScan(2)
                print resultData

                print "#######################################################"

                # print "Checking Status....."
                # while(status is None):
                    
                    
                #     # response = scanHandle.scanStatus(accessToken, scanId)
                #     print ".............."
                #     print "Calling web service"
                    
                #     resultData = scanHandle.scanStatus(scanId)
                    
                #     print resultData['scan_status']

                #     if(resultData['scan_status'] == 'Finished'):
                #         status = 1

                #     print "................"

                # print "........."

                #if(resultData['scan_status'] == 'Finished'):
                accessTokenHandle.flushAccessToken(accessToken)   
                   

if __name__=='__main__' :

    #c=Client()
    #c.start()
    scanLauncher = ScanLauncher()
    scanLauncher.start()                                 



    
    
    

    
    