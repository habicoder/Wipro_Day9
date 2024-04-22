import os 
directory = "Geeks"
parent = "D:/Pycharm projects/"
path = os.path.join(parent, directory) 
os.rmdir(path)