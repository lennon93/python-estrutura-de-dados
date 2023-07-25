import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)

    sys.stdout.write(str(data))


def remove(instance):
    if not len(instance):
        print("Não há elementos")
    else:
        removed = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(str(f"Arquivo {removed} removido com sucesso\n"))

def file_metadata(instance, position):
    if not 0 <= position < len(instance):
        print('Posição inválida', file=sys.stderr)
    else:
        response = instance.search(position)
        sys.stdout.write(str(response))
