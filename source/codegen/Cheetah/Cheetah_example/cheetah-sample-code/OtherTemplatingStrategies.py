#!/usr/bin/env python

"""This script demonstrates templating strategies built into
Python. These strategies work in simple cases but they typically don't
support member lookups, method calls, or flow control."""

#You can generate the text in question entirely through Python code.
#Here you're not using a templating system at all.
from DummyObjects import dummyUser, dummyOrder
l = []
l.append('Hello, ')
l.append(dummyUser.firstName)
l.append('.\n\nYour order (#')
l.append(str(dummyOrder.id))
l.append(') has shipped:\n')
for purchased, quantity in dummyOrder.purchased.items():
     l.append(' ')
     l.append(purchased.name)
     l.append(': ')
     l.append(str(quantity))
     l.append(' unit(s)\n')
l.append('\nYour tracking number is ')
l.append(dummyOrder.trackingNumber)
l.append('.')
print ''.join(l)
print '-' * 80

#You can embed printf-like codes in a string, and fill in the blanks with
#either a tuple or a map:
print 'Hello, %s.\n\nYour order (#%d) has shipped:' % (dummyUser.firstName, dummyOrder.id)
print '-' * 80

print 'Hello, %(firstName)s.\n\nYour order (#%(orderID)d) has shipped:' % \
{'firstName' : dummyUser.firstName, 'orderID' : dummyOrder.id}
print '-' * 80

#In Python 2.4 you can use a more modern-looking template format:
from string import Template
from DummyObjects import dummyUser, dummyOrder
t = Template('Hello, $firstName.\n\nYour order (#$orderID) has shipped:')
print t.substitute({'firstName' : dummyUser.firstName,
                    'orderID' : dummyOrder.id})
