import networkx as nx
import matplotlib


def build_graph(valuations):
    G = nx.DiGraph()

    people_num = len(valuations)
    house_num = len(valuations[0])

    for i in range(people_num):
        G.add_node("player "+str(i))
        G.add_node("house "+str(i))
        G.add_edge("house "+str(i), "player "+str(i))

    for player in range(people_num):
      for house in range(house_num):
        if valuations[player][house] > 0:
          G.add_edge("player "+str(player), "house "+str(house))

    return G


def is_out_edges(neighbors, comp):
  return not set(neighbors).issubset(set(comp))


def connected_to_my_house(G, node):
  my_houses = []
  for house in (G.in_edges(node)):
    my_houses.append(house[0])

  the_house_i_want = []
  for i_want in (G.out_edges(node)):
    the_house_i_want.append(i_want[1])

  if len(the_house_i_want) > 0:
    if the_house_i_want[0] in my_houses:
      return True
  return False


def contain_final_stong_component(G)->bool:
  scc = list(nx.strongly_connected_components(G))
  print("-------------------------------\nstrongly connected components: ", scc, "\n")
  for comp in scc:
    flag = True
    for node in comp:
      comp = list(comp)
      if is_out_edges(G.neighbors(node), comp) or not connected_to_my_house(G, node):
        flag = False
        break
    if flag:
      return True

  return False


if __name__ == '__main__':
    # TESTS#
    valuations1 = [[0, 1], [1, 0]]  #False
    valuations2 = [[1, 0], [1, 0]]  #True
    valuations3 = [[1, 1], [1, 0]]  #False

    G = build_graph(valuations1)
    nx.draw(G, with_labels=True)
    matplotlib.pyplot.show()
    print("contain final strong component? :", contain_final_stong_component(G))#False

    G = build_graph(valuations2)
    nx.draw(G, with_labels=True)
    matplotlib.pyplot.show()
    print("contain final strong component? :", contain_final_stong_component(G))#True


    G = build_graph(valuations3)
    nx.draw(G, with_labels=True)
    matplotlib.pyplot.show()
    print("contain final strong component? :", contain_final_stong_component(G))#False



