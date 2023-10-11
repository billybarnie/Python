import csv
from datetime import datetime

def main():
     
    try:
        products_dict = read_dictionary("products.csv", 0)
        print("Buc-ee's")
        print()
        sum = 0
        total = 0
        with open("request.csv", "rt") as requestfile:

            request_csv = csv.reader(requestfile)

            next(request_csv)

            for line in request_csv:

                # Index 0 of the request.csv
                keys = line[0]
                # Index 1 of the request.csv
                quantity = int(line[1])
                # products_dict matches the keys in the request.csv file to the keys in the products_dict
                item = products_dict[keys]
                # grabs the name of the item from the products_dict
                name = item[1]
                # grabs the price of the item from the products_dict
                price = float(item[2])

                sum += quantity
                total += quantity * price
                
                print(f"{name}: {quantity} @ {price}")

            tax = total * 0.06
            entire = tax + total
            print()
            print(f"Number of Items: {sum}")
            print(f"Subtotal: ${total:.2f}")
            print(f"Sales Tax: ${tax:.2f}")
            print(f"Total: ${entire:.2f}")

            current_date = datetime.now()
            no = current_date.weekday()
            
            if no == 4 or no == 5:
                disc = entire * .1
                a = entire - disc
                print(f"You have gotten a 10% discount as today is thursday or friday!")
                print(f"Your total with the discount: ${a:.2f}")
            
            print()
            print("Thank you for shopping at Buc-ee's")
            print(f"{current_date:%a %b %w %I:%M:%S %Y}")
    
    except KeyError as key_err:
        print()
        print(f"Errer: Unknown product ID in the request.csv file"
                f" {key_err}")


    except FileNotFoundError as not_found_err:
        print("Error: missing file")
        print(f"{not_found_err}")



def read_dictionary(filename, key_column_index):

    dictionary = {}
    with open(filename, "rt") as productfile:

        product_csv = csv.reader(productfile)

        next(product_csv)

        for line in product_csv:

            key = line[key_column_index]

            product = line[1]

            price = line[2]
            
            dictionary[key] = [key, product, price]

    return dictionary

if __name__ == "__main__":
    main()