# 
require 'yaml'

dump( obj, io = nil ) 
Converts obj to YAML and writes the YAML result to io. 

  File.open( 'animals.yaml', 'w' ) do |out|
    YAML.dump( ['badger', 'elephant', 'tiger'], out )
  end

# If no io is provided, a string containing the dumped YAML is returned. 

  YAML.dump( :locked )
     #=> "--- :locked"

