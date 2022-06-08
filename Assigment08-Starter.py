# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Jbentzen,6.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JBentzen,6.6.2022,Modified code to complete assignment 8
    """
    # Constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
            if str(value).isnumeric() == False:
                self.__product_name = value
            else:
                raise Exception("Products cannot be numbers!")

    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        if str(value).isalpha() == False:
            self.__product_price = value
        else:
            raise Exception("Price must be a number!")

    def __str__(self):
        return self.product_name + ',' + self.product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        write_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JBentzen,6.6.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        try:
            file_list = []
            print("Current Products in File: \n")
            f = open(file_name, "r")
            for line in f:
                product, price = line.split(",")
                objP1 = Product(product, price)
                file_list.append(objP1)
            for each in file_list:
                print(each)
            f.close()
            return file_list
        except:
            print("There was an error!")

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of rows
        """
        try:
            f = open(file_name, "w")
            for row in list_of_rows:
                f.write(str(row) + '\n')
            f.close()
            return list_of_rows
        except:
            print("There was an error!")

    @staticmethod
    def add_data_to_list(product, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param Product: object containing product and price
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of object rows
        """
        try:
            list_of_rows.append(product)  # Appended Code
            return list_of_rows
        except:
            print("There was an error!")

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Captures input and output provided from the user:

    static methods:
    output_menu_tasks():
    input_menu_choice():
    print_data_from_list(list_of_rows):
    input_new_product_and_price():

    changelog: (When,Who,What)
        JBentzen, 6.6.2022, Created Class
    """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Show Current list of Products
        3) Save Data to File
        4) Read Data from File        
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_data_from_list(list_of_rows):
        """ Prints the current list of products

        :param list_of_rows: (list) with current products:
        """
        try:
            for each in list_of_rows:
                print(each)
        except:
            print("There was an error!")

    @staticmethod
    def input_new_product_and_price():
        """  Gets task and priority values to be added to the list

        :return: (object) with product and price
        """
        try:
            product = input("Please enter a Product: ")
            price = input("Please enter the price: ")
            objP1 = Product(product, price)
            return objP1
        except Exception as e:
            print(e)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data to main list on start

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
      # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if (choice_str.strip() == '1'):  # Add a new Task
        obj_product = IO.input_new_product_and_price()
        table_lst = FileProcessor.add_data_to_list(obj_product, lstOfProductObjects)
        continue  # to show the menu

    elif (choice_str == '2'):  # Show Current Product List
        IO.print_data_from_list(lstOfProductObjects)
        continue  # to show the menu

    elif (choice_str == '3'):  # Save Data to File
        table_lst = FileProcessor .write_data_to_file(strFileName, lstOfProductObjects)
        print("Data Saved!")
        continue  # to show the menu

    elif (choice_str == '4'):  # Read Data from File
        table_lst = FileProcessor.read_data_from_file(strFileName)
        continue  # to show the menu

    elif (choice_str == '5'):  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

    else:
        print("Please Select Numbers 1-5!")

# Main Body of Script  ---------------------------------------------------- #

