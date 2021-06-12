#Author Jibreel Natsheh
#Date: June 28,2020
#edited on June 29,2020

from XmlTree import *
import time
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    #Excution for reading 3 xml file and building the trees 1000 time using createFromFile method
    testFiles = ['test1.xml', 'test2.xml', 'test3.xml']
    startTime = time.time()
    for i in range(1000):
        for file in testFiles:
            try:
                XmlTree.createFromFile(file)
            except Exception as e:
                print(str(e))
    endTime = time.time()
    execTime = endTime - startTime
    print("Excution time for reading 3 xml file and building the trees 1000 time using createFromFile method is: ")
    print(execTime)

    #Excution for reading 3 xml file and building the trees 1000 time using XML Library method
    startTime2 = time.time()
    for i in range(1000):
        for file in testFiles:
            try:
                ET.parse(file)
            except Exception as e:
                print(str(e))
    endTime2 = time.time()
    execTime2 = endTime2 - startTime2
    print("Excution time for reading 3 xml file and building the trees 1000 time using Python XML Library is: ")
    print(execTime2)
    
    files = list()
    for f in testFiles:
        try:
            tree = XmlTree.createFromFile(f)
            files.append(tree)
        except Exception as e:
            print(str(e))

    saveFiles = ['save1.xml', 'save2.xml', 'save3.xml']
    for i, f in zip(range(3), saveFiles):
        try:
            files[i].saveToFile(f)
        except Exception as e:
            print(str(e))

