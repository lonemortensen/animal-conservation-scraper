# =======================================================================
# Project: Animal conservation web scraper
# Description: Building web scrapers for data collection.
# The project uses Python's Beautiful Soup library to build and combine two web scrapers that extract website data on the conservation status and animal class of endangered species. The combined, extracted data is saved to a JSON file to make it easier to analyze and visualize.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====

# The main.py file contains code that:
# - requests the website to scrape, and gathers and stores all site data.
# - extracts data from the website's html on animal conservation status and
# animal class, respectively, via two separate web scrapers.
# - connects the two webscrapers to pull animal names and their conservation status
# - removes unwanted output before storing the combined data in a list of Python  dictionaries.
# - saves the dictionary data to a JSON file with each animal’s name, class, and conservation status. 
# =======================================================================

import requests
from bs4 import BeautifulSoup
import json


# Gathers data:
def get_soup(url):
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup


### Building the web scrapers:


# Web scraper 1: Extracts data on animals and their conservation status ("category"):
def get_categories(url):
  soup = get_soup(url)
  data = {}
  # Selects and extracts category animals:
  # - finds <dt> (conservation status) for each <dl> and extracts actual text from html tag.
  # - extracts all links from each <dl> (each animal is a link).
  # - adds category_name (key) and category_animals (value) (an array of links) to the "data" library:
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a")
    data[category_name] = category_animals
  return data


# Web scraper 2: Extracts the class for each animal:
def get_animal(url):
  soup = get_soup(url)
  # Extracts data from table on each animal's website by the table's class attribute:
  table = soup.find("table", {"class": "infobox biota"})
  if not table:
    return "No class found."

  rows = table.find_all("tr")
  for row in rows:
    # If row data contains the text "Class:", gets the contents of the link ("animal class" of animal):
    if "Class:" in row.get_text():
      animal_class = row.find("a").contents[0]
  return animal_class


# Calls animal conservation status function and passes website url to scrape:
category_data = get_categories(
  "https://skillcrush.github.io/web-scraping-endangered-species/")

### Combining the two web scrapers:

# Stores dictionaries, one for each animal:
collected_data = []

# Connecting the conservation status (category) and animal class web scrapers:
# - loops through each category inside the category_data (conservation status) variable:
for category in category_data:
  # Loops through the list of animals in each conservation category (e.g. "endangered"):
  for animal in category_data[category]:
    # Gets the link (href) attribute of each animal (i.e. its webpage) inside each category:
    animal_href = animal["href"]
    # Gets text inside each link:
    animal_name = animal.contents[0]
    # Passes animal webpage links to class scraper and gets class from each animal's webpage:
    animal_class = get_animal(animal_href)
    # Removes unwanted outputs:
    if len(animal_class) > 3:
      animal_data = {
        "Category": category,
        "Animal Name": animal_name,
        "Animal Class": animal_class
      }
      collected_data.append(animal_data)

# Saves dictionary data to a JSON file:
with open("data.json", "w") as jsonfile:
  json.dump(collected_data, jsonfile)
