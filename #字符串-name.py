#字符串-name
name="ada love"
print(name.title())   #“name"是变量，"."是对 “title”所指代的方法（首字母大写）的操作。方法后一定要带（）。
#全部大写或小写输出（可用于 不管用户输入的是大/小写，统一识别为小写输出）
name="ada love"
print(name.upper())
print(name.lower())

#合并字符串 （+）
first_name="ada" ;last_name="love";full_name=first_name+" "+last_name
message="Hello,"+full_name.title()+"!"
print(message)