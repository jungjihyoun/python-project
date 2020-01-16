import csv

class myFile():
    def __init__(self, filename='', filemode=''):
        self.filename = filenamedks
        self.filemode = filemode
        self.file = filename



        if self.filemode == 'w':
            filemode = 'r'
            filelist = []
            file = open(self.filename, self.filemode)

            linecontent = file.readline()

            while linecontent != '':
                filelist.append(linecontent.strip('\n'))
                linecontent = file.readline()
            print(filelist)


        if self.filemode == 'r':
            file = open(self.filename, self.filemode)


#다시
    def getStatus(self):
        print(False)





    def getBody(self):
        self.file = open(self.filename, self.filemode)
        contents = self.file.readlines()
        contents = contents[1:4]
#스트립ㅎ하기
        print(contents)





    def setContentHead(self,head = ''):
        self.head = head
        self.headlist = None
        #리스트형태로 받음
        if head != '':
            self.headlist = head
            print(self.headlist)
            return True
        elif head == '':
            self.headlist = None
            print("error")
            return False

    def setContentBody(self,body=''):
        self.body = body
        self.bodylist = None
        if body != '' :
            self.bodylist = body
            print(self.bodylist)
            return True
        elif body == '' :
            self.bodylist = None
            print("error")
            return False

    def writeFile(self):
        a = myFile(self.filename,self.filemode)
        b = myFile(self.filename,self.filemode)

        a.setContentHead(self.head)
        b.setContentBody(self.body)

    def closeFile(self):
        self.file.close()


    def mergeList(self,list1,list2):
        newlist=[]
        while True:
            for i in len(list1):
                if list1[i] in list2[:]:
                    newlist.append[list2]









file1 = myFile("inputdata1.csv", 'r')
file2 = myFile("inputdata2.csv", 'r')

if (file1.getStatus() != False) and (file2.getStatus() != False):
    newList = mergeList(file1.getBody(), file2.getBody())

    file3 = myFile("output.csv", 'w')
    filelist = []
    file = open('inputdata1.csv', 'r')

    linecontent = file.readline()

    while linecontent != '':
        filelist.append(linecontent.strip('\n'))
        linecontent = file.readline()
    print(filelist)
    file.close

else:
    print("input file error")

file1.closeFile()
file2.closeFile()