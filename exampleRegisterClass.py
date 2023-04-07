
#%%
class k:
 def __init__(self,a,b,c):
     self.a=a
     self.b=b
     self.c=c
     print("init k")


class m:
    def __init__(self):
        self.list={}
    def register(self,name,f):
        self.list.update({name:f})
    def getInstance(self,name):
        return self.list[name]()
    def getList(self):
        return self.list.keys()

main = m()
main.register("k",lambda a=1,b=2,c=3:k(a,b,c))
print("test")
kk = main.getInstance("k")
print("done")
for i in main.getList():
    print(i)
# %%
