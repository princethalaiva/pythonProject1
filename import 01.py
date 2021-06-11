#[Yesterday 3: 57PM] AbdulKaleemAnsariMohammed

import re

data = "My name is Ansari and the age is 40 and the address is 124 Bangalore the"

res = re.search("the", data)
res = re.findall("the", data)

print(res)

if res:
    print("there is a match")
else:
    print("no match found")

#--------------------------------------------

import re

data = "My _ name is Ansari and the age is 40 $ ! and the address is 124 Bangalore the"

res = re.findall("[A-Za-z]", data)

print(res)

#---------------------------------------------

import re

data = "My _ name is Ansari and theee age is 40 $ ! and the address.. is 124 Bangalore thee"

res = re.findall("..e{1}", data)

print(res)

