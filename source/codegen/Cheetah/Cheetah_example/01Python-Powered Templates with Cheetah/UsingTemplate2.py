from default_pyunit import default_pyunit

tmpl = default_pyunit()
tmpl.classundertest = "query_runner"
tmpl.testcases = ['runquery', 'executequery']

print tmpl