#xml file Generater--- 


import xml.etree.ElementTree as xml

def GenerateXML(fileName):
    root=xml.Element("Customers")
    cl=xml.Element("Customer")
    root.append(cl)
    type1=xml.SubElement(cl,"place")
    type1.text="UK"

    Amount1=xml.SubElement(cl,"Amount")
    Amount1.text="4500"

    tree=xml.ElementTree(root)
    with open(fileName,"wb") as files:
        tree.write(files)

if __name__=="__main__":
    GenerateXML("Cus.xml")


