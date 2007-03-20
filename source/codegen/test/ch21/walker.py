# walker.py
class Walker:
    def __init__(self, node):
        self.node = node
    def startElement(self, node):
        pass
    def endElement(self, node):
        pass
    def textNode(self, node):
        pass
    def walk(self, node=None):
        if node == None:
            node = self.node
        for node in node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                self.textNode(node)
            elif node.nodeType == node.ELEMENT_NODE:
                self.startElement(node)
                self.walk(node)
                self.endElement(node)
