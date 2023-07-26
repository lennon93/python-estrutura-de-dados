def exists_word(word, instance):
    result = []

    for item in instance.queue:
        searched_words = []
        nome_item = item['nome_do_arquivo']
        linhas_item = item['linhas_do_arquivo']

        for num_linha, linha in enumerate(linhas_item, start=1):
            if word.lower() in linha.lower():
                searched_words.append({"linha": num_linha})
                
        if searched_words:
            result.append({
                "palavra": word,
                "arquivo": nome_item,
                "ocorrencias": searched_words
            })
    return result

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
