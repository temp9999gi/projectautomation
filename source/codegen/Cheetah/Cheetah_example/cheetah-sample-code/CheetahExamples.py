#!/usr/bin/env python

"""This script demonstrates the various features of the Cheetah
templating system."""

#Create a simple Template in Python code.
#
from Cheetah.Template import Template
from DummyObjects import dummyUser, dummyOrder
definition = """Hello, $user.firstName.

Your order (#$order.id) has shipped:"""
print Template(definition, searchList=[{'user' : dummyUser,
                                        'order' : dummyOrder}])
print '-' * 80

#The following test assumes you've run 'cheetah compile Greeting.tmpl'
#to generate Greeting.py, a Python class corresponding to a Cheetah
#template which you can then import.
#
from Greeting import Greeting
print Greeting(searchList=[{'user' : dummyUser, 'order' : dummyOrder}])
print '-' * 80

#Here we introduce the '#for' directive for loops
#
definition = """Hello, $user.firstName.

Your order (#$order.id) has shipped:
#for $purchased, $quantity in $order.purchased.items():
 $purchased.name: $quantity unit(s)
#end for

Your tracking number is $order.trackingNumber."""
print Template(definition, searchList=[{'user' : dummyUser,
			                'order' : dummyOrder}])
print '-' * 80

#At this point the article just starts listing the Cheetah template
#definitions. Here's a simple method for interpreting those
#definitions.
def printTemplate(definition):
    print Template(definition, searchList=[{'user' : dummyUser,
                                            'order' : dummyOrder}])
    print '-' * 80

#Here we introduce the '#if' directive, but there's a newline problem.
#
printTemplate("""Hello, $user.firstName.
Your order (#$order.id) has shipped:
#for $purchased, $quantity in $order.purchased.items():
 $purchased.name: $quantity unit
#if $quantity != 1
s
#end if
#end for

Your tracking number is $order.trackingNumber.""")

printTemplate("""#for $purchased, $quantity in $order.purchased.items():
 $purchased.name: $quantity unit#slurp
#if $quantity != 1
s
#end if
#end for""")

printTemplate("""#for $purchased, $quantity in $order.purchased.items():
 #if $quantity == 1
  #set $units = 'unit'
 #else
  #set $units = 'units'
 #end if
 $purchased.name: $quantity $units
#end for""")

#Print out the HTML order status page.
printTemplate(open('OrderStatus.tmpl').read())

#Print out the HTML order status page, based on a skeleton page.
from OrderStatus import OrderStatus
print OrderStatus(searchList=[{'user' : dummyUser, 'order' : dummyOrder}])
