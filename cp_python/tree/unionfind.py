## unionfind library
## verify: ATC001B, ABC075C
## ref: https://qiita.com/Kerzival/items/6923c2eb3b91be86f19f
## ref: https://pyteyon.hatenablog.com/entry/2019/03/11/200000

## begin library unionfind
## usage: uf = UnionFind()
## usage: r = uf.Find_Root(x)
## usage: uf.Unite(x, y)
## usage: bool = uf.isSameGroup(x, y)
## usage: n = uf.Count(x)
class UnionFind():

    def __init__(self, n):
        self.n = n # number of nodes
        # if root[x]<0 then x is root and it has |x| leafs
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # find root of node x
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # path compression
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    # unite two trees which has node x and node y
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # same tree
        if(x == y):
            return
        # different tree
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # if same rank (same depth)
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # return number of leafs
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

## end library unionfind

