import os
from xml.etree import ElementTree

filename= "data.xml"
fullfile= os.path.abspath(os.path.join( filename))

dom = ElementTree.parse(fullfile)

username = dom.findall('login/username')
password = dom.findall('login/password')

for c in username:

    print(c.text)

for l in password:

    print(l.text) 



#========== crate xml file data.xml=========== 

# <root>

#  <login>
#  <username>ddddd</username>
#  <password>sfssfs</password>
#  </login>

# </root>

