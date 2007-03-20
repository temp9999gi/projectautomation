# A first Cheetah example

from Cheetah.Template import Template
from DummyObjects import dummyUser, dummyOrder

definition = """Hello, $user.firstName.

Your order (#$order.id) has shipped:

#for $purchased, $quantity in $order.purchased.items():
 #if $quantity == 1
  #set $units = 'unit'
 #else
  #set $units = 'units'
 #end if
 $purchased.name: $quantity $units
#end for

Your tracking number is $order.trackingNumber."""


print Template(definition, searchList=[{'user' : dummyUser,
			                'order' : dummyOrder}])
