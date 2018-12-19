class Mylist(list):

    def __init__(self, *args):
        super(Mylist, self).__init__(*args)
        self.append("----------------")


myl = Mylist(range(3, 6))
myl.append(6)
print(myl)
