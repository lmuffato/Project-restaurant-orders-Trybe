import csv
import os.path


class ReadCsvFile():
    @classmethod
    def get_csv(self, path):
        if not os.path.isfile(path) or not path.endswith(".csv"):
            raise FileNotFoundError(
                "No such file or directory: " "'{}'".format(path)
            )
        new_order = []
        with open(path) as file:
            file_read = csv.reader(file, delimiter=",", quotechar='"')
            for client, order, day in file_read:
                new_order.append(
                    {'client': client, 'order': order, 'day': day}
                )
        return new_order

# https://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python
# https://stackoverflow.com/questions/50401632/f-strings-giving-syntaxerror
