import random
import curses
import time
import sys
import snake.constants as constants

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
    
    def __getitem__(self, key):
        """
        Uses 'list[key]' structure in order to get access to an item in the list

        Args:
            key (int): index number of desired place in the list
        
        Returns:
            node.value: a point in space (x,y); default to None
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
        if not current:
            return
        
        if key == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head = current.next
                self.head.prev = current.prev
                current.next = self.head

        else:
            current.next.prev = current.prev
            current.prev.next = current.next
        
        self.length -= 1


    def _find_node(self, key:int) -> Node | None:
        """Selects node found in the desired place or returns None"""
        current = self.head
        match key:
            case 0:
                pass

            case _ if (key < 0 and abs(key) < self.length):
                while (key != 0 and current != None):
                    current = current.prev
                    key += 1

            case _ if (key > 0 and abs(key) < self.length):
                while (key != 0 and current != None):
                    current = current.next
                    key -= 1

            case _:
                current = None

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
        Returns entire list in form of set

        Returns:
            set_ (set): a set of all elements from list 
        """

        set_ = set()

        for element in self:
            set_.add(element)
        
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

    def diff(self, width:int, height:int):
        """
        Returns all positions not occupied by the snake or fruit.
        Args:
            width (int): width of the board
            height (int): height of the board
        Returns:
            list (list): all positions that aren't taken
        """
        occupied = set(self)
        return [(i, j) for i in range(width) for j in range(height) if (i, j) not in occupied]

    def set_fruit(self, position:tuple):
        """
        Updates fruit position

        Args:
            position (tuple): a point in space (x,y); position of the new fruit
        """

        self.__setitem__(0, position)

    def get_fruit(self) -> tuple:
        """
        Returns fruit position

        Returns:
            position (tuple): current fruit position
        """

        return self.head.value

    def move_snake(self, direction:tuple):
        """
        Updates snake position in the list

        Args:
            direction (tuple): one of the 4 possible directions: left (-1,0); up (0,1); right (1,0); down (0,-1)
        """

        self.__delitem__(1)

        s_pos_x, s_pos_y = self.__getitem__(-1)
        self.append((s_pos_x + direction[0], s_pos_y + direction[1]))

        
    def expand_snake(self):
        """Expands current snake body in-place (doubles 'tail node' in the body)"""
        old_tail = self.head.next
        tail_value = old_tail.value
        new_node = self.Node(tail_value, prev=self.head, next=old_tail)
        self.head.next = new_node
        old_tail.prev = new_node
        self.length += 1


