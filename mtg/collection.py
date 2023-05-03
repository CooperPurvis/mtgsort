import csv
from fuzzywuzzy import process

filename = "bulk.csv"

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)    
    for row in csvreader:
        rows.append(row)
        
print("no of rows %d"%(csvreader.line_num))

#defines col0 'names' 
col0 = [row[0].lower() for row in rows]

# convert all col0 values to lowercase
col0_lower = [x.lower() for x in col0]

#defines col9 'price'
col9 = [row[9] for row in rows]

search_type = input("Enter 'p' to input prices or 'n' for names: ")
if search_type == 'n':
            
    while True:
        search_name = input("\nEnter A Card (or 'quit' to exit): \n").lower()
        if search_name == 'quit':
            break    
        # find closest matches to the input using fuzzywuzzy
        matches = process.extract(search_name.lower(), col0_lower, limit=5)

    # print the closest matches if the input value is not found
        if search_name.lower() not in col0_lower:
            print("Value %s not found \n" % search_name)
            print("Closest matches:\n")
            for match in matches:
                match_index = col0_lower.index(match[0])
                print("%s (score: %d) - %s" % (rows[match_index][0], match[1], rows[match_index][9]))
        else:       
        # search for the input value in the lowercase row 0
            found = False
            for i,val in enumerate(col0_lower):
                if val == search_name.lower():
                    print("Found %s , Price is %s." % (search_name, rows[i][9]))
                    found = True
                    break
    
else:
    while True:
        search_price = input("\nEnter A Price (or 'quit' to exit): \n")
        if search_price == 'quit':
            break    
        # find closest matches to the input using fuzzywuzzy
        matches = process.extract(search_price, col9, limit=5)

    # print the closest matches if the input value is not found
        if search_price not in col9:
            print("Value %s not found \n" % search_price)
            print("Closest matches:\n")
            for match in matches:
                match_index = col9.index(match[0])
                print("%s (score: %d) - %s" % (rows[match_index][9], match[1], rows[match_index][0]))
        else:
            counter = 0
        # search for the input value in the lowercase row 0
            found = False
            for i,val in enumerate(col9):
                if val == search_price:
                    while counter < 50:
                        print("Found %s , Name is %s." % (search_price, rows[i][0]))
                        counter = counter + 1
                        found = True
                        break
            




