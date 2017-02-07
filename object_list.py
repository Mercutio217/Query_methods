import csv
from functions import Wojewodztwo, Powiat, Gmina


class Object_list:

    @classmethod
    def get_wojewodztwo(self, file_name):
        file_name = csv.reader(open(str(file_name), "r"))
        object_list = []
        itr = 0
        for row in file_name:
            row = row[0].split("\t")
            if itr == 0:
                pass
            else:
                if row[1] == "":
                    wojewodztwo = Wojewodztwo(row[4])
                    wojewodztwo.woj_num = row[0]
                    object_list.append(wojewodztwo)
            itr += 1

        return object_list

    @classmethod
    def get_powiats(self, file_name):
        file_name = csv.reader(open(str(file_name), "r"))
        object_list = []
        itr = 0
        for row in file_name:
            row = row[0].split("\t")
            if itr == 0:
                pass
            else:
                if row[5] == "powiat":
                    powiat = Powiat(row[4])
                    list_of_woj = list(Object_list.get_wojewodztwo("malopolska.csv"))
                    for wojewodztwo in list_of_woj:
                        if isinstance(wojewodztwo, Wojewodztwo) and row[0] == wojewodztwo.woj_num:
                            powiat.woj = wojewodztwo
                    powiat.pow_num = row[1]
                    object_list.append(powiat)
            itr += 1

        return object_list



print(Object_list.get_powiats("malopolska.csv"))