from prettytable import PrettyTable

class Table:

    @classmethod
    def make_pretty_table(cls, object_list, field_list=None):

        table = PrettyTable()
        for object in object_list:
            if field_list != None:
                table.field_names = [field_list]

            table.add_row([object])

        return table

    @classmethod
    def make_dict_table(cls, dict, field_key=None, field_value=None):

        table = PrettyTable()
        for key, name in dict.items():
            if field_key != None and field_value != True:
                table.field_names = [field_key, field_value]

            elif field_key == True:
                table.field_names = [field_key, ""]
            table.add_row([key, name])

        return table