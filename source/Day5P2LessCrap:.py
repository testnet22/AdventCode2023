def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data