from regions import *
from powiaty import *

class Gmina(Region):
    list_of_gminas = []

    def __init__(self, name):
        super().__init__(name)
        self.woj = ""
        self.powiat = ""
        self.gmi = 0
        self.powiat_num = 0
        self.rgmi = 0
        self.typ = ""
        self.list_of_gminas.append(self)

    def __repr__(self):
        return " {} ".format(self.name)

    @classmethod
    def get_count(cls, type):
        type_list = []
        for i in cls.list_of_gminas:
            if i.typ == type:
                type_list.append(i)
        count = len(type_list)
        return "{} {}".format(type, count)

    @classmethod
    def get_statistics(self):
        """This methods returns statistics of csv (basicaly it uses counting methods of each class)"""
        list_of_rows = []
        row1 = Wojewodztwo.get_wojewodztwa_count()
        row2 = Powiat.get_powiat_count()
        row3 = Gmina.get_count("gmina wiejska")
        row4 = Gmina.get_count("gmina miejska")
        row5 = Gmina.get_count("gmina miejsko-wiejska")
        row6 = Gmina.get_count("obszar wiejski")
        row7 = Gmina.get_count("miasto")
        row8 = Gmina.get_count("miasto na prawach powiatu")
        list_of_rows.extend([row1, row2, row3, row4, row5, row6, row7, row8])

        return list_of_rows


    @classmethod
    def display_3_cities_with_longest_names(cls):
        """This method iterates through list of gminas, picks a postion with type 'city'
        and finds the longest 'name' string"""
        longest_dict = {1: "", 2: "", 3: ""}
        for gmina in cls.list_of_gminas:
            if gmina.typ == "miasto":
                if len(gmina.name) > len(longest_dict[1]):
                    longest_dict[1] = gmina.name
                elif len(gmina.name) > len(longest_dict[2]):
                    longest_dict[2] = gmina.name
                elif len(gmina.name) > len(longest_dict[3]):
                    longest_dict[3] = gmina.name

        return longest_dict

    @classmethod
    def display_county_name_with_largest_num_of_communities(cls):
        """Similar like last one, but it takes a number of county
        and counts the positions until it reaches another number.
        Then, it compares it with last greatest one and returns the
        greatest number of all (but not necessarily 42)"""

        county_dict = {}
        current_type = 0
        for name in cls.list_of_gminas:
            if name.powiat == "":
                pass
            if name.powiat not in county_dict:
                county_dict[name.powiat] = 1
                current_type = name.rgmi
            else:
                if name.rgmi != current_type:
                    county_dict[name.powiat] += 1
        try:
            largest_com_county = max(county_dict, key=county_dict.get)
        except ValueError:
            return ""

        return largest_com_county



    @classmethod
    def multiple_categories(cls):
        """This method checks if any name comes with different
        category. It just compares strings."""
        name_list = []
        multi = []
        for object in Gmina.list_of_gminas:
            if len(name_list) < 1:
                name_list.append(str(object.name))
            elif object.name not in name_list:
                name_list.append(str(object.name))
            else:
                multi.append(object)

        return multi

    @staticmethod

    def searcher(user_input):  #I had some proble with docstring here. This method checks
        result = [] # If user input is in object name
        for object in Gmina.list_of_gminas:
            if str(user_input) in str(object.name):
                result.append(object)

        return result