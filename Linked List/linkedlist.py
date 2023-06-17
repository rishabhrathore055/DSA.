class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    
    def listLength(self):
        current = self.data
        count = 0
        while current!=None:
            count +=1
            current = current.getNext()
        return count

c1 = Node()
c1.setData(10)
c1.setData(20)
print(c1.listLength())