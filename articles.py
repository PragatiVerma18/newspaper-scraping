#importing Article from newspaper module
from newspaper import Article

url = 'https://www.foxnews.com/science/elon-musk-moon-mars-twitter' # change this url to any article

article = Article(url, language="en")

article.download()

article.html

article.parse()

#print the article's authors, text and main image url
print("Article by: ", article.authors[0])
print("Article text: ", article.text)
print("Hero Image:", article.top_image)


