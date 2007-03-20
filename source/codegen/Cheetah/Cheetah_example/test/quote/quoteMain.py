import random
from quote import quote

# Define a list of quotations
quotations = [ [ 'It is easier to find people fit to govern themselves than people fit to govern others.', 'Lord Acton' ],\
               [ 'A house divided against itself cannot stand.', 'Abraham Lincoln' ],\
               [ 'Before anything else, preparation is the key to success.', 'Alexander Graham Bell' ] ]

# Pick a random quotation
quotation = random.choice ( quotations )

# Print the product
print quotation ( searchList = [{ 'quotation': quotation [0],'author': quotation [1] }])

# Adding Logic
