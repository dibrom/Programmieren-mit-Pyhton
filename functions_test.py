#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
#  Import other ipynb files
import import_ipynb
import functions as fn
import pandas as pd


# In[2]:


class TestFunctions(unittest.TestCase):

    # Test class for unittests in functions.ipynb
    # unittest for quaderror function
    get_ipython().run_line_magic('tb', '')
    def test_quad_error(self):
        result = fn.Value_functions.quad_error(2,4)
        self.assertEqual(result, 4, "Der quadratische Fehler muss 4 betragen")
        
        
    def test_euclidean_distance(self):
        result = fn.Value_functions.euclidean_distance(0,1,0,4)
        self.assertEqual(result, 3, "Der euklidische Abstand muss 3 betragen")
    
    def test_read_csv_to_dataframe(self):
        result = fn.Read_Dataframe.read_csv_to_dataframe('train.csv')
        self.assertIsInstance(result, pd.DataFrame)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

