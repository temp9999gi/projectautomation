# A first Cheetah example

from Cheetah.Template import Template
from DummyObjects import dummyUser, dummyOrder
definition = """Hello, $user.firstName.

Your order (#$order.id) has shipped:"""
print Template(definition, searchList=[{'user' : dummyUser,
                                        'order' : dummyOrder}])
