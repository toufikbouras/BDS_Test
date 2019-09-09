
# coding: utf-8

import os
import json
import logging


def extract_products():

#     script_dir = os.path.dirname(__file__)
#     file_path = ('/home/toufik/data.json')
#     with open(file_path) as datafile:
#         data = json.load(datafile)

    def print_av(x, j):

        Product_Price= round(float(x[j]['Price']), 1) 
        Product_Name= x[j]['Name'][:30]
        print(f'You can buy {Product_Name} at our store at {Product_Price}')
        return Product_Name, Product_Price
    
    def print_unav(x, j): 
        y= x[j]['Barcode'] 
        z= x[j]['Name']
        logging.warning(f'product_id is {y}, product name is {z}')


    with open("../data.json") as datafile:
        data = json.load(datafile)

    ls = {}
    for i in range(len(data['Bundles'])):
        for product in data['Bundles'][i]:
            if 'Product' in product:
                try:
                    data['Bundles'][i][product][0]['IsAvailable']
                except:
                    try:
                        data['Bundles'][i][product][1]['IsAvailable']
                    except:
                        logging.error(f'The product is not available')
                    else:
                        if data['Bundles'][i][product][1]['IsAvailable'] == True:
                            x, y = print_av(data['Bundles'][i][product], 1)
                            ls[x] = y
    #                         Product_Price= round(float(data['Bundles'][i][product][1]['Price']), 1) 
    #                         Product_Name= data['Bundles'][i][product][1]['Name'][:30]
    #                         ls[Product_Name] = Product_Price
    #                         print(f'You can buy {Product_Name} at our store at {Product_Price}')
                        else:
                            print_unav(data['Bundles'][i][product], 1)
    #                         y= data['Bundles'][i][product][1]['Barcode'] 
    #                         z= data['Bundles'][i][product][1]['Name']
    #                         logging.warning(f'product_id is {y}, product name is {z}')
                else:
                    if data['Bundles'][i][product][0]['IsAvailable'] == True:
                        x, y = print_av(data['Bundles'][i][product], 0)
                        ls[x] = y
    #                     Product_Price= round(float(data['Bundles'][i][product][0]['Price']), 1) 
    #                     Product_Name= data['Bundles'][i][product][0]['Name'][:29]
    #                     ls[Product_Name] = Product_Price
    #                     print(f'You can buy {Product_Name} at our store at {Product_Price}')

                    else:
                        print_unav(data['Bundles'][i][product], 0)
    #                     y= data['Bundles'][i][product][0]['Barcode'] 
    #                     z= data['Bundles'][i][product][0]['Name']
    #                     logging.warning(f'product_id is {y}, product name is {z}')

    with open('list of the products', 'w') as f:
        for key in ls.keys():
            f.write("%s,%s\n"%(key,ls[key]))
    return(ls)

