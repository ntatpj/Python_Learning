list1=[1,2,3,4,65,123,313,110]
le= len(list1)
var=list1[0]
print(le,var)
list1[0]=list1[le-1]
list1[le-1]=var
print(list1)