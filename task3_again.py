import pywikibot
import re
prop_dict = { "name" :"P735", "image" :"P18","caption" :"P2096","curator" :"P1640", "title" :"P1448", "publisher" :"P123", "url" :"P854", "image1" :"P18" , "image2":"P18", "image3":"P18", "image4":"P18"}      
site = pywikibot.Site("en", "wikipedia")
page = pywikibot.Page(site, "Louvre")
text = page.get()
#text.splitlines()
# print(text[3])
# print(type(text))
#inforegex = re.search(r'(?=\{Infobox)(\{([^{}]|(?1))*\})' , text)
# # infobox = inforegex.search(text)
#print(inforegex)
split = text.split('\n')

for item in split:
    flag = 1
    z = re.match(r'(?:^\|.*[a-z]$)', item)
    if z is not None:
     m =z.group(0)
     x = m.split('=')
     y = x[0].split('|')[1].strip()
     #print( y , ':', x[1])
     for keys in prop_dict.keys():
        if y == keys:
           print( prop_dict[keys] , ':' , x[1])  # prints infobox information and replace property name with P-id
           flag = 0
           if y == "image":        #name can be changed subsequesntly to to indicate which property i found manually in task1.
            print('above property found manually in task1')    #line to indicate which property was found manually
     if flag:
        print ( y , ':', x[1])              #prints infobox information if no P-id is found for that in prop_dict. 
     
     