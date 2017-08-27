class Node:

    def __init__(self):
        self.N = []
        self.PE = 0
        self.PS = 0
        self.pai = None

    def add_neighbor(self, n):
        self.N.append(n)

class DFS:

    def __init__(self):
        self.t = 0
        self.blue = []
        self.red = []

    def P(self, v):
        self.t += 1
        v.PE = t
        for w in v.N:
            if w.PE == 0:
                self.blue.append((v, w))
                w.pai = v
                self.P(w)
            else if w.PS == 0 and w != v.pai:
                # cycle
                self.red.append((v, w))
        t += 1
        v.PS = t