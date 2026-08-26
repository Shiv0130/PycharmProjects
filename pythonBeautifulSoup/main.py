from bs4 import BeautifulSoup

with open("pva.html","r") as f:
    doc=BeautifulSoup(f,"html.parser")
    #print(doc.prettify())

    #tag = doc.title
    #tag.string ="PVA"
    #print(tag.string)
    #print(tag)
    #print(doc)
    # tags = doc.find_all("button")
    # print(tags)

    # tags = doc.find_all("button")[0]
    # print(tags)

    

