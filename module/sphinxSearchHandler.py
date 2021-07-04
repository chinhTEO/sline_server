import sphinxapi
from serverCfg import ServerCfg

class sphixSeachHandler:
    def __init__(self):
        cfg = ServerCfg.getInstance()
        self.client = sphinxapi.SphinxClient()    
        self.client.SetServer(cfg.sphinxSearchServer, cfg.sphinxSearchPort)

    def search(self, searchStr):
        return  self.client.Query(searchStr)