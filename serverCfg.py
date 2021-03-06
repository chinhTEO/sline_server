import yaml

config_path = './cfg/config.yaml'

class ServerCfg:
    __instance = None
    DBpath = ""
    ImgPath = ""
    sphinxSearchServer = '127.0.0.1'
    sphinxSearchPort = 9312

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if ServerCfg.__instance == None:
            ServerCfg()
        return ServerCfg.__instance

    def getConfigFile(self):
        with open(config_path,'r') as file:
            config = yaml.safe_load(file)
            self.DBpath = config['server']['DBpath']
            self.ImgPath = config['server']['ImgPath']
            self.sphinxSearchServer = config['server']['sphinxSearchServer']
            self.sphinxSearchPort = config['server']['sphinxSearchPort']

    def __init__(self):
        """ Virtually private constructor. """
        if ServerCfg.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ServerCfg.__instance = self
            self.getConfigFile()