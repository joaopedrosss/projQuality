
class Login():
    def __init__(self,sessionIsActive = False):
        self.__sessionIsActive = sessionIsActive
        self.__user_in_session = None
    
    def getSession(self):
        return self.__sessionIsActive
    
    def setSession(self,value):
        self.__sessionIsActive = value
    
    def getUserInSession(self):
        return self.__user_in_session
    
    def setUserInSession(self, value):
        self.__user_in_session = value

    def validateUser(self,userNew,list_of_user):
        match = False
        for user in list_of_user.getUsuarios():
            match = (userNew.getPass() == user.getPass()) and (userNew.getId() == user.getId())
            if(match):
                return user
        return None
    
    

        
        