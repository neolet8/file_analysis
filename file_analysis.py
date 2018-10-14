import os
import os.path


path= r"C:\\Users\\..."  

fileSet = os.listdir(path)
sorteda = sorted(fileSet,key=lambda x: int(os.path.splitext(x)[0]))

img=list(range(1,5))

a = [os.path.splitext(x)[0] for x in fileSet]


sorteda = sorted(a,key=lambda x: int(os.path.splitext(x)[0]))
results = list(map(int, sorteda))


klm=list(set(img) - set(results))


print(sorted(klm))
print(len(sorted(klm)))



