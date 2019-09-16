import unittest
import xmlrunner
from pkg.my_multiply import multiply
 
class TestMultiply(unittest.TestCase):
 
    def setup(self):
        print ("setup             class:TestStuff")
 
    def teardown(self):
        print ("teardown          class:TestStuff")
 
    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)
 
    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)
 
    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)
 
    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)
	
    def test_numbers_3_4(self):
        print ('test_strings_3_4  <============================ actual test code')
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        print ('test_strings_a_3  <============================ actual test code')
        self.assertEqual( multiply('a',3), 'aaa')
 
 
 # Run specified test functions and generate xml test report.        
def run_test_suite_generate_xml_report(test_function_name):

    # Create a TestSuite object.
    test_suite = unittest.TestSuite()
	
    # Add test function in the suite.
    test_suite.addTest(TestMultiply(test_function_name))
	
    # Create HtmlTestRunner object and run the test suite.
    test_runner = xmlrunner.XMLTestRunner(output='xml_result')
    test_runner.run(test_suite)   
	
if __name__ == '__main__':
	run_test_suite_generate_xml_report('test_numbers_3_4')
	run_test_suite_generate_xml_report('test_strings_a_3')