# Web-Scrapper

## Overview

This Python script scrapes all 50 pages of the catalogue from [books.toscrape.com](http://books.toscrape.com). It extracts key information for every book and saves the data into a clean, ready-to-use CSV file named `books.csv`.
This script can be easily adapted to scrape data from any website that does not employ bot protection.

## Features

* **Full Site Scraping:** Navigates through all 50 pages of the book catalogue automatically.
* **Multiple Data Points:** Extracts all pieces of information for each book:
    * Title
    * Price
    * Stock Availability
    * Rating
* **CSV Export:** Saves the structured data to a `books.csv` file for easy use in Excel, Google Sheets, or data analysis software.


## Requirements

* Python 3.x
* The libraries listed in the `requirements.txt` file.

## How to Run the Script

1.  **Clone the repository:**
    `git clone https://github.com/OmkarSarkar204/Python-Web-Scrapper.git`
2.  **Navigate to the project directory:**
    `cd Python-Web-Scrapper`
3.  **Install the required libraries:**
    `pip install -r requirements.txt`
4.  **Run the script:**
    `python books_scraper.py`

After the script finishes, you will find a `books.csv` file in the directory containing all the scraped book data.
