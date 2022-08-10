import csv
from operator import itemgetter
import argparse


class SortProducts:
    def __init__(self):
        self.products_ = []

    @staticmethod
    def read_csv():
        products_file = open('products.csv', 'r')
        reader = csv.reader(products_file, delimiter=',')
        next(reader)
        return reader

    def sort_by_asc_amount(self):
        res = sorted(self.read_csv(), key=itemgetter(2), reverse=False)
        for item in res:
            self.products_.append(list(enumerate(item)))
        if self.products_:
            print(self.products_)

    def sort_by_prod_col_amount_asc(self):
        res = sorted(self.read_csv(), key=itemgetter(0), reverse=False)
        for item in res:
            self.products_.append(list(enumerate(item)))
        if self.products_:
            print(self.products_[2])

    def sort_by_prod_col_amount_desc(self):
        res = sorted(self.read_csv(), key=itemgetter(1), reverse=True)
        for item in res:
            self.products_.append(list(enumerate(item)))
        if self.products_:
            print(self.products_[1])


if __name__ == '__main__':
    run = SortProducts()
    parser = argparse.ArgumentParser(description='Sorting script')
    parser.add_argument('-p', '--p', action='store_false')
    args = parser.parse_args()
    run.read_csv()
    run.sort_by_asc_amount()
    run.sort_by_prod_col_amount_asc()
    run.sort_by_prod_col_amount_desc()



