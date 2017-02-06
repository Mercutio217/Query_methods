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

    def give_crowdiest_county(self, file_path):
        file_path = super().get_objects(file_path)
        max_county = []
        current_county = 0
        counter = 0

print(Funtions.three_longest_names("malopolska.csv"))
