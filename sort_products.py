import csv
from operator import itemgetter, attrgetter
import collections
import argparse

class SortProducts():
    def __init__(self):
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
    run.read_csv()
    run.sort_by_asc_amount()
    run.sort_by_prod_col_amount_asc()
    run.sort_by_prod_col_amount_desc()

    parser = argparse.ArgumentParser()
    parser.add_argument('--products_file', type=argparse.FileType('r', encoding='UTF-8'),
                        required=True)
    args = parser.parse_args()
    print(args)
    args.products_file.close()
# parser = argparse.ArgumentParser()
# parser.add_argument('products_file', type=argparse.FileType('r'))
# args = parser.parse_args(["products_file", "products.csv"])
# print(type(args.products_file))
# print("~ File: {}".format(args.products_file))

