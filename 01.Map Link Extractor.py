from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Set user agent for Chrome
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
options = Options()
options.add_argument(f"user-agent={user_agent}")

# Initial offset value and increment value
initial_offset = 0
offset_increment = 1000

# Original URL
url = "https://carte.ville.quebec.qc.ca/ArcGIS/rest/services/CIMobile/Proprietes/MapServer/0/query?f=json&where=&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22%22ymin%22%22xmax%22%22ymax%22%22spatialReference%22:%20{%22wkid%22:%2032187,%20%22latestWkid%22:%2032187}}&geometryType=esriGeometryEnvelope&inSR=32187&outFields=CUQ_IDF_ID%2CURL_FICHE&resultOffset="

# Output file path
output_file = "F:\Jupyter_directory\selenium\linksfull.txt"

try:
    with open(output_file, "w") as outputfile:
        offset = initial_offset
        while True:
            # Fetch the data with the current offset
            driver.get(url + str(offset))

            # Parse the response JSON
            response_text = driver.find_element(By.XPATH, "//pre").text
            response_json = json.loads(response_text)

            if "features" in response_json:
                for feature in response_json["features"]:
                    attributes = feature.get("attributes")
                    if attributes and "URL_FICHE" in attributes:
                        url_fiche = attributes["URL_FICHE"]
                        print(url_fiche)
                        outputfile.write(f"{url_fiche}\n")

            # Increment the offset by 1000
            offset += offset_increment

            # Break the loop if there are no more features
            if len(response_json.get("features", [])) == 0:
                break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
