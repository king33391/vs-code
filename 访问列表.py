#列表   “[]”来表示列表 ; 用","分隔开元素 ; 索引从“0”开始
names=['king','sara','Sansics','Moriarty']
print(names)
print(names[1].title())
print(names[-2].title())   #"-1"表示列表中的最后一个元素，依次类推

message="Hi "+names[3].title()+","+"How are you?"
print(message)