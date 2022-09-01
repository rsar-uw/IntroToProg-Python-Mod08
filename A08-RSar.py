# ------------------------------- #
# Title: Assignment08
# Dev: RSar
# Desc: Working with classes
# ChangeLog: (date,name,change)
#       2022/01/01, RRoot, Created started script
#       2022/01/02, RRoot, Added pseudocode to start assignment 8
#       2022/08/28, RSar, Modified code to complete assignment 8
# ------------------------------- #


# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []
errorCode = "Error. Error. : "

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
    changelog: (date,name,change)
        2022/01/01, RRoot, Created Class
        2022/08/28, RSar, Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    # -- Fields --
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self):  # getter
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # setter
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product name must contain a letter.")

    # product_price
    @property
    def product_price(self):  # getter
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # setter
        if float(value) and value >= 0:
            self.__product_price = value
        elif not str(value).isnumeric() or float(value) < 0:
            raise Exception("Price must be a number and cannot be negative.")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "\t $" + '{0:.2f}'.format(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        add_data_to_list(name, price, list_of_rows):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (date,name,change)
        2022/01/01, RRoot, Created Class
        2022/08/28, RSar, Modified code to complete assignment 8
    """
    # -- Fields --
    # -- Constructor --
    # 	   -- Attributes --
    # -- Properties --
    # -- Methods --
    # TODO: Add Code to process data from a file

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        with open(file_name, "r") as file:
            for line in file:
                data = line.split(",")
                row = Product(product_name=data[0].strip(),
                              product_price=data[1].strip())
                list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(name, price, list_of_rows):
        row = (str(name).strip(),
               str(price).strip(), "\n")
        list_of_rows.append(row)
        return list_of_rows

    # TODO: Add Code to process data to a file

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        with open(file_name, "w") as file:
            for item in list_of_rows:
                file.write(str(item.product_name) + "," +
                           str(item.product_price) + "\n")
        file.close()
        print("\tData saved to file: '" + file_name + "'")
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Performs Input and Output tasks

    methods:
        output_menu_tasks():

    changelog: (date,name,change)
         2022/08/28, RSar, Created Class
    """
    # -- Fields --
    # -- Constructor --
    # 	   -- Attributes --
    # -- Properties --
    # -- Methods --
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        print("\n\t" + "="*9 + " Menu of options " + "="*9 +
              "\n\t1 - Show current list of products"
              "\n\t2 - Add product"
              "\n\t3 - Save and exit" +
              "\n\t" + "="*35)

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input("\nSelect an option from the menu "
                           "(1-3): ")).strip()
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_data(list_of_products):
        print("\t-------- List of Products --------")
        for item in list_of_products:
            print("\t" + str(item))
        print("\t" + "-"*35)

    # TODO: Add code to get product data from user
    @staticmethod
    def add_new_product():
        item = Product('', 0)  # instantiates 'null' item object
        while True:
            name = input("Enter product NAME: \t")
            try:
                item.product_name = name
                break
            except Exception as e:
                print("\n\t" + errorCode + str(e) + "\n")
                continue

        while True:
            price = input("\nEnter product PRICE: \t")
            try:
                item.product_price = float(price)
                break
            except Exception as e:
                print("\n\t" + errorCode + str(e))
        print()
        print("\tNew product added: \t" + str(item))
        return item

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try:
    file = open(strFileName)
except FileNotFoundError as e:
    print("\n\t" + errorCode + e.__str__())
except Exception as e:
    print(e)
else:
    lstOfProductObjects = FileProcessor.\
        read_data_from_file(strFileName, lstOfProductObjects)
    while True:
        # Show user a menu of options
        IO.output_menu_tasks()

        # Get user's menu option choice
        choice_str = IO.input_menu_choice()

        # Show user current data in the list of product objects
        if choice_str.strip() == '1':  # show current data
            print()
            print("\tDisplaying current list of products...")
            print()
            IO.show_current_data(lstOfProductObjects)
            continue

        # Let user add data to the list of product objects
        elif choice_str.strip() == '2':  # add product
            print()
            print("\tAdd product information...")
            print()
            lstOfProductObjects.append(IO.add_new_product())
            continue

            # let user save current data to file and exit program
        elif choice_str.strip() == '3':
            # ask user to save and exit
            while True:
                choice = input("\nSave changes to file? [Y/N]: \t")
                if choice.lower() == "y":
                    print()
                    print("\tSaving data to file...")
                    print()
                    FileProcessor.save_data_to_file(strFileName,
                                                    lstOfProductObjects)
                    break
                elif choice.lower() == "n":
                    print()
                    print("\tData not saved to file...")
                    break
                else:
                    print("\n\t" + errorCode + ": Invalid choice.")
                #     continue
            input("\nPress ENTER key to quit the program.")
            break
