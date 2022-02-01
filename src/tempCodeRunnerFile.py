
def analyze_log(path_to_file):
    raise NotImplementedError
    with open(path_to_file, 'r') as archive:
        arc_csv = csv.reader(archive, delimiter=',')
        lista = list(arc_csv)
        return print(lista)
