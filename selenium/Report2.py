from selenium import webdriver
import json
import time
import csv





chrome_options = webdriver.ChromeOptions()
settings = {
           "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
file = open("report.csv")
csvreader = csv.DictReader(file, delimiter=",")
rows = []
for row in csvreader:
    print(row["url"])
    url_page = row["url"]
    driver.get(url_page)
    time. sleep(15)
    driver.execute_script('window.print();')
driver.quit()
file.close()





