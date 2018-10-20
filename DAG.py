from copy import copy, deepcopy
from collections import deque

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

# Directed acyclic graph implementation
class DAG(object):

    def reset_graph(self):
        # Restore graph to an empty state
        self.graph = OrderedDict()

    def __init__(self):
        # Construct a new DAG with no nodes or edges
        self.reset_graph()

    def add_node(self, node_name, graph=None):
        # Add node if it doesn't exist yet
        if not graph:
            graph = self.graph
        if node_name in graph:
            raise KeyError('node %s already exists' % node_name)
        graph[node_name] = set()

    def add_node_if_not_exists(self, node_name, graph=None):
        try:
            self.add_node(node_name, graph=graph)
        except KeyError:
            pass

# delete node
# add edge
# VERTICES ??

    def downstream(self, node, graph=None):
        #Returns a list of all nodes this node has edges towards.
        if graph is None:
            graph = self.graph
        if node not in graph:
            raise KeyError('node %s is not in graph' % node)
        return list(graph[node])

    def all_downstreams(self, node, graph=None):
        #Returns a list of all nodes ultimately downstream
        #of the given node in the dependency graph, in
        #topological order.
        if graph is None:
            graph = self.graph
        nodes = [node]
        nodes_seen = set()
        i = 0
        while i < len(nodes):
            downstreams = self.downstream(nodes[i], graph)
            for downstream_node in downstreams:
                if downstream_node not in nodes_seen:
                    nodes_seen.add(downstream_node)
                    nodes.append(downstream_node)
            i += 1
        return list(
            filter(
                lambda node: node in nodes_seen,
                self.__topological_sort(graph=graph)
            )
        )

    def delete_edge(self, ind_node, dep_node, graph=None):
        #Delete an edge from the graph.
        if not graph:
            graph = self.graph
        if dep_node not in graph.get(ind_node, []):
            raise KeyError('this edge does not exist in graph')
        graph[ind_node].remove(dep_node)

    def predecessors(self, node, graph=None):
        #Returns a list of all predecessors of the given node
        if graph is None:
            graph = self.graph
        return [key for key in graph if node in graph[key]]

    def size(self):
        return len(self.graph)
