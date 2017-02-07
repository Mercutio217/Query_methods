import csv
import string

class Region:
    def __init__(self, woj, pow, gmi, rgmi, name, typ):
        self.woj = woj
        self.pow = pow
        self.gmi = gmi
        self.rgmi = rgmi
        self.name = name
        self.type = typ
        self.woj = Wojewodztwo.getby_id(woj)

    # def __str__(self, woj, pow, gmi, rgmi, name, typ):
    #     return "Nr województwa: {}, Nr powiatu: {}, Nr gminy: {}, Rodzaj gminy: {}, Nazwa: {}, Typ: {}".format()

    @classmethod
    def get_objects(cls, file_path):
        file_path = csv.reader(open(str(file_path), "r"))
        object_list = []
        itr = 0
        for row in file_path:
            if itr == 0:
                pass
            else:
                row = row[0].split("\t")
                woj = row[0]
                pow = row[1]
                gmi = row[2]
                rgmi = row[3]
                name = row[4]
                typ = row[5]
                object_list.append(Region(woj, pow, gmi, rgmi, name,typ))
            itr =+ 1

        return object_list



class Funtions(Region):


    @classmethod
    def get_statistics(self, file_path):
        stat_dict = {}
        file_path = super().get_objects(file_path)
        itr = 0
        for row in file_path:
            if itr == 1:
                stat_dict["Title"] = row.name
            else:
                if str(row.type) not in stat_dict:
                    stat_dict[row.type] = 1
                elif str(row.type) in stat_dict:
                    stat_dict[row.type] += 1

            itr += 1

        return stat_dict

    @classmethod
    def three_longest_names(self, file_path):
        file_path = super().get_objects(file_path)
        three_longest = {1 : "", 2 : "", 3 : ""}
        itr = 0
        for row in file_path:
                if row.type == "miasto":
                    if len(row.name) > len(three_longest[1]):
                        three_longest[1] = row.name
                    elif len(row.name) > len(three_longest[2]):
                        three_longest[2] = row.name
                    elif len(row.name) > len(three_longest[3]):
                        three_longest[3] = row.name
        itr += 1

        return three_longest
    @classmethod
    def give_crowdiest_county(self, file_path):
        file_path = super().get_objects(file_path)
        counties_dict = {}
        current_community = 0
        for row in file_path:
            if row.pow != "":
                if row.pow not in counties_dict:
                    counties_dict[row.pow] = 1
                else:
                    if current_community != row.gmi:
                        current_community = row.gmi
                        counties_dict[row.pow] += 1
        biggest_key = ""
        biggest_value = 0
        for key, value in counties_dict.items():
            if int(value) > int(biggest_value):
                biggest_key = key
                biggest_value = value
            else:
                pass

        crowdiest_county = ""

        for i in file_path:
            if i.pow == biggest_key and i.type == "powiat":
                crowdiest_county = "{} {}".format("powiat", i.name)

        return crowdiest_county





for i in Region.get_objects("malopolska.csv"):
    print(str(i))
