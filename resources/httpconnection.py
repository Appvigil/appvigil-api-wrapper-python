import requests
import logging
import sys
from urllib import urlencode
from constants import Constants


class HttpConnection(object):
    

    def get(self,resource,params):          
        
        URL = Constants.PROTO + Constants.HOST + Constants.VERSION + resource  
        
        try:
            user_agent = {'User-agent': 'PYTHON_CLI'}
            r=requests.get(URL,headers=user_agent,params=urlencode(params))
        
        except:
            
            logging.error("Couldn't resolve host try again!!")
            sys.exit(0)
        
        return r
    
    
    
    def post(self,resource,access_token,app_name,app,app_digest):
        
        URL = Constants.PROTO + Constants.HOST + Constants.VERSION + resource

        if(app!=None and app_digest==None):
            try:        
                files ={'app': open(app,'rb')}
          
            except:
            
                logging.error('invalid file')
                sys.exit(0)
            
            
            params ={'access_token':access_token,'app_name':app_name}
        
            try:                
                    r = requests.post(URL, files=files, data=params)
                    return r
                
            except:
                    
                    logging.error("parsing error")
                    sys.exit(0)
                    
        else:  
            
                    if(app==None and app_digest!=None):
                       
                            params ={'access_token':access_token,'app_name':app_name,'app_digest':app_digest}
                    
                            try:                        
                                
                                r = requests.post(URL, data=params)
                                return r
                            
                            except:
                                
                                logging.error("parsing error")
                                sys.exit(0)
                                
                                logging.error("parsing error")
                                sys.exit(0)            
        
       
        
        
        
        
         
        
        
        
        
        
        
        
         
        
        
        
        
        
        
        
        
        
