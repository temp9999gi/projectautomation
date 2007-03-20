# sax06.py  
from xml.sax import make_parser, handler   
import sys 
 
class ProductHandler(handler.ContentHandler):  
    def __init__(self, productName): 
        self.productName = productName 
        self.productList = [] 
        self.charActive = 0 
        self.searchActive = 0 
    def startElement(self, name, attrs): 
        if name == 'product': 
            if self.productName.lower() == attrs.get('name', '').lower(): 
                self.searchActive = 1 
            else: 
                self.searchActive = 0 
            return 
        if not self.searchActive: 
            return 
        if name == 'vendor': 
            self.vendor = attrs.get('name', 'unknown') 
        elif name == 'price': 
            self.model = attrs.get('model', 'unknown') 
            self.priceStr = '' 
            self.charActive = 1 
    def endElement(self, name): 
        if self.searchActive and name == 'price': 
            self.productList.append( (self.vendor, self.model, int(self.priceStr)) ) 
            self.charActive = 0 
    def characters(self, content): 
        if self.charActive: 
            self.priceStr += content 
    def endDocument(self):    # 문서의 끝에서 호출된다  
        self.productList.sort(lambda a, b: cmp(a[2], b[2])) 
        for product in self.productList: 
            print '%-7s %6s %5s' % product 
 
if __name__ == '__main__': 
    h = ProductHandler(sys.argv[1]) 
    parser = make_parser()   
    parser.setContentHandler(h)   
    parser.parse('product.xml') 
