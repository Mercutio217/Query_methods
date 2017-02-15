from funtions import *

class Data:

    @classmethod
    def get_data(cls):
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





