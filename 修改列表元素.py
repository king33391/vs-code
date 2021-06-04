#修改指定元素
names=['king','sara','Sansics','Moriarty']
names[0]='Sherlock'
print(names)

#增加元素
#“append()”在列表末端增加元素
names=['king','sara','Sansics','Moriarty']
names.append('Sherlock')
print(names)

names=[]    #先创建空列表，再将用户输入的信息依次作为元素填充到列表中。控制用户，储存输入的信息。
names.append('Sherlock');names.append('sara');names.append('King')
print(names)

#“insert(位置，'值')”在列表中插入元素,需要指定要插入的位置。
names=['king','sara','Sansics','Moriarty']
names.insert(1,'Sherlock')
print(names)

#删除元素     用户注销账号后删除其信息
# del()  删除列表指定位置的元素，且无法再次访问 
names=['king','sara','Sansics','Moriarty']
del names[1]
print(names)

#pop()   删除列表指定位置的元素，并可以接着使用被删除的元素。   将用户从活跃列表中删除，并送到不活跃列表中。
names=['king','sara','Sansics','Moriarty']
popped_name=names.pop(1)
print(names)
print(popped_name)

#remove()   删除指定值的第一个元素（要删除所有指定值的元素还需要用到for循环遍历），用于不确定元素在列表中的位置时使用，被删除的元素同样可以接着被使用。
names=['king','sara','Sansics','Moriarty']
names.remove('sara')
print(names)