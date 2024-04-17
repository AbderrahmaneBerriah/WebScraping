Importing Libraries:

Import necessary libraries for web scraping using Selenium, handling CSS selectors, and storing data in a Pandas DataFrame.
Initializing Chrome WebDriver:

Initialize a Chrome WebDriver instance to interact with the Chrome browser.
Setting User Agent:

Set a custom user agent for the Chrome browser to simulate different client devices or browsers.
Defining Input and Output Files:

Define the file paths for the input file containing URLs to scrape and the output Excel file where scraped data will be stored.
Scraping and Storing Data:

Open the input file and read URLs line by line.
For each URL, scrape specific elements using CSS selectors and extract text content.
Store the scraped data (address, borough, lot number, matricule number, predominant use, neighborhood unit number, dossier number) in a list of lists.
Error Handling:

Catch and print any exceptions that occur during scraping, indicating the URL where the error occurred.
WebDriver Cleanup:

Quit the WebDriver instance to release resources after scraping is complete.
Converting Data to DataFrame:

Convert the scraped data list into a Pandas DataFrame, with column names defined.
Writing Data to Excel:

Write the DataFrame to an Excel file, omitting the index column.
Print Final Message:

Print a message indicating the location where the scraped data has been saved in Excel format.
