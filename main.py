class Queue():
    def __init__(self):
        self.cards = []

    def push(self, card):
        self.cards.append(card)

    def pop(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop(0)

if __name__ == '__main__':
    queue = Queue()
    queue.push("Card1")
    queue.push("Card2")
    queue.push("Card3")
    
    print(queue.pop())  
    print(queue.pop())  
    print(queue.pop())  
    print(queue.pop())  
