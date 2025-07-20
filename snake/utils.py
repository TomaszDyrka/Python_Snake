class LinkedList:
    class Node:
        def __init__(self, value:tuple, prev:"LinkedList.Node" = None, next:"LinkedList.Node" = None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, value:tuple):
        self.head = self.Node(value)
        self.length  = 1

    def __len__(self):
        return self.length
    
    def __getitem__(self, key):
        match key:
            case 0:
                current = self.head

            case _ if (key < 0 and abs(key) < self.length):
                current = self.head

                while (key != 0 or current != None):
                    current = current.prev
                    key += 1

            case _ if (key > 0 and abs(key) < self.length):
                current = self.head

                while (key != 0 or current != None):
                    current = current.prev
                    key -= 1

            case _:
                current = None

        return current

    def __setitem__(self, key, value):
        node = self.__getitem__(key)
        if node:
            node.value = value

    def __delitem__(self, key):
        current = self.__getitem__(key)
        self.length -= 1

        if (key == 0 and current.next):
            if current.prev == current.next: # for first item when only 2 available
                self.head = current.next
                self.head.next = None
                self.head.prev = None
            else:                            # normal first item
                self.head = current.next
                self.head.prev = current.prev
                current.prev.next = self.head

        else:
            if current.prev == current.next: # for second item when only 2 available
                self.head.next = None
                self.head.prev = None
            else:                            # every other case
                current.prev.next = current.next
                current.next.prev = current.prev

    def append(self, value:tuple):
        if self.head.prev:
            last_node = self.head.prev
        else:
            last_node = self.head

        new_node = self.Node(value, last_node, self.head)
        self.head.prev = new_node
        last_node.next = new_node

        self.length += 1


class SnakeLinkedList(LinkedList):
    def __init__(self, fruit_position:tuple, snake_body:list):
        super().__init__(fruit_position)

        for element in snake_body:
            self.append(element)

    def set_fruit(self, position:tuple):
        self.__setitem__(0, position)

    def move_snake(self, position:tuple):
        self.__delitem__(1)
        self.append(position)

    def expand_snake(self):
        pass

