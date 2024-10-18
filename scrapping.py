import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

# Send a request to the university's course page
url='https://www.fiu.edu/academics/degrees-and-programs/index.html'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} -requests.get('url',headers=headers).text
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

# Extract course information
courses = []
for course in soup.find('ul', class_='list'):
    title=course.find('p', class_='program').text
    details = course.find('span', class_='degree-type').text
    # print(title.strip())
    courses.append([title,details])

print(courses)

# # Convert to DataFrame and save to Excel
# df = pd.DataFrame(courses, columns=['Course Title', 'Description'])
# df.to_excel('university_courses.xlsx', index=False)
