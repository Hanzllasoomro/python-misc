from lxml import etree

def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if elem.text:
                text = elem.text
            else:
                text = ''
            if elem.tag == 'author':
                last_name, first_name = text.split(',')
                print(elem.tag + ':', first_name, last_name)
            else:
                print(elem.tag + ": " + text)
            book_dict[elem.tag] = text
        if book.tag == "book":
            books.append(book_dict)
            book_dict = {}
    return books

my_books = parseBookXML(".\\books.xml")
