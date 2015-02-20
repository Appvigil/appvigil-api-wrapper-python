
import logging
import sys
#sys.path.append('../resources')

import hashlib
from os.path import basename

from resources.httpconnection import HttpConnection


class Upload(object):
    

    def __init__(self,accessToken):
        self.accessToken = accessToken

    
    def newUpload(self,appLocation,appName,**kwargs):        

        digest = True        

        if kwargs is not None:
            for key,value in kwargs.iteritems():
                if key == "digest" and kwargs['digest'] is not None:
                    digest = value
       
        host = HttpConnection()            
        resultData = {}
        responseJSON = None
        resultData = {}
        
        if (digest == True):
                
                
            appDigest=self.digest_file(appLocation)            
            responseJSON=host.post("upload/new/",self.accessToken,appName,None,appDigest)
                
            try:               
                message=responseJSON.json()['response']['message']
                code=responseJSON.json()['meta']['code']
                  
                if (code==146):
                                  
                    responseJSON=host.post("upload/new/",self.accessToken,appName,appLocation,None)
                    
               
            except:
                message=responseJSON.json()['response']['message']
                logging.error(message) 
                sys.exit(0)  
        
        
        else:                
            responseJSON=host.post("upload/new/",self.accessToken,appName,appLocation,None)
               

        try:                  
            message=responseJSON.json()['response']['message']
            code=responseJSON.json()['meta']['code']
            resultData['message'] = message
            resultData['code'] = code
            if (code==203 or code == 205):
               
                
                # if(verbose==1):
                    
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #         + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                #         + "  [response]=> stdClassObject\n     (\n"
                #         + "        [file_name] =>"+j.json()['response']['file_name']+"\n        [upload_id] =>"+str(j.json()['response']['upload_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                #         + ")\n");
                
                resultData['file_name'] = responseJSON.json()['response']['file_name']
                resultData['upload_id'] = responseJSON.json()['response']['upload_id']
                
            return resultData
                
                
        except:
            #message=j.json()['response']['message']
            logging.error(message) 
            sys.exit(0)  
        
       
        
        logging.error(message) 
        sys.exit(0)   
 
        
       
    def uploadList(self,**kwargs):        
        
        host = HttpConnection()
        params={'access_token':self.accessToken}
        if kwargs is not None:
            for key,value in kwargs.iteritems():
                if key == "count" or key == "this_ses":
                    params[key] = value
                
            
        responseJSON=host.get("upload/list/", params)
        resultData = {}
        try:                       
            
            message=responseJSON.json()['response']['message']
            code=responseJSON.json()['meta']['code']
            resultData['message'] = message
            resultData['code'] = code
            if (code==200):
               
                
                # if(verbose==1):
                    
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #         + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                #         + "  [response]=> stdClassObject\n     (\n"
                #         + "        [file_name] =>"+j.json()['response']['file_name']+"\n        [upload_id] =>"+str(j.json()['response']['upload_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                #         + ")\n");
                count = 0
                while True:
                    try:
                        indivFile = {}                        
                        indivFile['upload_id'] = responseJSON.json()['response'][str(count)]['upload_id']
                        indivFile['app_name'] = responseJSON.json()['response'][str(count)]['app_name']
                        resultData[str(count)] = indivFile
                    except Exception, e:
                        break
                    count = count + 1

            return resultData
                
                
        except:
                
            #message=j.json()['response']['message']
            logging.error(message) 
            sys.exit(0)  
        
        
        
        logging.error(message) 
        sys.exit(0)
       
        #print j.json()['response']['message']
        
        
       
           
        
    
    def uploadDetails(self,uploadId):

        if uploadId is None:
            sys.exit(0)

        else:

            params = {'access_token':self.accessToken,'upload_id':uploadId}
            host = HttpConnection()
            responseJSON = host.get("upload/details/", params)
            resultData = {}
            try:          
                message=responseJSON.json()['response']['message']
                code=responseJSON.json()['meta']['code']
                resultData['message'] = message
                resultData['code'] = code
                if (code==200):
                   
                    
                    # if(verbose==1):
                        
                    #     print('\n[DEBUG] stdClassObject')
                    #     print("(\n  [meta]=> stdClassObject\n     (\n"
                    #         + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                    #         + "  [response]=> stdClassObject\n     (\n"
                    #         + "        [file_name] =>"+j.json()['response']['file_name']+"\n        [upload_id] =>"+str(j.json()['response']['upload_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                    #         + ")\n");
                    resultData['app_name'] = responseJSON.json()['response']['app_name']
                    resultData['app_size_in_bytes'] = responseJSON.json()['response']['app_size_in_bytes']
                    resultData['upload_date_time'] = responseJSON.json()['response']['upload_date_time']
                    resultData['access_token'] = responseJSON.json()['response']['access_token']
                return resultData
                    
                    
            except:
                    
                #message=j.json()['response']['message']
                logging.error(message) 
                sys.exit(0)  
            
            
            
            logging.error(message) 
            sys.exit(0)   
       
        
    

    def digest_file(self,filename):
         
            try:
                genHash = hashlib.sha256()               
                  
                with open(filename,'rb') as appFile:               
                       
                        chunk = 0
                        while chunk != b'':
                         
                            chunk = appFile.read(1024)
                            genHash.update(chunk)               
                 
                return genHash.hexdigest()    
                
                
            except:
                logging.error("couldnt generate digest!!!!") 
                sys.exit(0)   
        
         
                
                
                
                
                
                
                
                
                
                