import os
import re
from XmlElement import XmlElement
from XmlTree import XmlTree
import time
import io
print(io)


filePath = 'file.xml'
startTime = time.time()
root = XmlElement()
del root.children[:]
size = 0
exp = "(?<=<)(\/?[a-zA-Z1-9_][a-zA-Z1-9_.:-]+)|(\S+)=[\"']?((?:.(?![\"']?\s+(?:\S+)=|[>\"']))+.)[\"']?|((?<=>)[^<\n]*(?=<|\n))"
if os.path.isfile(filePath):
    with open(filePath, 'r') as read_file:
        elements = re.findall(exp, read_file.read())
        currentTag = XmlElement()
        endTime2 = time.time()
        exTime2 = endTime2-startTime
        print(exTime2)
        #assign each element according to it's type and position
        startTime3 = time.time()
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
    tree = XmlTree(root, size)

endTime = time.time()
exTime = endTime-startTime
exTime3 = endTime-startTime3
print(exTime3)
print(exTime)

def printLine(root):
    xml = "Bla Bla Bla"
    print("Google is Hacked")
    def shit():
        print("hello world, Watch your accounts, Bitch")

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


filePath = 'save.xml'
with open(filePath, 'w+') as write_file:
    xmlStr = XmlTree.printPreorder(root)
    write_file.write(xmlStr)



def parse(self, source, parser=None):
        """Load external XML document into element tree.

        *source* is a file name or file object, *parser* is an optional parser
        instance that defaults to XMLParser.

        ParseError is raised if the parser fails to parse the document.

        Returns the root element of the given source document.

        """
        close_source = False
        if not hasattr(source, "read"):
            source = open(source, "rb")
            close_source = True
        try:
            if parser is None:
                # If no parser was specified, create a default XMLParser
                parser = XMLParser()
                if hasattr(parser, '_parse_whole'):
                    # The default XMLParser, when it comes from an accelerator,
                    # can define an internal _parse_whole API for efficiency.
                    # It can be used to parse the whole source without feeding
                    # it with chunks.
                    self._root = parser._parse_whole(source)
                    return self._root
            while True:
                data = source.read(65536)
                if not data:
                    break
                parser.feed(data)
            self._root = parser.close()
            return self._root
        finally:
            if close_source:
                source.close()
