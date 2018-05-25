import shelve
import os
import pickle
class Book(object):             #自定义一种类型
     def __init__(self,name):
         self.name = name
     def my_book(self):
         print ("my book is: " + self.name)
         return self.name

if __name__ == '__main__':
    s = shelve.open("22901.db")
    s["name"] = "www.itdiffer.com"
    s["lang"] = "python"
    s["pages"] = 1000
    s["contents"] = {"first":"base knowledge","second":"day day up"}
    s.close()
    s = shelve.open("22901.db")
    name = s["name"]
    #print (name)
    contents = s["contents"]
    #print (contents)
    #print ('======================')
    #print (s)




    """
    fd = open ('blockchain.data', 'wb')
    #fd.write (buf.getvalue ())

    pybook = Book("<from beginner to master>")
    print(pybook.my_book())
    pickle.dump(pybook,fd)
    fd.close()
    """
    if os.path.exists('blockchain1.data'):
        print('File exists')
    else:
        print('no exists')
    fd = open ('blockchain.data', 'rb')
    pybook2 = pickle.load(fd)
    print('book2' + pybook2.my_book())

    
