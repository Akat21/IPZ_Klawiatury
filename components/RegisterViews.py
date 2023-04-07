class Views():
    def __init__(self):
        self.views={}
        self.n=0
        
    def register(self,name,f,Update=False):
        self.views.update({name:f})
        if not Update:
            self.n+=1

    def getInstance(self,name):
        return self.views[name]()
    
    def getList(self):
        return self.views.keys()
    
    def getN(self):
        return self.n