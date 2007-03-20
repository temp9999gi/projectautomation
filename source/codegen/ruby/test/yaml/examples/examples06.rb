# http://yaml4r.sourceforge.net/doc/page/examples.htm

require 'yaml'
puts( { 'dog' => 'canine',
        'cat' => 'feline',
        'badger' => 'malign' }.to_yaml )
# prints:
#   dog: canine
#   cat: feline
#   badger: malign
