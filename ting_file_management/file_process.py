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

    print(data)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
