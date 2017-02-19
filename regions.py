

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
        return "{}".format(self.name)

    @classmethod
    def get_wojewodztwa_count(cls):
        return "{} {}".format("Województwo:", len(cls.list_of_wojewodztwa))


