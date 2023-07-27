import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    no_priority = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": []
        }
    priority_one = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": []
    }
    priority_two = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": []
    }

    queue.enqueue(no_priority)
    queue.enqueue(priority_one)
    queue.enqueue(priority_two)

    assert len(queue) == 3
    assert queue.search(0) == priority_one
    assert queue.search(1) == priority_two
    assert queue.search(2) == no_priority
    assert queue.dequeue() == priority_one
    assert queue.dequeue() == priority_two
    assert queue.dequeue() == no_priority

    assert len(queue) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(1)
