from ting_file_management.abstract_queue import AbstractQueue
# inicia o projeto

class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []
        
    def __len__(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Índice Inválido ou Inexistente")

    def search(self, index):
        if 0 <= index < len(self.queue):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")


