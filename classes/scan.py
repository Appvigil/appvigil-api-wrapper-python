import logging
import sys
#sys.path.append('../resources')


from resources.httpconnection import HttpConnection


class Scan(object):

    def __init__(self,accessToken):
        self.accessToken = accessToken
        pass     
       
    
    def startScan(self,uploadId,**kwargs):

        host = HttpConnection()
        params={'access_token':self.accessToken,'upload_id':uploadId}

        if kwargs is not None:
            for key,value in kwargs.iteritems():
                if (key == "credential_id" and value is not None) or (key == "scan_type" and value is not None):
                    params[key] = value
       
        responseJSON = host.get("scan/start/", params)
        resultData = {}
       
        try:
            
            message=responseJSON.json()['response']['message']
            code=responseJSON.json()['meta']['code']
            resultData['message'] = message
            resultData['code'] = code
            if (code==204):
                
                # if(verbose==1):
                    
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #                  + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                #                  + "  [response]=> stdClassObject\n     (\n"
                #                  + "        [scan_id] =>"+str(j.json()['response']['scan_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                #                  + ")\n");
                                 
                resultData['scan_id'] = responseJSON.json()['response']['scan_id']
                
            return resultData            
       
        except:           
            message=responseJSON.json()['response']['message']
            logging.error(message) 
            sys.exit(0)          
       
        
        logging.error(message) 
        sys.exit(0)          
             
        
  
    def listScan(self,statusType):        
       
        host = HttpConnection()
        params={'access_token':self.accessToken,'status_type':statusType}
        responseJSON = host.get("scan/list/", params)
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
                #                  + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                #                  + "  [response]=> stdClassObject\n     (\n"
                #                  + "        [scan_id] =>"+str(j.json()['response']['scan_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                #                  + ")\n");
                                 
                
                count = 0
                while True:
                    try:
                        indivFile = {}                                                
                        indivFile['scan_id'] = responseJSON.json()['response'][str(count)]['scan_id']               
                        indivFile['scan_status'] = responseJSON.json()['response'][str(count)]['scan_status']                   
                        indivFile['scan_date_time'] = responseJSON.json()['response'][str(count)]['scan_date_time']                 
                        indivFile['finish_date_time'] = responseJSON.json()['response'][str(count)]['finish_date_time']                        
                        indivFile['upload_id'] = responseJSON.json()['response'][str(count)]['upload_details']['upload_id']                
                        indivFile['file_name'] = responseJSON.json()['response'][str(count)]['upload_details']['file_name']                 
                        indivFile['upload_on'] = responseJSON.json()['response'][str(count)]['upload_details']['upload_on']
                        resultData[str(count)] = indivFile

                    except Exception, e:
                        break
                    count = count + 1

            return resultData
                            
        
        except:           
            message=j.json()['response']['message']
            logging.error(message) 
            sys.exit(0)          
        
        
        logging.error(message) 
        sys.exit(0)        

        

    def scanStatus(self,scanId):


        if scanId is None:
            sys.exit(0)

        else:
            host = HttpConnection()
            params={'access_token':self.accessToken,'scan_id':scanId}
            responseJSON = host.get("scan/status/", params)
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
                    #                  + "        [code] =>"+str(j.json()['meta']['code'])+"\n        [request_id] =>"+j.json()['meta']['request_id']+"\n     )\n\n"
                    #                  + "  [response]=> stdClassObject\n     (\n"
                    #                  + "        [scan_id] =>"+str(j.json()['response']['scan_id'])+"\n        [message] =>"+j.json()['response']['message']+"\n     )\n\n"
                    #                  + ")\n");                                                
                    resultData['scan_id'] = responseJSON.json()['response']['scan_id']                
                    resultData['scan_status'] = responseJSON.json()['response']['scan_status']                
                    resultData['scan_date_time'] = responseJSON.json()['response']['scan_date_time']                
                    resultData['finish_date_time'] = responseJSON.json()['response']['finish_date_time']
                    
                    if resultData['scan_status'] == "Finished":
                        resultData['report_url'] = responseJSON.json()['response']['report_url']                
                return resultData
                                
            
            except:           
                message=responseJSON.json()['response']['message']
                logging.error(message) 
                sys.exit(0)       
            
            logging.error(message) 
            sys.exit(0)        

      
       
        
        
        
        
       
        
        
        
        
        
        
        
