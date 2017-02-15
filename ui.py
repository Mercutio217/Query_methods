from functions import *

class Ui:
    menu = """""What would you like to do:
                (1) List statistics
                (2) Display 3 cities with longest names
                (3) Display county's name with the largest number of communities
                (4) Display locations, that belong to more than one category
                (5) Advanced search
                (0) Exit program  """
    def menu(self):
        choice = int(input())
        exit = 0
        while exit == 0:
            if choice == 1:
                Region.get_statistics()

            elif choice == 2:
                Gmina.display_3_cities_with_longest_names()
            elif choice == 3:

            elif choice == 4:

            elif choice == 5:
            elif choice == 0:
                exit = 1

