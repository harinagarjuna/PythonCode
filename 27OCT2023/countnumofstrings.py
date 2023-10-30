names = ["HariH","Ravi","Suresh","H","E","L","O"]
ln = len(names)
count =0
for n in names:
    if len(n) >=2 and n[0] == n[len(n)-1]:
        count+=1
print(count)

