

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




class Wojewodztwo(Region):
    list_of_wojewodztwa = []
    def __init__(self, name):
        super().__init__(name)
        self.woj_num = 0
        self.list_of_wojewodztwa.append(self)

    def __repr__(self):
        return "Województwo: {}".format(self.name)



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

        return len(cls.list_of_powiats)





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
    def get_gmina_count(cls, typ):
        counter = 0

        for gmina in self.list_of_gminas:
            if self.typ == typ:
                counter += 1

        return counter

    

class Attributes:

    @classmethod
    def get_attributes(cls):
        with open("malopolska.csv", "r") as f:
            reader = csv.reader(f, delimiter='\t')

            for row in reader:
                if row[5] == "województwo":
                    wojewodztwo = Wojewodztwo(row[4])
                    wojewodztwo.woj_num = row[0]

                elif row[5] == "powiat":
                    powiat = Powiat(row[4])
                    for woj in Wojewodztwo.list_of_wojewodztwa:
                        if row[0] == woj.woj_num:
                            powiat.woj = woj.name
                            powiat.pow_num = row[1]
                # elif

                elif row[5] != "powiat" and row[5] != "województwo" and row[0] != "nazwa":
                    gmina = Gmina(row[4])
                    for powiat in Powiat.list_of_powiats:
                        if powiat.pow_num == row[1]:
                            gmina.powiat = powiat.name
                            gmina.woj = powiat
                            gmina.gmi = row[2]
                            gmina.rgmi = row[3]
                            gmina.typ = row[5]
                        else:
                            gmina.powiat = gmina.name
                            gmina.woj = powiat
                            gmina.gmi = row[2]
                            gmina.rgmi = row[3]
                            gmina.typ = row[5]





