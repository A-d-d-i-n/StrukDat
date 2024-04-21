def Create_node(key):
    return {"current key" : key, "left child" : None, "right child" : None}


def Insert(root, node):
    if not root:
        root = node
    if Find(node):
        return print("Duplicate Value!")
    elif node["current key"] < root["current key"]:
        if not root["left child"]:
            root["left child"] = node
        else:
            return Insert(node["left child"], node)
    elif node["current key"] > root["current key"]:
        if not root["right child"]:
            root["right child"] = node
        else:
            return Insert(node["right child"], node)
    else: 
        return print("Duplicate Value!")


def Search(root, value):
    while root:
        if value > root["current key"]:
            return Search(root["right child"], value)
        elif value < root["current key"]:
            return Search(root["left child"], value)
        else:
            return root
    return None


def Find(root, value):
    temp = Search(root, value)
    if temp == None:
        return False
    if temp["current key"] == value:
        return True
    else:
        return False


def Find_min(root, node):
    if not node:
        node = root
    if not root:
        return node
    if root["current key"] < node["current key"]:
        node = root
    return Find_min(root["left child"], node)


def Find_max(root, node):
    if not node:
        node = root
    if not root:
        return node
    if root["current key"] > node["current key"]:
        node = root
    return Find_min(root["right child"], node)


def Remove(root, value):        
    if root == None:
        return root
    if not Find(value):
        return print("Cannot Find the Value!")
    elif value < root["current key"]:
        root["left child"] = Remove(root["left child"], value)
    elif value > root["current key"]:
        root["right child"] = Remove(root["right child"], value)
    else:
        if root["left child"] == None and root["right child"] == None:
            root = None
        elif root["left child"] == None:
            root = root["right child"]
        elif root["right child"] == None:
            root = root["left child"]
        else:
            temp = Find_min(root["right child"])
            root["current key"] = temp["current key"]
            root["right child"] = Remove(root["right child", temp["current key"]])
    return root



def In_order(root):
    if root is None:
        return 
    In_order(root["left child"])
    print(root["current key"])
    In_order(root["right child"])


def Preorder(root):
    if root is None:
        return
    print(root["current key"])
    Preorder(root["left child"])
    Preorder(root["right child"])


def Postorder(root):
    if root is None:
        return
    Postorder(root["left child"])
    Postorder(root["right child"])
    print(root["current key"])


def Level_order(root):
    if root is None:
        return
    Queue = [root]
    node = Queue.pop(0)
    print(node["current key"], end = " ")
    if node["left child"]:
        Queue.append(node["left child"])
    if node["right child"]:
        Queue.append(node["right child"])


in_range = []
def Range_Sum(root, lo, hi):
    jangkauan = range(lo, hi+1)
    if root is None:
        return 
    Range_Sum(root["left child"], lo, hi)
    if root["current key"] in jangkauan:
        in_range.append(root["current key"])
    Range_Sum(root["right child"], lo, hi)



n = int(input())
inpt = list(map(int, input().split()))
low, high = map(int, input().split())

akar = None
for node in inpt:
    if akar == None:
        akar = Create_node(node)
    else:
        titik = Create_node(node)
        Insert(akar, titik)

if low > high:
    temp = low
    low = high
    high = temp
if low == high:
    high = low + 1


Range_Sum(akar, low, high)

total = 0
for i in in_range:
    total = total + i
print(total)