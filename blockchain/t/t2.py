import shelve
if __name__ == '__main__':
    s = shelve.open("22901.db")
    s["name"] = "www.itdiffer.com"
    s["lang"] = "python"
    s["pages"] = 1000
    s["contents"] = {"first":"base knowledge","second":"day day up"}
    s.close()
    s = shelve.open("22901.db")
    name = s["name"]
    print (name)
    contents = s["contents"]
    print (contents)
    print ('======================')
    print (s)
