import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

url='https://www.fiu.edu/academics/degrees-and-programs/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())

courses = []
for course in soup.find('ul', class_='list'):
    title=course.find('p', class_='program').text
    details = course.find('span', class_='degree-type').text
    # print(title.strip())
    courses.append([title,details])

print(courses)
