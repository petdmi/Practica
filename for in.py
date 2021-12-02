

l = [0,1,2,3,4,5]
t = (0,1,2,3,4,5,6,7,8,9,10)

s = {0,1,2,3,4,5,6}
d = {0:"-",1:"a",2:"b",3:"c",4:"d",5:"e"}

# collection = l
# for element in collection:
#     print(element)

for element in "!".join(map(,l)):
    print(element)
#####################################################
##Перебираем длину списка
# cnt = 0
# size = len(l)

# while cnt < size:
#     print(l[cnt])
#     cnt+=1
#####################################################
##Перебираем длину кортежа
# cnt = 0
# size = len(t)
#
# while cnt < size:
#     print(t[cnt])
#     cnt+=1
#####################################################
##Перебираем длину множества
# cnt = 0
# size = len(s)
# #
# while cnt < size:
#     print(s.pop())
#     cnt+=1

#####################################################
##Перебираем длину словаря
# cnt = 0
# size = len(d)
#
# keys_d = list(d.keys())
# while cnt < size:
#     print(keys_d[cnt])
#     cnt+=1

#####################################################
##Testing GIT - commit, push, pull, etc

print('Testing Git 3 time')
print('Testing Commit and Push')
print("Checkout From Merge to feature/TEST-1")
#git branch - проверить на какой ветке мы находимся в данный момент
#git checkout -b feature/TEST-1 - мы перенсли с ветки main на ветку feature/TEST-1
#git push
#git commit


##################################################
#git Log
#git cherry-pick
#git reset --hard 7f8f5d9376140c1a5dca57e58ca8e2a4da34ac99
#git push --force
#git branch -D some_new_branch
#git push origin --delete some_new_branch
###################################################


print("1")
print("2")
print("3")