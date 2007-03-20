myglobals = {}
myenv = {}
exec "def add(x,y): return x+y" in myglobals, myenv
print myenv['add'](1,2)   
