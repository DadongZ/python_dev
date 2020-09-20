import unittest
import script

class TestMain(unittest.TestCase):
    def setUp(self):
        print('in script.py')
    def test_do_stuff(self):
        '''test numbers'''
        test_num = 10
        result = script.do_stuff(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''test strings'''
        test_num = 'abc'
        result = script.do_stuff(test_num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''test none and else'''
        test_num = None
        result = script.do_stuff(test_num)
        self.assertIsNone(result, None)

    def tearDown(self):
        print('clear to release..')

if __name__=='__main__':
    unittest.main() #just run all the tests here