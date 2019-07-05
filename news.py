#importing newspaper3k module of python
import newspaper

cnn_paper = newspaper.build('http://cnn.com')
# to print all the articles on the cnn mainpage
for article in cnn_paper.articles:
  print(article.url)

# to print all the categories available at the cnn mainpage
for category in cnn_paper.category_urls():
  print(category)

