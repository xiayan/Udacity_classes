def find_eulerian_tour(graph):
        tour=[]
        find_tour(1,graph,tour)
        return tour
def find_tour(u,E,tour):
    for (a,b) in E:
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    tour.insert(0,u)

def test():
    graph1 = [(1, 2), (1, 3), (1, 5),(4, 3),(4, 2),(4, 5)]
    graph2 = [(1,2),(1,3),(2,3)]
    graph3 = [(1,2),(1,3),(1,5),(1,6),(4,2),(4,3),(4,5),(4,6)]
    graph4 = [(1,2),(1,3),(1,5),(3,5),(2,5),((3,4),(2,4))]
    graph5 =  [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    test_set = [graph1, graph2, graph3, graph4,graph5]
    #test_set =[graph5]
    for test in test_set:
        print find_eulerian_tour(test)

test()