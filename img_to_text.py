from PIL import Image
import re
#from dateutil import parser

import pytesseract

#getting data from image
bill_data = pytesseract.image_to_string(Image.open('food-bill1.jpeg'))
print(bill_data)

# name of place 
bill_name = bill_data.split(' ')[0]
print(bill_name)
#Extracting date from data
bill_date_match = re.search(r'\d{2}/\d{2}/\d{2}', bill_data)[0]
print(bill_date_match)

#Get total amt of bill
total_bill_amt = re.search(r'total \d+', bill_data, re.IGNORECASE)[0]
#total_bill_amt_rs = re.findall(r'Rs. \d+', bill_data, re.IGNORECASE)

print(total_bill_amt)
bill_amt = total_bill_amt.split()[1]
#bill_amt = total_bill_amt.search(bill_data)
print(bill_amt)

with open('new.json', 'w') as file:
    file.write(bill_data)
