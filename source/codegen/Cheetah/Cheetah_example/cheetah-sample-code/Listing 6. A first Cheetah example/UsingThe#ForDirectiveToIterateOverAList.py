# A first Cheetah example

from Cheetah.Template import Template
from DummyObjects import dummyUser, dummyOrder


definition = """Hello, $user.firstName.

Your order (#$order.id) has shipped:
#for $purchased, $quantity in $order.purchased.items():
 $purchased.name: $quantity unit(s)
#end for

Your tracking number is $order.trackingNumber."""


print Template(definition, searchList=[{'user' : dummyUser,
			                'order' : dummyOrder}])
