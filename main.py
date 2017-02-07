from functions import Wojewodztwo, Powiat, Gmina
import csv

class Main:

    @classmethod
    def get_objects(cls, file_path):
        file_path = csv.reader(open(str(file_path), "r"))
        object_list = []
        itr = 0
        for row in file_path:
            row = row[0].split("\t")
            if itr == 0:
                pass
            else:
                if row[1] == "":
                    wojewodztwo = Wojewodztwo(row[4])
                    wojewodztwo.woj_num = row[0]
                    object_list.append(wojewodztwo)
                elif row[5] == "powiat":
                    pow = Powiat(row[4])

                    for object in object_list:
                        if isinstance(object, Wojewodztwo) and row[0] == object.woj_num:
                            pow.woj = object
                    pow.pow_num = row[1]
                    object_list.append(pow)
                else:
                    gmina = Gmina(row[4])
                    for object in object_list:
                        if isinstance(object, Wojewodztwo) and row[0] == object.woj_num:
                            gmina.woj = object
                        if isinstance(object, Powiat) and row[1] in object.pow_num:
                            gmina.powiat = object.name
                    gmina.typ = row[5]
                    object_list.append(gmina)



            itr =+ 1

        return object_list

dupa = Main.get_objects("malopolska.csv")
for i in dupa:
    if isinstance(i, Wojewodztwo):
        print(i.name)

