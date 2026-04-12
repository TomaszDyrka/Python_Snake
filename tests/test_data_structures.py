from src.snake.utils import *
import pytest


class Test_Linked_List:
    def test_node_creation_and_coupling(self):
        # if with proper attributes
        node_0 = Linked_List.Node((0,0))
        assert hasattr(node_0, 'value')
        assert hasattr(node_0, 'prev')
        assert hasattr(node_0, 'next')

        # different values
        node_1 = Linked_List.Node((1,2))
        node_2 = Linked_List.Node((-1,2))
        node_3 = Linked_List.Node((-1,-2))
        node_4 = Linked_List.Node((1,-2))

        assert node_0.value == (0,0)
        assert node_1.value == (1,2)
        assert node_2.value == (-1,2)
        assert node_3.value == (-1,-2)
        assert node_4.value == (1,-2)

        # coupling with prev and next
        node_1.next = node_2
        assert node_1.next == node_2
        assert node_1.prev == None
        assert node_2.next == None
        assert node_2.prev == None

        node_3.prev = node_4
        assert node_3.prev == node_4
        assert node_3.next == None
        assert node_4.prev == None
        assert node_4.next == None

        node_2.next = node_3
        node_3.prev = node_2

        assert node_2.next == node_3
        assert node_3.prev == node_2

    def test_ll_creating_appending_setting(self):
        ll = Linked_List((0,0))
        ll.append((3,4))

        assert ll[0] == (0,0)
        assert ll[1] == (3,4)
        assert ll[-1] == (3,4)

        ll[0] = (10,10)
        assert ll[0] == (10,10)

    def test_ll_finding_node(self):
        ll = Linked_List((0,0))
        for i in range(1, 10):
            ll.append((i, -i))


        assert ll._find_node(3).value == (3, -3)
        assert ll._find_node(-2).value == (8, -8)
        assert ll._find_node(9) is not None
        assert ll._find_node(-10) is not None
        assert ll._find_node(10) is None
        assert ll._find_node(-11) is None

    def test_ll_iterating_deleting(self):
        ll = Linked_List((0,0))
        for i in range(1, 10):
            ll.append((i, -i))

        i = 0
        for value in ll:
            assert value == (i, -i)
            i += 1

        temp = ll[2]
        del ll[2]

        assert temp not in ll

    def test_ll_exporting_to_set(self):
        ll = Linked_List((0,0))
        for i in range(1, 10):
            ll.append((i, -i))

        temp_set = ll.to_set()

        assert len(temp_set) == len(ll)
        for value in ll:
            assert value in temp_set
            temp_set.remove(value)

        assert not temp_set


class Test_Snake_Linked_List:
    # A little different apporach: using fixtures and blocking tests
    # in order to e.g. ensure no data logic will be created in class

    @pytest.fixture
    def initial_fruit(self):
        return (5, 5)
    @pytest.fixture
    def alt_initial_fruit(self):
        return (-5, -5)


    @pytest.fixture
    def initial_body(self):
        return [(1, 1), (1, 2), (1, 3)]
    @pytest.fixture
    def alt_initial_body(self):
        return [(-1, 1), (-1, 2), (-1, 3)]


    @pytest.fixture
    def snake(self, initial_fruit, initial_body):
        return Snake_Linked_List(initial_fruit, initial_body)
    @pytest.fixture
    def alt_snake(self, alt_initial_fruit, alt_initial_body):
        return Snake_Linked_List(alt_initial_fruit, alt_initial_body)


    def test_creation(self, snake, initial_fruit, alt_snake, alt_initial_fruit):
        assert snake.get_fruit() == initial_fruit
        assert snake[-1] == (1, 3)

        assert alt_snake.get_fruit() == alt_initial_fruit
        assert alt_snake[-1] == (-1, 3)

    def test_set_and_get_fruit(self, snake, alt_snake, initial_fruit, alt_initial_fruit):
        assert snake.get_fruit() == (5, 5)
        assert alt_snake.get_fruit() == (-5, -5)

        snake.set_fruit(alt_initial_fruit)
        alt_snake.set_fruit(initial_fruit)
        
        assert snake.get_fruit() == alt_initial_fruit
        assert alt_snake.get_fruit() == initial_fruit

    def test_diff(self, snake, alt_snake):
        width, height = 3, 3
        free_spaces = snake.diff(width, height)
        alt_free_spaces = alt_snake.diff(width, height) 
        
        assert len(free_spaces) == 7
        assert (0, 0) in free_spaces
        assert (1, 1) not in free_spaces
        assert (1, 2) not in free_spaces

        assert len(alt_free_spaces) == 9
        assert (-1, 1) not in alt_free_spaces
        assert (-1, 2) not in alt_free_spaces
        assert (-1, 3) not in alt_free_spaces

    def test_move_snake(self, snake, alt_snake):
        old_head = snake[-1]  
        alt_old_head = alt_snake[-1]
        direction = (0, 1)    
        alt_direction = (-1, 0) 

        snake.move_snake(direction)
        alt_snake.move_snake(alt_direction)
        
        new_head = snake[-1]
        alt_new_head = alt_snake[-1]

        assert new_head == (old_head[0] + direction[0], old_head[1] + direction[1])
        assert alt_new_head == (alt_old_head[0] + alt_direction[0], alt_old_head[1] + alt_direction[1])
        assert (1, 1) not in set(snake)
        assert (-1, 1) not in set(alt_snake)

    def test_expand_snake(self, snake, alt_snake):
        old_length = snake.length
        old_tail_value = snake.head.next.value
        
        snake.expand_snake()
        
        assert snake.length == old_length + 1
        assert snake.head.next.value == old_tail_value
        assert snake.head.next.next.value == old_tail_value


def test_reverse_func():
    assert is_reverse( (1,0), (-1,0) ) 
    assert is_reverse( (0,1), (0,-1) ) 

    assert not is_reverse( (1,0), (0,-1) ) 
    assert not is_reverse( (0,-1), (1,0) ) 
