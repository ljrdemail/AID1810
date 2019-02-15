class Mylist(list):
    def insert_head(self, n):
        # self[0:0]=[n]
        self.insert(0, n)


myl = Mylist(range(3, 6))
print(myl)
myl.insert_head(2)
print(myl)
