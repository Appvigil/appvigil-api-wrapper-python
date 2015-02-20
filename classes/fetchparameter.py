import sys
import argparse
import time
import logging
import json
import re
import logging

class FetchParameter(object):

    def __init__(self):

        self.api_key=None
        self.api_secret=None
        self.app_loc = None                
        self.app_name="PYTHON_DEFAULT"
        self.credentials=None
        self.ttl=None
        self.verbose=None
        self.digest=True        
        self.scan_type = 2

    def validateandInitialize(self,args):
                

        if re.match("[A-Za-z0-9]{15}",args.api_key) and len(args.api_key) == 15:
            self.api_key = args.api_key
        else:
            sys.exit(0)

        if re.match("[A-Za-z0-9]{15}",args.api_secret) and len(args.api_secret) == 30:
            self.api_secret = args.api_secret
        else:
            sys.exit(0)

        if args.app_loc.endswith("apk"):
            try:
                open(args.app_loc,'rb')
                self.app_loc = args.app_loc
            except Exception, e:
                sys.exit(0)
                    
        else:
            sys.exit(0)

        if(args.credential_id):

            credentials=args.credential_id
                     
            clist=credential_id.split(',')
                     
                     
            for i in range(len(clist)):
                if len(clist[i]) != 8:
                    logging.error('credential_id must be 8 character length')
                    sys.exit(0)
                             
                if not(re.match("[A-Za-z0-9]{8}",clist[i])):
                    logging.error('credential_id must not contains any special characters')
                    sys.exit(0)

            self.credentials = credentials   
                         

        if(args.verbose):                    
            self.verbose=1
                    
        if(args.disable_digest_check):                    
            self.digest=False               
                
        if(args.app_name):                    
            self.app_name=args.app_name
                    
        if(args.scan_type):
            self.scan_type = args.scan_type

    def takeParameter(self):
    
        parser = argparse.ArgumentParser()
        parser.add_argument('-K','--api_key',required=True, help='* Require the ApiKey before executing your jar')
        parser.add_argument('-S','--api_secret',required=True, help='* Require the ApiSecret before executing your jar')
        parser.add_argument('-L','--app_loc',required=True, help='* Require the AppLocation before start your scan')
        parser.add_argument('-A','--app_name', help='Specify your own name')
        parser.add_argument('-C','--credential_id', help='Specify test credential id')
        parser.add_argument('-t','--ttl', help='(optional) value to set ttl(TIME TO LIVE) for access_token')
        parser.add_argument('-v','--verbose',action='store_true', help='Run verbosely')
        parser.add_argument('-d','--disable_digest_check',action='store_true', help='Disable the digest check')
        parser.add_argument('-type','--scan_type',help='(optional) To specify the type of scan. (0 for Static scan, 1 for dynamic and 2 for both)')
        args = parser.parse_args()
        self.validateandInitialize(args)
                
                
                         

#if __name__=='__main__' :

    #c=Client()
    #c.start()
    #scanLauncher = ScanLauncher()
    #scanLauncher.start()                                 



    
    
    

    
    