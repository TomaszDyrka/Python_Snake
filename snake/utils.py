import random

class Linked_List:
    class Node:
        def __init__(self, value:tuple, prev:"Linked_List.Node" = None, next:"Linked_List.Node" = None):
            """
            Initialize new node

            Args:
                value (tuple): a point in space (x,y)
                prev (Linked_List.Node): node linked backwards, default to None
                next (Linked_List.Node): node linked forward, default to None
            """
            self.value = value
            self.prev = prev
            self.next = next


    class Linked_List_Iterator:
        def __init__(self, head_node:"Linked_List.Node", length:int):
            """Linked_List iterator"""
            self.node = head_node
            self.num = 0
            self.end_num = length 

        def __iter__(self):
            """__iter__ returns the iterator itself"""
            return self
        
        def __next__(self):
            """__next__ returns value (tuple) of current node"""
            if self.num < self.end_num:
                value = self.node.value
                self.node = self.node.next
                self.num += 1

                return value
            
            else:
                raise StopIteration


    def __init__(self, value:tuple):
        """
        Initialize new class instance

        Args:
            value (tuple): a point in space (x,y)
        """

        self.head = self.Node(value)
        self.length = 1

    def __len__(self):
        """Returns length of list"""

        return self.length
    
    def __iter__(self):
        """Iterator method"""

        return self.Linked_List_Iterator(self.head, self.length)
    
    def __getitem__(self, key:int):
        """
        Uses 'list[key]' structure in order to get access to an item in the list

        Args:
            key (int): index number of desired place in the list
        
        Returns:
            current: a point in space (x,y); default to None
        """

        node = self._find_node(key)

        return node.value

    def __setitem__(self, key:int, value:tuple):
        """
        Uses 'list[key] = value' structure in order to set item's value in the list

        Args:
            key (int): index number of desired place in the list
            value (tuple): a point (x,y) to replace previous one
        """

        node = self._find_node(key)

        if node:
            node.value = value

    def __delitem__(self, key:int):
        """
        Uses 'del list[key]' structure to delete a value in the list

        Args:
            key (int): index number of desired place in the list
        """

        current = self._find_node(key)
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

    def _find_node(self, key:int):
        """Selects node found in the desired place or returns None"""
        match key:
            case 0:
                current = self.head

            case _ if (key < 0 and abs(key) < self.length):
                current = self.head

                while (key != 0 and current != None):
                    current = current.prev
                    key += 1

            case _ if (key > 0 and abs(key) < self.length):
                current = self.head

                while (key != 0 and current != None):
                    current = current.prev
                    key -= 1

            case _:
                return None

        return current
        
    def append(self, value:tuple):
        """
        Appends given value to the end of the list

        Args:
            value (tuple): a point in space (x,y)
        """

        if self.head.prev:
            last_node = self.head.prev
        else:
            last_node = self.head

        new_node = self.Node(value, last_node, self.head)
        self.head.prev = new_node
        last_node.next = new_node

        self.length += 1

    def to_set(self):
        """
        Returns all list in form of set

        Returns:
            set: a set of all elements from list 
        """

        set_ = set([self.head.value])
        head = self.head

        while head.next is not self.head:
            head = head.next
            set_.add(head.value)
        
        return set_
    

class SnakeLinked_List(Linked_List):
    def __init__(self, fruit_position:tuple, snake_body:list):
        """
        Initializes a new class instance

        Args:
            fruit_position (tuple): a point in space (x,y)
            snake_body (list): list of points of the initial snake body position
        """

        super().__init__(fruit_position)

        for element in snake_body:
            self.append(element)

    def set_fruit(self, position:tuple):
        """
        Updates fruit position

        Args:
            position (tuple): a point in space (x,y); position of the new fruit
        """

        self.__setitem__(0, position)

    def move_snake(self, position:tuple):
        """
        Updates snake position in the list

        Args:
            position (tuple): a point in space (x,y); new snake head position
        """

        self.__delitem__(1)
        self.append(position)

    def diff(self, width:int, height:int):
        """
        Produces list - difference between positions free and taken, without maintaining order of positions

        Args:
            width (int): width of the board
            height (int): height of the board

        Returns:
            list (list): all positions that aren't taken
        """

        list_ = [(i,j) for i in range(width) for j in range(height)]
        
        for element in self:
            position = element[0] * width + element[1]
            list_[position] = list_[-1]
            list_.pop()

        return list_

    def expand_snake(self):
        pass

