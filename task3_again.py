import pywikibot
import re
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
    z = re.match(r'(?:^\|.*[a-z]$)', item)
    if z is not None:
     m =z.group(0)
     x = m.split('=')
     y = x[0].split('|')[1].strip()
     print( y , ':', x[1])
     #pid = input(' all infobox information has been printed, now check for some specific information. Give the property id which you want to check?") 
     
     if y == 'location':                
        print( y , ":" , x[1])     
         