str1 = "PyNaTive"
str2=""
str3=""

for i in str1:
  if(i.islower()):str2+=i
  if(i.isupper()):str3+=i

print(str2+str3)