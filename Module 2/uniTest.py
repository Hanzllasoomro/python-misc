import unittest

def join_names(name1, name2):
    return " ".join([name1.capitalize(), name2.capitalize() ])

return_data = join_names("hanzlla","Soomro")
print(return_data)

class TestStringMethods(unittest.TestCase):
    def test_isCapitalized(self):
        temp1 , temp2 = return_data.split(" ")
        self.assertTrue(temp1.istitle())
        self.assertTrue(temp2.istitle())
    def test_length(self):
        self.assertTrue(len(return_data.split(" ")), 2)
    def test_split(self):
        self.assertEqual(type(return_data), str)

if __name__ == '__main__':
    unittest.main()