#*- coding: utf-8 -*-
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testDefaultSize(self):
        assert self.widget.size() == (50,50), 'incorrect default size'
    def testResize(self):
        self.widget.resize(100,150)
        assert self.widget.size() == (100,150), \
               'wrong size after resize'



#if __name__ == "__main__":
#    unittest.main()


widgetTestSuite = unittest.TestSuite()
widgetTestSuite.addTest(WidgetTestCase("testDefaultSize"))
widgetTestSuite.addTest(WidgetTestCase("testResize"))


runner = unittest.TextTestRunner()
runner.run(widgetTestSuite)       
                                          