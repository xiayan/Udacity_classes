# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#
def create_rooted_spanning_tree(G, root):
    S = {}
    open_list = [root]
    marked = [root]
    while len(open_list) > 0:
        current = open_list[0]
        if current not in S:
            S[current] = {}
        del open_list[0]
        for neighbor in G[current]:
            if neighbor not in marked:
                open_list.append(neighbor)
                marked.append(neighbor)
                S[current][neighbor] = 'green'
            else:
                if neighbor not in S:
                    S[current][neighbor] = 'red'
                elif current in S[neighbor]:
                    S[current][neighbor] = S[neighbor][current]
                else:
                    S[current][neighbor] = 'red'
    return S

# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'}
                 }
###########

def post_order(S, root):
    open_list = [root]
    rank = []
    order = 1
    po = {}
    while len(open_list) > 0:
        current = open_list.pop()
        rank.append(current)
        children = [neighbor for neighbor, color in S[current].items()
                             if color == 'green'
                             if neighbor not in rank]
        if len(children) == 0:
            po[current] = order
            order += 1
        else:
            open_list += children

    for i in range(len(rank)-1, -1, -1):
        if rank[i] in po:
            continue
        else:
            po[rank[i]] = order
            order += 1

    return po

# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
    print "good"

##############
import operator

def number_of_descendants(S, root):
    po = post_order(S, root)
    nd = {}
    sorted_po = [a for a,b in sorted(po.iteritems(), key=operator.itemgetter(1))]
    for node in sorted_po:
        children = [neighbor for neighbor, color in S[node].items() if color == 'green' if po[neighbor] < po[node]]
        if len(children) == 0:
            nd[node] = 1
        else:
            nd[node] = sum([nd[child] for child in children]) + 1
    return nd

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'},
          'b': {'a': 'green', 'd': 'red'},
          'c': {'a': 'green', 'd': 'green'},
          'd': {'c': 'green', 'b': 'red', 'e': 'green'},
          'e': {'d': 'green', 'g': 'green', 'f': 'green'},
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'}
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    l = {}
    sorted_po = [a for a,b in sorted(po.iteritems(), key=operator.itemgetter(1))]
    for node in sorted_po:
        children = [neighbor for neighbor, color in S[node].items() if (color == 'green' and po[neighbor] < po[node]) or color == 'red']
        if len(children) == 0:
            l[node] = po[node]
        else:
            numbers = []
            for child in children:
                if child in l:
                    numbers.append(l[child])
                else:
                    numbers.append(po[child])
            numbers.append(po[node])
            l[node] = min(numbers)
    return l

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}
    print "good"

################

def highest_post_order(S, root, po):
    h = {}
    sorted_po = [a for a,b in sorted(po.iteritems(), key=operator.itemgetter(1))]
    for node in sorted_po:
        children = [neighbor for neighbor, color in S[node].items() if (color == 'green' and po[neighbor] < po[node]) or color == 'red']
        if len(children) == 0:
            h[node] = po[node]
        else:
            numbers = []
            for child in children:
                if child in h:
                    numbers.append(h[child])
                numbers.append(po[child])
            numbers.append(po[node])
            h[node] = max(numbers)

    return h

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    print h
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    print 'high good'

test_highest_post_order()
#################

def bridge_edges(G, root):
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    l = lowest_post_order(S, root, po)
    h = highest_post_order(S, root, po)
    result = []
    for node in G.keys()[1:]:
        if h[node] <= po[node] and l[node] > (po[node] - nd[node]):
            tail = node
            for neighbor in S[tail]:
                if po[neighbor] > po[tail] and S[tail][neighbor] == 'green':
                    head = neighbor
                    result.append((head, tail))
    print S
    print po
    print nd
    print l
    print h
    return result

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(G, 'a')
    print bridges
    assert bridges == [('d', 'e')]
    print 'good'

test_bridge_edges()