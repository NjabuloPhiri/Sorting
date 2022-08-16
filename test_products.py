import unittest
import csv
import sort_products
from operator import itemgetter, attrgetter


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.products_ = []
    
    def read_csv(self):
        products_file = open('products.csv', 'r')
        reader = csv.reader(products_file, delimiter=',')
        next(reader)
        return reader
        
    def sort_by_asc_amount(self):
        res = sorted(self.read_csv(), key=itemgetter(2), reverse=False)
        for item in res:
            self.products_.append(list(enumerate(item)))
        if self.products_:    
            return(res)
    
    #Negative test
    def test_sorted_negative(self):
        res = sorted(self.read_csv(), key=itemgetter(2), reverse=False)
        self.sort_by_asc_amount()
        self.assertNotEqual(res, self.products_)
        
    #Positive test    
    def test_sorted_positive(self):
        res = sorted(self.read_csv(), key=itemgetter(2), reverse=False)
        self.sort_by_asc_amount()
        self.assertTrue(res, reversed)

if __name__ == '__main__':
    unittest.main()