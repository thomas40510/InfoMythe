import visugraphe


class Graph:
    def __init__(self):
        self.nodes = []
        self.links = []

    def add_node(self, n, c=0, x=0, y=0):
        """
        adds a node to the graph
        :param n: name of node
        :param c: color of node
        :param x: x-coordinate of node
        :param y: y-coordinate of node
        :return: n
        """
        node = Node(n, c, x, y)
        self.nodes.append(node)
        return node

    def add_link(self, n1, n2):
        """
        Adds link to a graph
        :param n1: name of node 1
        :param n2: name of node 2
        :return:
        """
        n1.newlink(n2)
        n2.newlink(n1)
        if [n1, n2] not in self.links:
            self.links.append([n1, n2])

    def find_node(self, s):
        """
        finds node of name s in graph
        :param s: name of node to find
        :return:
        """
        for n in self.nodes:
            if n.name == s:
                return n
        return None

    def welsh_powell(self):
        """
        colors nodes of graph so any node has a different color from its neighbors
        :return:
        """
        lst = []
        for e in self.nodes:
            lst.append([e.name, len(e.neighbors), e])
        for i in range(1, len(lst)):
            l = lst[i]
            k = lst[i][1]
            j = i - 1
            while j >= 0 and k < lst[j][1]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = l
        n = 0
        while len(lst) > 0:
            self.nodes[self.nodes.index(lst[0][2])].color = n
            n += 1
            lst.pop(0)

    def click(self, n: int):
        """
        creates graph of n nodes linked to all others
        :param n: number of nodes
        :return:
        """
        for i in range(n):
            self.add_node(n)
        for j in range(n):
            for k in range(n):
                self.add_link(self.nodes[j], self.nodes[k])

    def biparti(self, n: int, p: int, colored=False):
        """
        creates a graph of n+p nodes linking each of n nodes to all of p nodes
        :param n: number of n nodes
        :param p: number of p nodes
        :param colored: defines if n and p nodes are colored differently
        :return:
        """
        for i in range(n + p):
            if colored:
                self.add_node(i, c=0 if i <= n else 1)
            else:
                self.add_node(i)
        for j in range(n):
            for k in range(p):
                self.add_link(self.nodes[j], self.nodes[n + k])

    def cycle(self, n: int):
        """
        creates a cycle graph of n nodes
        :param n: number of nodes
        :return:
        """
        for i in range(n):
            self.add_node(i)
        for j in range(len(self.nodes) - 1):
            self.add_link(self.nodes[j], self.nodes[j + 1])
        self.add_link(self.nodes[0], self.nodes[-1])

    def pathos(self):
        """
        creates a graph "pathos"
        :return:
        """
        alpha = "ABCDEFGH"
        for i in range(8):
            self.add_node(alpha[i])
        L = [0, 2, 3, 4, 6, 7]
        for j in range(len(L) - 1):
            self.add_link(self.nodes[L[j]], self.nodes[L[j + 1]])
        self.add_link(self.nodes[0], self.nodes[1])
        self.add_link(self.nodes[4], self.nodes[5])


class Node:
    def __init__(self, n, c=0, x=0.0, y=0.0):
        self.name = n
        self.neighbors = []
        self.color = c
        self.x = x
        self.y = y

    def newlink(self, n):
        """
        Create link to node n
        :param n: name of linked node
        :return:
        """
        if n not in self.neighbors:
            self.neighbors.append(n)
        return True


if __name__ == '__main__':
    # g = Graph()
    # nA = g.add_node("A")
    # nB = g.add_node("B")
    # nC = g.add_node("C")
    # nD = g.add_node("D")
    # nE = g.add_node("E")
    # g.add_link(nA, nB)
    # g.add_link(nA, nE)
    # g.add_link(nB, nC)
    # g.add_link(nB, nD)
    # g.add_link(nB, nE)
    # g.add_link(nC, nD)
    # g.add_link(nC, nE)
    # g.add_link(nD, nE)
    # # visugraphe.visu_graphe_simple(g)
    # g.welsh_powell()
    # visugraphe.visu_graphe_color(g)
    #
    # h = Graph()
    # # h.biparti(5, 4, colored=True)
    # # h.click(5)
    # h.pathos()
    # visugraphe.visu_graphe_color(h)

    f = open("files/dept.txt")
    s = f.read()
    f.close()
    L = s.split("\n")
    L = [e.split(" ") for e in L]
    size = int(L[0][0])
    L.pop(0)
    L1 = L[:size]
    L2 = L[size+1:]

    france = Graph()
    nds = []
    for dep in L1:
        n = france.add_node(int(dep[0]), x=float(dep[1]), y=float(dep[2]))
        nds.append(n)

    for dep in L2:
        try:
            tmp = int(dep[0])
            print(dep[0])
            nd = france.find_node(tmp)
            for v in dep[1:]:
                france.add_link(nd, france.find_node(int(v)))
        except Exception as e:
            print(e)
    # france.welsh_powell()
    visugraphe.visu_graphe_coord(france)


