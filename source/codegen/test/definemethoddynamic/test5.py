class Test:
    def __init__(self):
        exec "def dfunc(msg):\n print msg"
        #exec "dfunc('Hello from __init__.')"
        exec "self.dfunc = dfunc"

    def show(self, msg):
        self.dfunc(msg)



d = Test()
d.show('hello')		
