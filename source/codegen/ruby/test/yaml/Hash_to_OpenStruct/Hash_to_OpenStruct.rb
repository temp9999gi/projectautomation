# Hash to OpenStruct 
# http://www.rubyquiz.com/quiz81.html

require "yaml"
require "ostruct"

class Object
    def to_openstruct
        self
    end
end

class Array
    def to_openstruct
        map{ |el| el.to_openstruct }
    end
end

class Hash
    def to_openstruct
        mapped = {}
        each{ |key,value| mapped[key] = value.to_openstruct }
        OpenStruct.new(mapped)
    end
end

module YAML
    def self.load_openstruct(source)
        self.load(source).to_openstruct
    end
end

p YAML.load_openstruct(File.read("sample.yml"))


# C:\_kldp\codegen\ruby\test\yaml\Hash_to_OpenStruct>Hash_to_OpenStruct.rb
# <OpenStruct baz=[1, 2, 3] foo=1 bar=nil a=<OpenStruct z=3 x=1 y=2> quux=42 doctors=["William Hartnel
# l", "Patrick Troughton", "Jon Pertwee", "Tom Baker", "Peter Davison", "Colin Baker", "Sylvester McCo
# y", "Paul McGann", "Christopher Eccleston", "David Tennant"]>