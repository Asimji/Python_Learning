input="masai"

str=""

for key in range(len(input)-1,-1,-1):
  str+=input[key]

def palindrome(input,str):
  flag=True
  for key in range(len(input)):
   if(input[key]!=str[key]):
         flag=False
   break
    
  return flag

output=palindrome(input,str)

if(output==True):print("Palindrome")
else:print("Not a Palindrome")  


