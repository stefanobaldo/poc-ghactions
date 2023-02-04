import os

def roar():
    print("Roaaaarrr!")
    if (os.environ['HOME'] == "something"):
        print("Meooooww!")
    print("More")
    return 0
