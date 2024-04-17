from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Set user agent for Chrome
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
options = Options()
options.add_argument(f"user-agent={user_agent}")

# Input file containing URLs
input_file = r"F:\Jupyter_directory\selenium\filtered_links.txt"

# Output file for scraped data in Excel format
output_excel_file = r"F:\Jupyter_directory\selenium\output_data.xlsx"

scraped_data = []
try:
    with open(input_file, "r") as file:
        urls = file.readlines()

    # Scrape each URL and store the data in a list of dictionaries
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace and newline characters
        try:
            driver.get(url)
            adrs = driver.find_element(By.CSS_SELECTOR,'#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(1) > td')
            arron = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(2) > td')
            ndl = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(3) > td')
            nm = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(4) > td')
            up = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(5) > td')
            nuv = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(6) > td')
            dos = driver.find_element(By.CSS_SELECTOR, '#ctl00_ctl00_contenu_texte_page_fichePropriete_divRole > table.table_identification_unite > tbody > tr:nth-child(7) > td')
            
            adrst = adrs.text.strip()
            arront = arron.text.strip()
            ndlt = ndl.text.strip()
            nmt = nm.text.strip()
            upt = up.text.strip()
            nuvt = nuv.text.strip()
            dost = dos.text.strip()

            # Store the scraped data in a list
            scraped_data.append([adrst, arront, ndlt, nmt, upt, nuvt, dost])
            
            print(nuvt)
        except Exception as e:
            print(f"An error occurred while scraping {url}: {e}")
finally:
    driver.quit()

    # Convert the scraped data to a pandas DataFrame

df = pd.DataFrame(scraped_data, columns=['Adresse','Arrondissement','Numéro de lot','Numéro matricule','Utilisation prédominante',"Numéro d'unité voisinage",'Dossier no'])
    
df.to_excel(output_excel_file, index=False)

print(f"Scraped data written to: {output_excel_file}")
