import copy
from XmlElement import XmlElement
import os
import re
class XmlTree:
    def __init__ (self, root = XmlElement(), size = 0):
        self.root = copy.deepcopy(root)
        self.size = size

    @staticmethod
    def createFromFile (filePath):
        root = XmlElement()
        del root.children[:]
        size = 0
        exp = "(?<=<)(\/?[a-zA-Z1-9_][a-zA-Z1-9_.:-]+)|(\S+)=[\"']?((?:.(?![\"']?\s+(?:\S+)=|[>\"']))+.)[\"']?|((?<=>)[^<\n]*(?=<|\n))"
        if os.path.isfile(filePath):
            with open(filePath, 'r') as read_file:
                elements = re.findall(exp, read_file.read())
                currentTag = XmlElement()
                #assign each element according to it's type and position
                for i in range(len(elements)):
                    #if the element is a tag
                    if elements[i][0]:
                        #if the tag was a closing tag
                        if elements[i][0][0] == '/':
                            currentTag = currentTag.parent
                        #else then it is a new tag
                        else:
                            #if it is the root tag
                            if size == 0:
                                root.name = elements[i][0]
                                currentTag = root
                                size+=1
                            #if it is not the root tag
                            else:
                                newTag = XmlElement(elements[i][0], currentTag, [], {}, '')
                                currentTag.children.append(newTag)
                                currentTag = newTag
                                size+=1
                    #if the element is an attribute
                    elif elements[i][1]:
                        #if it is the root tag
                        if size == 0:
                            root.attributes.update({elements[i][1] : elements[i][2]})
                            currentTag = root
                        #if it is not the root tag
                        else:
                            currentTag.attributes.update({elements[i][1] : elements[i][2]})
                    elif elements[i][3]:
                        #if it is the root tag
                        if size == 0:
                            root.text = elements[i][3]
                            currentTag = root
                        #if it is not the root tag
                        else:
                            currentTag.text = elements[i][3]
                        
                    else:
                        pass
        return XmlTree(root, size)

    @staticmethod
    def printPreorder(root): 
        xmlStr = ''
        if root: 
            # First print the data of the root tag
            xmlStr += '<'+root.name
            for attribute in root.attributes:
                xmlStr += ' ' + attribute + '=' + '\"'+root.attributes[attribute]+'\"'
            xmlStr += '>' + ' ' + root.text
            # Then recur on childs
            for child in root.children:
                xmlStr += '\n\t' + XmlTree.printPreorder(child) +'\n'

            xmlStr +='</' + root.name + '>'
        return xmlStr


    def saveToFile(self, filePath = 'saved.xml'):
        with open(filePath, 'w+') as write_file:
            xmlStr = XmlTree.printPreorder(self.root)
            write_file.write(xmlStr)