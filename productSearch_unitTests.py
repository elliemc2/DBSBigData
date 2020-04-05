#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:42:23 2020

@author: Elaine
"""

def get_csv_file_name(product_type):
    csv_name = 'Todays_' + product_type + '_today.csv'
    return csv_name


def get_pages(showing_total_products): 
    total_products = int(showing_total_products[3])
    products_per_page = int(showing_total_products[1].split('-')[1])
    how_many_pages = (total_products//products_per_page)+1
    return how_many_pages


def check_string_is_empty(productString):
    productString = productString.strip()
    if productString:
        return productString
    else:
        return ('NA')


import unittest

class TestSearch(unittest.TestCase):

    def test_getCSVFileName(self):
        self.assertEqual('Todays_bread_today.csv', get_csv_file_name('bread'))
        self.assertEqual('Todays_5_today.csv', get_csv_file_name('5'))
        self.assertEqual('Todays_milk_today.csv', get_csv_file_name('milk'))
        self.assertEqual('Todays_ _today.csv', get_csv_file_name(' '))
        self.assertEqual('Todays__today.csv', get_csv_file_name(''))
        
    def test_getPages(self):
        self.assertEqual(10, get_pages(['\nShowing', '1-30', 'of', '290', 'items\n']))
        self.assertEqual(1, get_pages(['\nShowing', '1-30', 'of', '22', 'items\n']))
        
        
    def test_checkEmptyString(self):
        self.assertEqual('Not Empty',check_string_is_empty('Not Empty'))
        self.assertEqual('NA',check_string_is_empty(''))
        self.assertEqual('NA',check_string_is_empty(' '))
        
            
        
        
        

if __name__ == '__main__':
    unittest.main()
