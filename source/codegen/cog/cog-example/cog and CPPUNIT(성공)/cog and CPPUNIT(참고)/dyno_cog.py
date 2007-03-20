import cog
import re


def cppunit_tests(test_class, header_file):    
    results = []
    pattern = re.compile(".* %s::(test.*)\(\).*" % test_class)
    for line in open(header_file.replace('.h', '.cpp')):
        m = pattern.match(line, 1)
        print '------------'
        print m
        if m:
	        results.append(m.group(1))
    return results


def cppunit_macros(test_class, header_file):
	
    # print '------------'
    # print test_class, header_file
    
    for test in cppunit_tests(test_class, header_file):
        cog.outl("CPPUNIT_TEST(""%s);" % test)


def cppunit_defs(test_class, header_file):
    for test in cppunit_tests(test_class, header_file):
    	cog.outl("void %s();" % test)

