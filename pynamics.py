import networkx as nx

class BondGraph(nx.MultiDiGraph):
  def __init__(self, *args, **kwargs):
    super(BondGraph, self).__init__(*args, **kwargs)
  def __add__(self, rhs):
    # add connections from node
    pass
