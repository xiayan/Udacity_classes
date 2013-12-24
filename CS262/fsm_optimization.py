# Title: FSM Optimization
#
# Challenge Problem: 2 Stars
#
# Lexical analyzers are implemented using finite state machines generated
# from the regular expressions of token definition rules. The performance
# of a lexical analyzer can depend on the size of the resulting finite
# state machine. If the finite state machine will be used over and over
# again (e.g., to analyze every token on every web page you visit!), we
# would like it to be as small as possible (e.g., so that your webpages
# load quickly). However, correctness is more important than speed: even
# an optimized FSM must always produce the right answer.
#
# One way to improve the performance of a finite state machine is to make
# it smaller by removing unreachable states. If such states are removed,
# the resulting FSM takes up less memory, which may make it load faster or
# fit better in a storage-constrained mobile device.
#
# For this assignment, you will write a procedure nfsmtrim that removes
# "dead" states from a non-deterministic finite state machine. A state is
# (transitively) "dead" if it is non-accepting and only non-accepting
# states are reachable from it. Such states are also called "trap" states:
# once entered, there is no escape. In this example FSM for r"a*" ...
#
# edges = { (1,'a') : [1] ,
#           (1,'b') : [2] ,
#           (2,'b') : [3] ,
#           (3,'b') : [4] }
# accepting = [ 1 ]
#
# ... states 2, 3 and 4 are "dead": although you can transition from 1->2,
# 2->3 and 3->4 on "b", you are doomed to rejection if you do so.
#
# You may assume that the starting state is always state 1. Your procedure
# nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting)
# corresponding to a FSM that accepts exactly the same strings as the input
# FSM but that has all dead states removed.
#
# Hint 1: This problem is tricky. Do not get discouraged.
#
# Hint 2: Think back to the nfsmaccepts() procedure from the "Reading
# Machine Minds" homework problem in Unit 1. You are welcome to reuse your
# code (or the solution we went over) to that problem.
#
# Hint 3: Gather up all of the states in the input machine. Filter down
# to just those states that are "live". new_edges will then be just like
# edges, but including only those transitions that involve live states.
# new_accepting will be just like accepting, but including only those live
# states.

def nfsmtrim(edges, accepting):
  #in_graph = set([s for (s, i) in edges])
  start = next((s, i) for (s, i) in edges if s == 1)
  visited = []
  path, paths, new_accepting = [start],[], []
  find_all_path(start, visited, edges, accepting, path, paths, new_accepting)
  new_accepting = list(set(new_accepting))
  the_set = set()
  for the_path in paths:
    for node in the_path:
      the_set.add(node)

  the_list = list(the_set)
  node_list = list(set(node for node, i in the_list))

  new_edges = generate_new(edges, new_accepting, the_list, node_list)
  return new_edges, new_accepting


def find_all_path(node, visited, edges, accepting, path, paths, new_accepting):
  for outlet in edges[node]:
    if outlet in accepting:
      new_accepting.append(outlet)
      paths.append(path)
    for new in edges:
      if new[0] == outlet and new not in visited:
        visited.append(new)
        new_path = path + [new]
        find_all_path(new, visited, edges, accepting, new_path, paths, new_accepting)

def generate_new(edges, accepting, the_list, node_list):
  new_edges = {}
  for key, value in edges.items():
    if (key in the_list): #or key[0] in accepting:
      new_value = []
      for old in value:
        if old in node_list or old in accepting:
          new_value.append(old)
      new_edges[key] = new_value

  return new_edges


edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , }
accepting1 = [ 1 ]
(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1)
print new_edges1
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1]

(new_edges2, new_accepting2) = nfsmtrim(edges1,[])
print new_edges2 == {}
print new_accepting2 == []

(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6])
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]

edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] }
accepting4 = [ 2 ]
(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4)
print new_edges4 == {
  (1, 'a'): [1],
  (1, 'b'): [2],
  (2, 'b'): [3],
  (3, 'c'): [2, 1],
}
print new_accepting4 == [2]