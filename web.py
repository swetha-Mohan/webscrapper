import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url='https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_'
headers = {"Accept-Language": "en-US, en;q=1"}
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

#initiate data storage
names = []
authors = []
ratings = []
user_rated = []
prices = []
book_div = soup.find_all('div', class_='a-section a-spacing-none aok-relative')

#our loop through each container
for container in book_div:

        #name
        name = container.find('span', attrs={'class':'zg-text-center-align'})
        
        n = name.find_all('img', alt=True)
        
        #print(n[0]['alt'])
        author = container.find('a', attrs={'class':'a-size-small a-link-child'})
        
        rating = container.find('span', attrs={'class':'a-icon-alt'})
        
        users_rated = container.find('a', attrs={'class':'a-size-small a-link-normal'})
        
        price = container.find('span', attrs={'class':'p13n-sc-price'})
        
        

        if name is not None:
           
            names.append(n[0]['alt'])
        else:
            names.append("unknown-product")

        if author is not None:
            
            authors.append(author.text)
        elif author is None:
            author = container.find('span', attrs={'class':'a-size-small a-color-base'})
            if author is not None:
                authors.append(author.text)
            else:    
                authors.append('0')

        if rating is not None:
            
            ratings.append(rating.text)
        else:
            ratings.append('-1')

        if users_rated is not None:
            
            user_rated.append(users_rated.text)
        else:
            user_rated.append('0')     

        if price is not None:
            
            prices.append(price.text)
        else:
            prices.append('0')
         
#pandas dataframe        
books = pd.DataFrame({
'BookName': names,
'AuthorName': authors,
'BookRating': ratings,
'UserRating': user_rated,
'BookPrice': prices,

})




books.to_csv('amaz_products.csv')


