# Animal Conservation Web Scraper: Building and Combining Scrapers
Building and combining two web scrapers with Python's Beautiful Soup library. 

## About
Using the Beautiful Soup library to build and combine two web scrapers, this project extracts data from a website on the conservation status and animal class of endangered species. The extracted and combined data is saved to a JSON file to make it easier to analyze and visualize. 

## Project Background
The project was built as part of the coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

During this project, I practiced: 

- Extracting and saving data (text and links) stored in html tags and nested html tags to a library, using loops and Beautiful Soup's find_all(), find(), and get_text() methods. 

- Extracting specific data by filtering by the class attribute of html tags, using an if statement, the get_text() and find() methods, and the contents attribute to check for and access specific text in the extracted data.   

- Combining two web scrapers into one web scraper by passing data from the first scraper to the second scraper, using for loops and the href attribute to get the relative url of each animal and extract data on its animal class. 

- Using the combined web scraper to pull animal names and their conservation status, creating a list of dictionaries containing the "Category", "Animal Name", and "Animal Class" for each animal. 

- Exporting the data from the combined web scrapers to a JSON file.   

## Built With 
- Python
- Beautiful Soup
- JSON module
- Requests 

## Launch
[See the project here.](https://replit.com/@lonemortensen/skillcrush-py-cl03-ls10-scraper-species-beautSoup-final)

## Acknowledgements

**Skillcrush** - I coded the project's main.py file with support and guidance from Skillcrush. 