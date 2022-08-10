import unittest


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.products_ = [
                          'Nike', 'Red', '20.00',
                          'Vans', 'Blue', '10.00',
                          'Nike', 'Green', '10.00',
                          'New Balance', 'White', '50.00',
                          'Adidas', 'Blue', '30.00',
                        ]

    def test_ascending(self):
        items = sorted(self.products_, reverse=False)
        self.assertTrue(items, self.products_)
        print(items)


if __name__ == '__main__':
    unittest.main()
