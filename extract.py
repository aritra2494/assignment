

import textract
import re
text = textract.process('C://Users//admin//Desktop//New folder//resume.pdf')



txt=str(text)

match = re.findall(r'[\w\.-]+@[\w\.-]+', txt)
for i in match:
    print(i)# mail ids


for j in re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', txt):
    print (j)# phone numbers

txt1 =list(txt)
s=txt1.readlines()
print (s[0])




