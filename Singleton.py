
# Singleton

# Primeiro Singleton por https://www.python.org/dev/peps/pep-0318/#examples
def  singleton ( cls ):
    instâncias = {}
    def  getinstance ():
        se  cls  não está  em instâncias:
            instâncias [ cls ] =  cls ()
        retornar instâncias [ cls ]
    return getinstance

@singleton
classe MyClass

# Segundo Singleton
Classe  Singleton :
    # Aqui será a instância armazenada.
    __instance =  None

    @ staticmethod
    def  getInstance ():
        "" " Método de acesso estático. " ""
        if Singleton .__ instance ==  None :
            Singleton ()
        return singleton .__ instance

    def  __init__ ( self ):
        "" " Construtor virtualmente privado. " ""
        if Singleton .__ instance ! =  None :
            raise  Exception ( " Esta classe é um singleton! " )
        else :
            Singleton .__ instance =  self
