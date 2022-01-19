from asyncore import read


def swapFileData():
    file1=input("Enter your first file name")
    file2=input("Enter your second file name")
    a=open(file1,'r')
    dataA=a.read()
    b=open(file2,'r')
    dataB=b.read()
    a=open(file1,'w')
    a.write(dataB)
    b=open(file2,'w')
    b.write(dataA)
swapFileData()
