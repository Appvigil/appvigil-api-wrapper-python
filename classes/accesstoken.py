import logging
import sys
#sys.path.append('../resources')


#from constants import Constants
from resources.httpconnection import HttpConnection




class AccessToken(object):
    
    
    def __init__(self,api_key,api_secret):
     
        self.api_key = api_key
        self.api_secret = api_secret      
    
    
    def requestNewAccessToken(self,**kwargs):
      
        params={'api_key':self.api_key, 'api_secret':self.api_secret}
            
        if kwargs is not None:
            for key,value in kwargs.iteritems():
                if key == "product_id" or key == "license_key" or key == "appvigil_server_key" or key == "appvigil_app_key" or key == "ttl":
                    params[key] = value
                else:
                    continue
            
        
        host = HttpConnection()
        responseJSON=host.get("access_token/request/", params)
        returnData = {}
       
       
        try:            
            message=responseJSON.json()['response']['message']            
            code=responseJSON.json()['meta']['code']
            returnData["message"] = message
            returnData["code"] = code           
            
            if (code==200):
                
                # if(verbose==1):
                   
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #              + "        [code] =>"+str(responseJSON.json()['meta']['code'])+"\n        [request_id] =>"+responseJSON.json()['meta']['request_id']+"\n     )\n\n"
                #              + "  [response]=> stdClassObject\n     (\n"
                #              + "        [access_token] =>"+responseJSON.json()['response']['access_token']+"\n        [ttl_in_seconds] =>"+str(responseJSON.json()['response']['ttl_in_seconds'])+"\n        [message] =>"+responseJSON.json()['response']['message']+"\n     )\n\n"
                #              + ")\n");
                returnData["access_token"] = responseJSON.json()['response']['access_token']
                returnData["ttl_in_seconds"] = responseJSON.json()['response']['ttl_in_seconds']
            
            return returnData           
       
        except:
            message=responseJSON.json()['response']['message']
            logging.error(message) 
            sys.exit(0)    
        
       
        
        logging.error(message) 
        sys.exit(0)   
    
    
    
    def renewAccessToken(self,accessToken,**kwargs):
        
        
        if accessToken is None:
            sys.exit(0)

        else:
            params={'access_token':accessToken}

            if kwargs is not None:
                for key,value in kwargs.iteritems():
                    if key == "new_ttl":
                        params[key] = value
                
            host = HttpConnection()
            responseJSON=host.get("access_token/renew/", params)
            returnData = {}
            
            #k=j.json()['response']['message']
            
            
            #print k
            try:
                
                message=responseJSON.json()['response']['message']            
                code=responseJSON.json()['meta']['code']
                returnData["message"] = message           
                returnData["code"] = code

                if (code==201):
                    
                    # if(verbose==1):
                       
                    #     print('\n[DEBUG] stdClassObject')
                    #     print("(\n  [meta]=> stdClassObject\n     (\n"
                    #              + "        [code] =>"+str(responseJSON.json()['meta']['code'])+"\n        [request_id] =>"+responseJSON.json()['meta']['request_id']+"\n     )\n\n"
                    #              + "  [response]=> stdClassObject\n     (\n"
                    #              + "        [access_token] =>"+responseJSON.json()['response']['access_token']+"\n        [ttl_in_seconds] =>"+str(responseJSON.json()['response']['ttl_in_seconds'])+"\n        [message] =>"+responseJSON.json()['response']['message']+"\n     )\n\n"
                    #              + ")\n");
                    
                    returnData["access_token"] = responseJSON.json()['response']['access_token']                
                    returnData["ttl_in_seconds"] = responseJSON.json()['response']['ttl_in_seconds']                
                return returnData            
            
            except:
                message=responseJSON.json()['response']['message']
                logging.error(message) 
                sys.exit(0)       
            
            
            logging.error(message) 
            sys.exit(0)  
    
    
    
    def viewAccessToken(self,accessToken):       
        
       
        params={'access_token':accessToken}
        host = HttpConnection()
        responseJSON=host.get("access_token/view/", params)
        returnData = {}
       
        try:            
            message=responseJSON.json()['response']['message']            
            code=responseJSON.json()['meta']['code']
            returnData["message"] = message
            returnData["code"] = code           
            if (code==200):
                
                # if(verbose==1):
                   
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #              + "        [code] =>"+str(responseJSON.json()['meta']['code'])+"\n        [request_id] =>"+responseJSON.json()['meta']['request_id']+"\n     )\n\n"
                #              + "  [response]=> stdClassObject\n     (\n"
                #              + "        [access_token] =>"+responseJSON.json()['response']['access_token']+"\n        [ttl_in_seconds] =>"+str(responseJSON.json()['response']['ttl_in_seconds'])+"\n        [message] =>"+responseJSON.json()['response']['message']+"\n     )\n\n"
                #              + ")\n");

                returnData["access_token"] = responseJSON.json()['response']['access_token']
                returnData["ttl_in_seconds"] = responseJSON.json()['response']['ttl_in_seconds']
                returnData["issue_date_time"] = responseJSON.json()['response']['issue_date_time']
            return returnData           
        
        except:
            message=responseJSON.json()['response']['message']
            logging.error(message) 
            sys.exit(0)    
        
        
        
        logging.error(message) 
        sys.exit(0) 
        
    
    
    def flushAccessToken(self,accessToken):
        
        
        params={'access_token':accessToken}
        host = HttpConnection()
        responseJSON=host.get("access_token/flush/", params)
        returnData = {}

        try:                       
            message=responseJSON.json()['response']['message']                     
            code=responseJSON.json()['meta']['code']            
            returnData["code"] = code            
            returnData["message"] = message
            
            if (code==202):
                
                # if(verbose==1):
                   
                #     print('\n[DEBUG] stdClassObject')
                #     print("(\n  [meta]=> stdClassObject\n     (\n"
                #              + "        [code] =>"+str(responseJSON.json()['meta']['code'])+"\n        [request_id] =>"+responseJSON.json()['meta']['request_id']+"\n     )\n\n"
                #              + "  [response]=> stdClassObject\n     (\n"
                #              + "        [access_token] =>"+responseJSON.json()['response']['access_token']+"\n        [ttl_in_seconds] =>"+str(responseJSON.json()['response']['ttl_in_seconds'])+"\n        [message] =>"+responseJSON.json()['response']['message']+"\n     )\n\n"
                #              + ")\n");

                #resultData['code'] = code
                #resultData['message'] = message
                pass
            
            return returnData           
        
        except:
            message=responseJSON.json()['response']['message']
            logging.error(message) 
            sys.exit(0)    
        
        
        
        logging.error(message) 
        sys.exit(0) 
    
       
        
        
    



        
    
        
        
        
        
        