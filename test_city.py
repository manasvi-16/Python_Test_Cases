#This pgm contains a test case to check whether the city_functions.py is working fine or not

import unittest
from city_functions import city_function

class Test(unittest.TestCase):
    """Tests the city_function method."""
    
    def test(self):
        new = city_function('mumbai','india')
        self.assertEqual(new,'Mumbai, India')

#This part of code works only when we are directly running this python script.
if __name__ == '__main__':
    unittest.main()
