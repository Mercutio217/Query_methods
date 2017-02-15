

class Region:
    list_of_regions = []
    def __init__(self, name):
        self.name = name
        Region.list_of_regions.append(self)

    def __repr__(self):
        return "{}".format(self.name)

    @classmethod
    def get_regions_count(cls):

        return len(cls.list_of_regions)

    @classmethod
    def get_statistics(self):
        list_of_rows = []
        row1 = Wojewodztwo.get_wojewodztwa_count()
        row2 = Powiat.get_powiat_count()
        row3 = Gmina.get_count("gmina wiejska")
        row4 = Gmina.get_count("gmina miejska")
        row5 = Gmina.get_count("gmina miejsko-wiejska")
        row6 = Gmina.get_count("obszar miejski")
        row7 = Gmina.get_count("obszar miejski")
        row8 = Gmina.get_count("miasto")
        row9 = Gmina.get_count("miasto na prawach powiatu")
        list_of_rows.extend([row1, row2, row3, row4, row5, row6, row7, row8, row9])
        table = Table(list_of_rows)
        table.make_pretty_table()

        return table.make_pretty_table()




class Wojewodztwo(Region):
    list_of_wojewodztwa = []
    def __init__(self, name):
        super().__init__(name)
        self.woj_num = 0
        self.list_of_wojewodztwa.append(self)

    def __repr__(self):
        return "Województwo: {}".format(self.name)

    @classmethod
    def get_wojewodztwa_count(cls):
        return "{}: {}".format("Województwa:", len(cls.list_of_wojewodztwa))

class Powiat(Region):
    list_of_powiats = []

    def __init__(self, name):
        super().__init__(name)
        self.woj = None
        self.pow_num = 0
        self.list_of_powiats.append(self)


    def __str__(self):
        return "Województwo {}, powiat: {}".format(self.woj, self.name)

    @classmethod
    def get_powiat_count(cls):

        return "{}: {}".format("Powiat", len(cls.list_of_powiats))





class Gmina(Region):
    list_of_gminas = []

    def __init__(self, name):
        super().__init__(name)
        self.woj = ""
        self.powiat = ""
        self.gmi = 0
        self.rgmi = 0
        self.typ = ""
        self.list_of_gminas.append(self)

    def __repr__(self):
        return "Gmina: {} Rodzaj: {} Powiat: {} Typ: {} Województwo: {}".format(self.name, self.rgmi, self.powiat, self.typ, self.woj)

    @classmethod
    def get_count(cls, type):
        type_list = []
        for i in cls.list_of_gminas:
            if i.typ == type:
                type_list.append(i)
        count = len(type_list)
        return "{} {}".format(type, count)

    @classmethod
    def display_3_cities_with_longest_names(cls):
        longest_dict = {1 : "", 2 : "", 3 : ""}
        for gmina in cls.list_of_gminas:
            if len(gmina.name) > len(longest_dict[1]):
                longest_dict[1] = gmina.name
            elif len(gmina.name) > len(longest_dict[2]):
                longest_dict[2] = gmina.name
            if len(gmina.name) > len(longest_dict[3]):
                    longest_dict[3] = gmina.name

        return longest_dict

    @classmethod
    def display_county_name_with_largest_num_of_communities(cls):
        largest_county = ""
        largest_count = 0
        current_county = ""
        current_count = 0
        for gmina in cls.list_of_gminas:
            if gmina.powiat != current_county:
                current_county = gmina.powiat
            else:
                current_county += 1

            if current_count > largest_count:
                largest_county = gmina.name

        return largest_county

    def

print(Gmina.display_3_cities_with_longest_names())
    

