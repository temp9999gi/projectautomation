class Test(object):
    exec "def dfunc(self,msg):\n\tprint msg\nprint 'exec def function'"

    def __init__(self):
        self.dfunc('Msg in init ...')

			
    def show(self, msg):
        self.dfunc(msg)

d = Test()
d.show('hello')



