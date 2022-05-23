import re
txt="The welcome to coding tricks spain"
x = re.search("^The.*spain",txt)
#####search_function##########
 if x:
     print("yes! we found it!")
 else:
     print("oops!No text found!")


 text="The rain in spain"
 x = re.findall("[a-m]",text)
 print(x)

 txat="The rain in spain"
 x = re.split("\s",txat)
print(x)

tcxt="The rain in spain"
x=re.sub("\s", "9", tcxt,1)
print(x)
