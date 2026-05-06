# Web Data Extraction Exercise

This exercise covers techniques for extracting data from the internet using Python, focusing on two main approaches:
1. Downloading structured data from files
2. Scraping unstructured data from web pages

## Prerequisites

### Setting up the environment

1. Activate the ppchem environment:
   ```bash
   conda activate ppchem
   ```

2. Install the required packages:
   ```bash
   pip install requests beautifulsoup4 IPython
   ```

## Exercise Overview

### Part 1: Using the Requests Library
- Learn how to make HTTP GET requests using the `requests` library
- Handle HTTP responses and status codes
- Implement error handling with try-except blocks

### Part 2: Web Scraping with BeautifulSoup
- Parse HTML content using BeautifulSoup
- Navigate and search HTML parse trees
- Extract specific elements from web pages

### Part 3: Practical Tasks
1. Extract all URLs from a webpage
2. Find and extract exercise and solution links from a university chemistry teaching page
3. Compare your manual implementation with ChatGPT's solution

### Part 4: Working with Chemical Data
- Convert SMILES strings to molecular structure images
- Construct URLs with parameters for the CDK Depict service
- Display SVG images of molecular structures

## Tips for Success
- Pay attention to HTML structure when scraping web pages
- Use browser developer tools to inspect webpage elements
- Remember to handle potential errors in HTTP requests
- Test your constructed URLs in a browser before implementing them in code

## Learning Objectives
- Understand HTTP request-response cycle
- Develop skills in web scraping using Python libraries
- Apply these techniques to chemistry-related data extraction
- Compare manual implementation with AI-assisted solutions

Happy coding!