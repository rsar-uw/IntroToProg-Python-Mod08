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
strFileName = 'products.txt'
lstOfProductObjects = []

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
    # -- Fields --
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

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
            raise Exception("Product name cannot be numbers")

    # product_price
    @property
    def product_price(self):  # getter
        return float(self.__product_price)  # Numeric characters

    @product_price.setter
    def product_price(self, value):  # setter
        if value >= 0:
            self.__product_price = value
        else:
            raise Exception("Price cannot be negative")

    # -- Methods --
    # TODO: Add Code to the Product class
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)


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
        print("\n\tData saved to file: '" + file_name + "'")
        return list_of_rows

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
        """ Display a menu of choice to the user

        :return: nothing
        """
        print("""
    Menu of options
    1 - Show current list of products
    2 - Add product
    3 - Save and exit
        """)

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input("Select an option from the menu "
                           "(1-3): ")).strip()
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_data(list_of_products):
        print("\t======= List of Products =======")
        for item in list_of_products:
            print("\t" + str(item.product_name) + "\t $" +
                  '{0:.2f}'.format(item.product_price))
        print("\t" + "="*len("======= List of Products ======="))

    # TODO: Add code to get product data from user
    @staticmethod
    def add_new_product():
        n = input("Enter product NAME: \t")
        p = input("\nEnter product PRICE: \t")
        # print()
        item = Product(product_name=n,
                       product_price=p)
        return item

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName,
                                                        lstOfProductObjects)

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
        print("\tAdd new product information...")
        print()
        lstOfProductObjects.append(IO.add_new_product())
        continue

        # let user save current data to file and exit program
    elif choice_str.strip() == '3':
        # ask user to save and exit
        print("3")
        lstOfProductObjects = \
            FileProcessor.save_data_to_file(strFileName,
                                            lstOfProductObjects)
        break
