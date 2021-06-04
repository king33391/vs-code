# .sort()  按字母顺序（且先大写后小写）对列表进行永久排序，无法恢复。
names=['King','Sara','Sansics','Moriarty']
names.sort()
print(names)

# .sort(reverse=True)  永久反序排列
names=['king','sara','Sansics','Moriarty']
names.sort(reverse=True)
print(names)

# sorted()  临时排序，以字母顺序显示，但不改变原列表顺序。
names=['King','Sara','Sansics','Moriarty']
print("\nHere is the list of our guests:"+str(names))
print("\nHere is the  sorted list of our guests:"+str(sorted(names)))
print("\nHere is the  original list of our guests:"+str(names))

# .reverse()  反转列表元素顺序，永久改变，再次用.reverse()可以恢复原顺序。
names=['King','Sara','Sansics','Moriarty']
names.reverse()
print(names)

# len()  确定列表长度    用来确定有多少用户。
names=['King','Sara','Sansics','Moriarty']
print(len(names))
