from prettytable import PrettyTable

class Table:
    def __init__(self, object_list):
        self.object_list = object_list

    # def __repr__(self):
    #     return "{}".format(self.object_list)

    def make_pretty_table(self):

        table = PrettyTable()
        for object in self.object_list:
            table.add_row([object])

        return table.get_string()
