class SuperList(list):
    def __len__(self):
        return 100


li = SuperList()
li.append(10)
li.append(20)
print(li)
print(len(li))
