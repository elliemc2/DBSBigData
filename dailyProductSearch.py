#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:07:16 2020

@author: Elaine
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_soup(params):
    response = requests.get('https://shop.supervalu.ie/shopping/search/allaisles', params=params)
    soup = BeautifulSoup(response.content, features="html.parser")
    #print(soup.prettify())
    return soup

def get_csv_file_name(product_type):
    csv_name = 'Todays_' + product_type + '_today.csv'
    #print(csv_name)
    return csv_name

def output_DataFrame(listofproducts, filename):
     #convert the list to a dataFrame so it can be written out to csv file
    todays_list = pd.DataFrame(listofproducts, columns = ['Product Name', 'Price', 'Per Kg', 'Promotion'])
    todays_list.to_csv(filename, index = False)
    print(todays_list)
    
def is_empty(string):
	return not string.strip()

def check_string_is_empty(productString):
    productString = productString.strip()
    if productString:
        return productString
    else:
        return ('NA')
    
def create_list_of_products(products):
    product_list = []
    for product in products:
        
        productdesc = check_string_is_empty(product.find(class_='product-list-item-details-title').get_text().strip())
        price = check_string_is_empty(product.find(class_='product-details-price-item').get_text().strip())
        pricekg = check_string_is_empty(product.find(class_='product-details-price-per-kg').get_text().strip().split(' ')[0])
        promotion = check_string_is_empty(product.find(class_='product-details-promotion-name').get_text().strip())
        
        lineitem = (productdesc, price, pricekg,promotion)
        product_list.append(lineitem)
    print(product)
    return product_list

def get_pages(showing_total_products): 
    #print(total_products_line)
    total_products = int(showing_total_products[3])
    products_per_page = int(showing_total_products[1].split('-')[1])
    #print ('Total products' , total_products)
    #print('Products per page', products_per_page)
    how_many_pages = (total_products//products_per_page)+1
    #print('how many pages',total_pages)
    return how_many_pages
    
def main(product_type):
    if product_type:
        params_first_request = (('q', product_type),)
        all_product_type_soup = get_soup(params_first_request)
        #Find how many products we have so we can create the next request with correct page number
        total_products_line = all_product_type_soup.find(id = 'product-count-info').get_text().split(' ')
        #now how many pages of that product
        total_pages = get_pages(total_products_line)
        #find the product aisle
        params_second_request = (('q', product_type),('page', total_pages),)
        #print(total_pages)
        product_soup = get_soup(params_second_request)
        product_class =  'col-xs-6 col-sm-4 col-md-2-4 ga-impression ga-product'
        #find all the product items
        products = product_soup.find_all(class_= product_class)
        #call method to loop through all the products to capture the data about each product item.
        product = create_list_of_products(products)
        filename = get_csv_file_name(product_type)
        output_DataFrame(product, filename)
        print('File generated: ', filename)
    else:
        print('No results')
    

search_for = str('bread')
main(search_for)


  