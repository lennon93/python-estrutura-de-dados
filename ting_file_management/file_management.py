import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            if not path_file.endswith('.txt'):
                print('Formato inválido', file=sys.stderr)
                return None

            lines = file.read().splitlines()
            return lines

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return None
