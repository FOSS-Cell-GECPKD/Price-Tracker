import requests  
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
import smtplib 
import io  
import csv 

# The front end can make use of the passing parameters
# In the dropdown list, the developer can give the Words like Laptops, Mobiles, Cameras, Headphones, Air conditioners etc
# Also the user can define the limit of number of pages to scrap [It is used in both functions]

def get_urls(DropDownSelection,limit):
  urlss=[] 
  # 1 = Laptops, 2 = Mobiles, 3 = Cameras, 4 = Headphones, 5 = AC's  
  switch= {
      1: 'https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&page=',
      2: 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=',
      3: 'https://www.flipkart.com/cameras/pr?sid=jek,p31&otracker=categorytree&page=',
      4: 'https://www.flipkart.com/headphones/pr?sid=fcn&otracker=categorytree&page=',
      5: 'https://www.flipkart.com/air-conditioners/pr?sid=c54&otracker=categorytree&page='
  }
  for i in range(1,limit):
    item = switch[DropDownSelection] + str(i)
    urlss=urlss+[item]
  # Change the variable with a dropdown box when merging with its front end according to the need
  return (urlss)

def scrape_page(urlss,limit):
  title=[]
  amount=[]
  linkss=[]
  ratings=[]
  #only use n-1 pages for removing out of index error
  for i in range(1,limit-1):  
    myurl= urlss[i]
    ucli= ureq(myurl)
    #reads the webpage and transfers to a variable
    page_html = ucli.read() 
    ucli.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
    #After fixing the whole target, the scraper moves towards the content using findAll function 
    for container in containers:
      datas=container.findAll("a",{"class":"_31qSD5"})
      link=container.findAll("div",{"class":"_1UoZlX"})
      for nextlinks in link:
        orglink=nextlinks.a.get('href')
        #Found the links for the targeted product
        real="https://www.flipkart.com"+orglink
        linkss=linkss+[real]
      for data in datas:
        nextcontainers = data.findAll("div",{"class":"_1uv9Cb"})
        for cont in nextcontainers:
          realprice=cont.div.text
          #Found price
          amount=amount+[realprice]
        maindata=data.findAll("div",{"class":"_1-2Iqu row"})
        for headdata in maindata:
          head=headdata.findAll("div",{"class":"col col-7-12"})
          mt=head[0].div.text
          #Found title
          title=title+[mt]
          #Found ratings
          rating=headdata.findAll("div",{"class":"niH0FQ"})
          try:
            oo=rating[0].span.text
            ratings=ratings+[oo]
          except:
            ratings=ratings+["No rating"]
          
  #for different type of page  
  if not title:  
    #only use n-1 pages for removing out of index error
    for i in range(1,limit-1):  
      myurl= urlss[i]
      ucli= ureq(myurl)
      #reads the webpage and transfers to a variable
      page_html = ucli.read() 
      ucli.close()
      page_soup = soup(page_html,"html.parser")
      containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
      #After fixing the whole target, the scraper moves towards the content using findAll function 
      for container in containers:
        datas=container.findAll("div",{"class":"_3liAhj"})
        for data in datas:
          link=container.findAll("a",{"class":"Zhf2z-"})
          for nextlinks in link:
            orglink=nextlinks.get('href')
            #Found the links for the targeted product
            real="https://www.flipkart.com"+orglink
            linkss=linkss+[real]
          maindata=data.findAll("a",{"class":"_2cLu-l"})
          mt=maindata[0].text
          subdata=data.findAll("div",{"class":"_1rcHFq"})
          sb=subdata[0].text
          #Found title
          title=title+[mt]
          rating=data.findAll("div",{"class":"niH0FQ _36Fcw_"})
          #Found ratings
          try:
            oo=rating[0].span.text
            ratings=ratings+[oo]
          except:
            ratings=ratings+["No rating"]
          nextcontainers = data.findAll("div",{"class":"_1vC4OE"})
          realprice=nextcontainers[0].text
          #Found price
          amount=amount+[realprice]
        
  #Returns the Links, Ratings, Amount, Number of products scraped in list with strict order
  return (linkss, title, ratings, amount, len(amount)) 

# Call the function like : scrape_page(get_urls(4,6),6), where 4 specifies the dropdownselection and 6 is the number of pages
