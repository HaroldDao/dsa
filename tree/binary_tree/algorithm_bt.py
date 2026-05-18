class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
r = node('R') 
y = node('Y')
t = node('T')
h = node('H')
x = node('X')
c = node('C')
v = node('V')

r.right = y
r.left = h
h.left = t
t.right = x
y.left = c
y.right = v

# root = r

def preoder(node):
    s = []
    if node is None:
        print("Empty tree!")
    else: 
        s.append(node)
        while len(s) > 0:
            p = s.pop()
            while p != None:
                print(p.data, end=" ")
                if p.right != None:
                    s.append(p.right)
                p = p.left

# inoder: Left ROOT Right
def inorder(node):
    s = []
    if node is None:
        print("Empty tree!")
        return
    else:
        p = node
        while len(s) > 0 or p != None:
            while p != None:
                s.append(p)
                p = p.left
            p = s.pop()
            print(p.data, end=" ")

            p = p.right

def postorder(node):
    s = []
    sr = []
    if node is None:
        print("Empty tree!")
    else: 
        s.append(node)
        while len(s) > 0:
            p = s.pop()
            sr.append(p.data)

            if p.left != None:
                s.append(p.left)
            if p.right != None:
                s.append(p.right)
    return sr

            

def main():
    # preoder(r)
    # inorder(r)
    print(postorder(r))

main()