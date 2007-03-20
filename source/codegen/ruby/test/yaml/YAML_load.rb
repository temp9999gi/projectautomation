require "yaml"

test_obj = ["dogs", "cats", "badgers"]

yaml_obj = YAML::dump( test_obj )
                    # -> ---
                    #    - dogs
                    #    - cats
                    #    - badgers

print (yaml_obj == test_obj) #얘는 같지 않다.

print "\n"

ruby_obj = YAML::load( yaml_obj )
                    # => ["dogs", "cats", "badgers"]

print "ruby_obj:", ruby_obj,"\n"

print "isTure:", (ruby_obj == test_obj)
                    # => true

