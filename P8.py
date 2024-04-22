import os
directory = "doss"
parent_dir = "D:/wipropy/"
path = os.path.join(parent_dir, directory)
 
os.mkdir(path)
print("Directory '% s' created" % directory)