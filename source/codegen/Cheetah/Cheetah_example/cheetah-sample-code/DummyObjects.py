"""This is a module full of dummy data objects used by the various
templating examples. There is a dummyUser, who has placed a
dummyOrder, which contains two dummyItems (dummyItem1 and
dummyItem2). In a real application, these objects would be backed by a
database store or something similar."""

class InventoryItem:
    pass

dummyItem1 = InventoryItem()
dummyItem1.stockNumber = 11111
dummyItem1.name = "Widget, blue"

dummyItem2 = InventoryItem()
dummyItem2.stockNumber = 22222
dummyItem2.name = "Widget, green"

class Order:
    def hasShipped(self):
        return hasattr(self, 'trackingNumber')
        
dummyOrder = Order()
dummyOrder.id = 98765
dummyOrder.trackingNumber = '1234567890AB'
dummyOrder.purchased = {dummyItem1 : 1,
                        dummyItem2 : 50}

class User:
    def getOrders(self):
        return self.orders
    
    def getMostRecentOrder(self):
        return self.orders[-1]

    def getFullName(self):
        return self.firstName + ' ' + self.lastName

dummyUser = User()
dummyUser.orders = [dummyOrder]
dummyUser.firstName = "Leonard"
dummyUser.lastName = "Richardson"
