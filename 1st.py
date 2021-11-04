#creating 3 lists , 2 full and 1 empty
list1=[3,6,9,12,15,18,21]
list2=[4,8,12,16,20,24,28]
list3=[]
#we use the function enumarate to get access the the index of items in list 1 / we look for odd index by devising it on 2
for index, item in enumerate(list1):
    if index%2!=0:
        #we insert the item with the odd index in the list3 at the end
        list3.append(item)
#same for list 2
for idx , itm in enumerate(list2):
    if idx%2==0:
        list3.append(itm)
print(list3)
