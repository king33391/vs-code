#添加空白
#制表符“\t"  换行符“\n” 
message="Languages:\n\tPython\n\tC\n\tJava"
print(message)

#删除空白  用于整理用户输入，统一格式
#删除开头、结尾、全部的空白分别调用：“lstrip"、”restrip"、“strip"
Love="      Jane         "
Love=Love.lstrip()
print(Love)

Love="      Jane         "
Love=Love.rstrip()
print(Love)

Love="      Jane         "
Love=Love.strip()
print(Love)