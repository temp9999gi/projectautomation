require 'yaml'
tree = YAML.load(File.open("tree.yaml"))
print tree[:uses][1] # >> web 