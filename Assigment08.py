# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# NSmith,6/7/2020,Updated code in class Product
# NSmith,6/7/2020,Updated code in class FileProcessor
# NSmith,6/7/2020,Updated code in class IO
# NSmith,6/7/2020,Added Main body code
# NSmith,6/8/2020,Added try-except to Main - Add a Product
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'  # name of file for reading and writing
lstOfProductObjects = []  # list of objects
strChoice = ''  # user menu choice
productName = ''  # name of a product
productPrice = 0.0  # price of a product
productObject = None  # object instance of class Product


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        __init__: initializes product attributes
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NSmith,6/7/2020,Added Constructor
        NSmith,6/7/2020,Added product_name property
        NSmith,6/7/2020,Added product_price property
        NSmith,6/8/2020,Removed try-except statements--\
        will handle errors in IO
    """

    # -- Constructor --
    def __init__(self, name: str, price: float):
        """Sets product name and price

        :param name: (string) name of product:
        :param price: (string) price of product in float format:
        :return: nothing
        """
        # -- Attributes --
        self.product_name = name  # call product_name property method to set name
        self.product_price = price  # call product_price property method to set price

    # -- Properties --
    # Product Name
    @property
    def product_name(self):  # define getter of property product_name
        """ Gets product name

        :return: (string) title case of of product name
        """
        return str(self.__product_name).title()  # return string title case product name

    @product_name.setter
    def product_name(self, value: str):  # define setter of property product_name
        """ Sets product name

        :param value: (string) the name of product to set:
        :return: nothing
        """
        self.__product_name = value  # assign value to hidden attribute

    # Product Price
    @property
    def product_price(self):  # define getter of property product_price
        """ Gets product price

        :return: (float) product price
        """
        return self.__product_price  # return string title case product price

    @product_price.setter
    def product_price(self, value: float):  # define setter of property product_price
        """ Sets product price

        :param value: (string) product price in float format:
        :return: nothing
        """
        self.__product_price = float(value)  # assign float(value) to hidden attribute


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NSmith,6/7/2020,Added read_data_from_file static method
        NSmith,6/7/2020,Added save_data_to_file static method
        NSmith,6/8/2020,Added try-except to read_data_from_file
    """

    # Code to process data from a file into a list
    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file and stores in a list

        :param file_name: (string) with name of file:
        :return: (list) of product names and prices
        """
        lst = []  # create empty list object
        try:  # check if file can be opened first i.e. does it exist?
            f = open(file_name, "r")  # open file in read mode
        except Exception:
            print("Catalog file does not exist.")
            print("Starting with empty product list.")
        else:  # run this code if try succeeds
            for line in f:  # iterate through each line in file
                prod, price = line.split(",")  # split line with comma separator
                prodObj = Product(prod, price)  # create object from Product class
                lst.append(prodObj)  # store object to list
            f.close()  # close the file
        return lst  # return a list of objects

    # Code to process list data to a file
    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Writes data from a list to a file

        :param file_name: (string) with name of file to write to:
        :param list_of_product_objects: (list) of data to be written to file:
        :return: nothing
        """
        f = open(file_name, "w")  # open file with write mode
        for row in list_of_product_objects:  # iterate through rows in the list
            # write each row of list to the file
            f.write(row.product_name + "," + str(row.product_price) + "\n")
        f.close()  # close file


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input and output tasks:

    methods:
        print_menu_Tasks():
        input_menu_choice(): -> (a string representing user's choice)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NSmith,6/7/2020,Added print_menu_Tasks static method
        NSmith,6/7/2020,Added input_menu_choice static method
        NSmith,6/7/2020,Added print_current_product_list static method
        NSmith,6/7/2020,Added input_product_and_price static method
        NSmith,6/7/2020,Added input_press_to_continue static method
        Nsmith,6/8/2020,Added try-except to input_product_and_price
    """

    # Static Method to show menu to user
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Display the menu
        print('''
        Menu of Options
        1) Print Current Products and Prices
        2) Add a Product to the Catalog
        3) Save Catalog to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # Static method to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) user's choice
        """
        # Get user's choice, strip whitespace, and store in string variable choice
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice  # return choice

    # Static Method to show the current data in product list
    @staticmethod
    def print_current_product_list(product_list: list):
        """ Shows the current product list saved to file

        :param file_name: (string) name of file containing product info
        :return: nothing
        """
        # Print header
        print("******** Catalog Items ********")
        print("________Product | Price________")
        # iterate through the list of items in the file
        for item in product_list:
            # print the product name and price
            print(f"\t{item.product_name} | {item.product_price}")
        # print a footer
        print("*******************************")
        print()  # Add an extra line for looks

    # Static Method to get product data from user
    @staticmethod
    def input_product_and_price():
        """ Gets user to input a product and price

        :param: nothing:
        :return: (tuple) with value of product and price
        """
        # get product name from user
        str_prod = str(input("Enter a product name: ").strip())
        # check if input is valid product name
        try:
            if not(not str_prod.isnumeric() and "." not in str_prod):
                # raise exception if number in name
                raise Exception("You did not enter a valid product name.\n")
        except Exception as e:
            print(e)
        else:  # if user entered valid product name, now ask for price
            str_price = str(input("Enter the price: ").strip())
            try:
                #  try to convert string to float
                flt_price = float(str_price)
            except Exception:
                print("Prices must be numbers.\n")
            # Execute the else statement if try successful
            else:
                print()  # Add an extra line for looks
                return str_prod, flt_price  # return the product name and its price

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue...')


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = (FileProcessor.read_data_from_file(strFileName))

while True:
    # Show user a menu of options
    IO.print_menu_Tasks()
    # Get user's menu option choice and store in strChoice
    strChoice = IO.input_menu_choice()

    # Process users input choice
    if strChoice == '1':  # Print current products
        # Show user current data in the list of product objects
        IO.print_current_product_list(lstOfProductObjects)
        IO.input_press_to_continue()  # wait for user to continue

    elif strChoice == '2':  # Add a product
        # Let user add data to the list of product objects
        try:  # try to run code, basically check if inputs are valid
            productName, productPrice = IO.input_product_and_price()  # unpack tuple
        # if try fails run this exception
        except Exception:
            print("Product not added, let's try again.")
        else:  # if try succeeds run this code
            productObject = Product(productName, productPrice)  # create object instance
            lstOfProductObjects.append(productObject)  # append object to list
            IO.input_press_to_continue("Product Added!")  # provide feedback

    elif strChoice == '3':  # Save catalog to file
        # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        IO.input_press_to_continue("File Saved!")  # provide feedback

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")  # provide feedback
        break  # and Exit

    else:  # user did not make a valid selection from the menu
        IO.input_press_to_continue(f"You entered '{strChoice}', "
                                   f"but this is not a valid option.\n")  # provide feedback

# Main Body of Script  ---------------------------------------------------- #
