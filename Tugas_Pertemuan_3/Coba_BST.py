def Create_node(key):
    return {"current key" : key, "left child" : None, "right child" : None}


def Insert(root, node):
    if not root:  # Creating a root
        root = node
    elif node["current key"] <= root["current key"]:  # I use "<=" for dupes
        if not root["left child"]:
            root["left child"] = node
        else:
            return Insert(node["left child"], node)
    else:
        if not root["right child"]:
            root["right child"] = node
        else:
            return Insert(node["right child"], node)


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
    if value < root["current key"]:
        root["left child"] = Remove(root["left child"], value)
    elif value > root["current key"]:
        root["right child"] = Remove(root["right child"], value)
    else:
        if root["left child"] == None and root["right child"] == None:  # No child, simply remove the node
            root = None
        elif root["left child"] == None:  # Replace the node with the child
            root = root["right child"]
        elif root["right child"] == None:
            root = root["left child"]
        else:  # If 2 child
            temp = Find_min(root["right child"])  # Find the smallest on the right
            root["current key"] = temp["current key"]  # Replace the value
            root["right child"] = Remove(root["right child", temp["current key"]])  # Delete the old smallest right
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



#keys = list(map(int, input().split()))  # Useless without the command loop
keys = [5, 34, 12, 7, 5, 18]

Akar = None
for i in keys:
    if Akar == None:
        Akar = Create_node(i)
    else:
        Titik = Create_node(i)
        Insert(Akar, Titik)

"""
if keys:
    while True:
        inpt = input()  # The orders won't work due to input() being a blocking operation, sad :(
        if inpt == "stop":
            break
        elif inpt == "find":
            f_value = int(input())
            print(Find(Akar, f_value))
        elif inpt == "find min":
            Find_min(Akar)["current key"]
        elif inpt == "find max":
            Find_max(Akar)["current key"]
        elif inpt == "insert":
            ins_node = int(input())
            Insert(Akar, ins_node)
        elif inpt == "remove":
            rmv_value = int(input())
            Remove(Akar, rmv_value)
        elif inpt == "postorder":
            Postorder(Akar)
        elif inpt == "preorder":
            Preorder(Akar)
        elif inpt == "inorder":
            In_order(Akar)
        elif inpt == "level order":
            Level_order(Akar)
"""

Postorder(Akar)
Preorder(Akar)
In_order(Akar)
Level_order(Akar)
print(Find(Akar, 12))
Remove(Akar, 34)
Preorder(Akar)
print(Find(Akar, 34))
Find_min(Akar["left child"])
Find_max(Akar["right child"])