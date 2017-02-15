from prettytable import PrettyTable

class Table:
    @classmethod
    def make_pretty_table(self, object_list, field_list=None):

        table = PrettyTable()
        for object in object_list:
            if field_list == True:
                table.field_names([field_list])
            else:
                table.field_names = []
            table.add_row([object])

        return table

    @classmethod
    def make_dict_table(cls, dict, field_key=None, field_value=None):

        table = PrettyTable()
        for key, name in dict.items():
            if field_key == True and field_value == True:
                table.field_names = [field_key, field_value]

            elif field_key == True:
                table.field_names = [field_key, ""]
            else:
                table.field_names = ["", ""]
            table.add_row([key, name])

        return table