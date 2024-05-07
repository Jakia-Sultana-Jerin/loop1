
#Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_file, json_file):
    products = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(row)

    with open(json_file, 'w') as jsonfile:
        json.dump(products, jsonfile, indent=4)

csv_to_json('products.csv', 'products.json')