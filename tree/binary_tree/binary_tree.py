class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def root(self):
        self.next = None
        
def pre_order(n):
    if n != None:
        print(n.data, end=" ")
        pre_order(n.left)
        pre_order(n.right)    

r = node('a')
a = node('y')
b = node('t')
d = node('h')
w = node('x')
g = node('c')
s = node('v')


r.right = d
r.left = a
a.left = b
b.right = w
d.left = g
d.right = s

root = r

def main():
    # pre_order(root)
    print(root)
    print(a)
    print(r)

main()