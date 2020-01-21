import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
f1 = set()
f2 = set()
with open(file1,"r") as f:
    for i in f:
        i = i.strip()
        f1.add(i)
        
with open(file2, "r") as f:
    for i in f:
        i = i.strip()
        f2.add(i)
        
intersec = sorted(f1.intersection(f2))
for i in range(0, len(intersec)):
    print(str(i + 1)+ ". " + str(intersec[i]))