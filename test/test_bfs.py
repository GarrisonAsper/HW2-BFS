# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    test_path = 'data/tiny_network.adjlist'
    test_graph = Graph(test_path)

    test_bfs= test_graph.bfs('Martin Kampmann')

    assert len(test_path) == len(test_graph.graph.nodes)

    correct_path = ['Martin Kampmann','33483487','32790644','31806696','31626775','31540829','Luke Gilbert','Steven Altschuler','Lani Wu','Neil Risch',
                    'Nevan Krogan','32036252','32042149','30727954','29700475','34272374','32353859','30944313','Hani Goodarzi','Michael McManus',
                    'Michael Keiser','Atul Butte','Marina Sirota','33232663','32025019','33765435','33242416','31395880','31486345','Charles Chiu']
    
    assert test_bfs == correct_path
    
    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    long_test_path = 'data/citation_network.adjlist'

    long_graph = Graph(long_test_path)

    none_path = long_graph.bfs('34407489', '34405267')

    assert none_path == None

    correct_shortest_path = ['30814728','Lani Wu','30727954','Michael McManus','29700475','Brian Shoichet']
    test_shortest_path = long_graph.bfs('30814728', 'Brian Shoichet')

    assert correct_shortest_path == test_shortest_path
    
    pass
