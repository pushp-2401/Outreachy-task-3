import pywikibot
from pywikibot import pagegenerators
from pywikibot.data import api
import numpy as np
import requests
import re

enwiki = pywikibot.Site('en', 'wikipedia')
enwiki_repo = enwiki.data_repository()

def parsesite(url):
    try:
        r = requests.get(url)
        websitetext = r.text
    except:
        print ('Problem fetching page!')
        return 0
    print (websitetext)
    s= websitetext.split('<div class="wikibase-statementgrouplistview">')[1].split('<div class="wikibase-statementgroupview-property-label" dir="auto">')
    
    i = 0
    for item in s:
        i+=1
        
        s1 = item.split()[1]
        
       
        Pid = str(s1[16:len(s1)-1])
        #
        if i>1 and Pid == 'P31': 
           s2 = item.split( '<div class="wikibase-snakview-value wikibase-snakview-variation-valuesnak">')[1]
           s3 = s2.split()[1]
           qid=re.search(r'[Q][0-9].*[0-9]',s3).group()
           if qid != None:
               try:
               
                  #print(qid)  
                  #print('done')
                  wd_item = pywikibot.ItemPage(enwiki_repo, qid)
                  item_dict = wd_item.get()
                  label = str(item_dict['labels']['en'])
                  print ( Pid , ':',  label)
               except:
                  print( Pid, qid )           
        
        
        
             
             
    return 0

parsesite('https://www.wikidata.org/wiki/Q15961638')
parsesite('https://www.wikidata.org/wiki/Q19675')

    