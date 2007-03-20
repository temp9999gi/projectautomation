class Test(object):
    def __init__(self):
        exec "def dfunc(msg):\n print msg"
        dfunc('Hello from __init__.')
        self.dfunc = dfunc

    def show(self, msg):
        self.dfunc(msg)



d = Test()
d.show('hello')		
