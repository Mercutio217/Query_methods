from regions import Region

class Powiat(Region):
    list_of_powiats = []

    def __init__(self, name):

        super().__init__(name)
        self.woj = None
        self.pow_num = 0
        self.list_of_powiats.append(self)


    def __str__(self):
        return "{}".format(self.name)

    @classmethod
    def get_powiat_count(cls):

        return "{} {}".format("Powiat", len(cls.list_of_powiats))




