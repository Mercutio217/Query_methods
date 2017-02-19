from gminy import *
from table import *

class Ui:
    """The image of options, which user can choose from."""

    image = """""What would you like to do:
                (1) List statistics
                (2) Display 3 cities with longest names
                (3) Display county's name with the largest number of communities
                (4) Display locations, that belong to more than one category
                (5) Advanced search
                (0) Exit program  """
    @classmethod
    def menu(cls):
        """Simple funtion regarding user menu"""

        exit = 0
        while exit == 0:
            print(cls.image)
            choice = input()
            if choice == "1":
                statistics = Gmina.get_statistics()
                print(Table.make_pretty_table(statistics, "Statystyki"))
                back = input("Press any key to continue")
                if back == True:
                    continue
            elif choice == "2":
                cities = Gmina.display_3_cities_with_longest_names()
                print(Table.make_dict_table(cities, "Nr", "Miasta"))
                back = input("Press any key to continue")
                if back == True:
                    continue

            elif choice == "3":
                largest_communities = Gmina.display_county_name_with_largest_num_of_communities()
                print("Result:", largest_communities)
                back = input("Press any key to continue")
                if back == True:
                    continue
            elif choice == "4":
                table = PrettyTable()
                for i in Gmina.multiple_categories():
                    table.field_names = ["Nazwa", "Typ"]
                    table.add_row([i.name, i.typ])

                print(table)
                back = input("Press any key to continue")
                if back == True:
                    continue

            elif choice == "5":
                user_input = input("Please, type phrase which You would like to find ")
                result = Gmina.searcher(user_input)
                print(Table.make_pretty_table(result, "Nazwa"))
                back = input("Press any key to continue")
                if back == True:
                    continue
            elif choice == "0":
                exit = 1
            else:
                continue
