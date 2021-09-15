class HtmlBuilder(object):

    def __init__(self):
        self.doc = None

    def createHtml(self):
        name = input("\nEnter the name for your HTML-page: ")   
        self.doc = open(name + ".html", 'w')

    def createTitle(self):
        print (t[0], file=self.doc) #<!DOCTYPE html>
        print (t[1], file=self.doc) #<html>
        print (t[2], file=self.doc) #<head>
        title = input("Enter your title here: ")
        print ("  <title>",title,"</title>", file=doc)
        print (t[3], file=self.doc) #</head>

    def Dispose(self):
        self.doc.flush()
        self.doc.close()

hb = HtmlBuilder()
while True:
    menu = input("\nPress 1 to enter the file name for the HTML-page"
                 "\nPress 2 to enter title for the HTML-page"
                 "\nPress 3 to start entering code in body"
                 "\nPress 4 to exit\n")
    if menu == "1":
        hb.createHtml()
    elif menu == "2":
        hb.createTitle()
    elif menu == "3":
        hb.createBody()
    else:
        print ("Good bye!")
        break

hb.Dispose()