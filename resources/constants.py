

class ConstantMeta(type):

    def __setattr__(cls, name, value):
        if name == "PROTO" or name == "HOST" or name == "PORT" or name == "VERSION":
            raise AttributeError("Cannot modify Constant class")
        else:
            return type.__setattr__(cls, name, value)

    def __delattr__(cls, name):
        if name == "PROTO" or name == "HOST" or name == "PORT" or name == "VERSION":
            raise AttributeError("Cannot delete Constant class")
        else:
            return type.__delattr__(cls, name)

        




class Constants(object):
    
    __metaclass__ = ConstantMeta
    PROTO="https://"
    HOST="api.appvigil.co/"
    PORT=""
    VERSION="v1.0/"
    

           
   

    
    
    

    
    
