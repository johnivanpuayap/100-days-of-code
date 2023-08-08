from bs4 import BeautifulSoup

with open("Day 45\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# Get hold of the first anchor tag
# print(soup.a)

# # Get hold of all the anchor tags
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    
#     # Get the String inside the anchor tag
#     print(tag.getText())

#     # Get the href of the anchor tag
#     print(tag.get("href"))

# # Get hold of elements by their ID
# heading = soup.find(name="h1", id="name")
# print(heading.text)

# # Get hold of elements by their Class
# heading = soup.find(name="h3", class_="heading");
# print(heading.text)

# soup.find_all("a")

# Get hold of an element inside an element
# Inside the selector argument you can specify . and # if needed
company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

headings = soup.select(".heading")
print(headings)