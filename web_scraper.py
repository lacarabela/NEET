import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

links = []
for page in range(0, 17900, 50):
    driver.get('https://myanimelist.net/topmanga.php?limit=' + str(page))
    link = driver.find_elements(By.CSS_SELECTOR, 'div[class="detail"] h3 a')
    for item in link:
        links.append(item.get_attribute('href'))

titles = []
ratings = []
genres = []
for item_link in links:
    driver.get(item_link)
    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="h1-title"]')))
    rating = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class*="score-label"]')))
    genre = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Genre")]/parent::div')))
    titles.append(title.text)
    ratings.append(rating.text)
    genres.append(genre.text)

my_data = {'Titles': titles, 'Ratings': ratings, 'Genres': genres}
df = pd.DataFrame(my_data)

csv_file_path = 'C:/Users/maldo/Desktop/anime/AnimeList.csv'
df.to_csv(csv_file_path, index=False)
