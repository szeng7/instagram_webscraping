from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
from tqdm import tqdm
import os.path
from os import path

XPATH = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
filename = "user_follower.txt"

def main():

    if path.exists("user_follower.pickle"):
        with open("user_follower.pickle","rb") as f:
            user_follower_dict = pickle.load(f)
    else:
        user_follower_dict = {}

    with open("users.txt", 'r') as file:
        users = file.readlines()

        for user_index in tqdm(range(len(users))):
            user = users[user_index]
            username = user.strip('\n')
            URL = "https://www.instagram.com/" + username
            browser = webdriver.Chrome(executable_path="/Users/szeng/chrome_webdriver/chromedriver")
            browser.get(URL)
            try:
                follower_count = browser.find_element_by_xpath(XPATH).get_attribute('title')
            except:
                follower_count = 0
            browser.quit()

            if username not in user_follower_dict:
                user_follower_dict[username] = follower_count

            print(f"{username}: {follower_count}")

            if user_index % 10:
                with open("user_follower.pickle", 'wb') as f:
                    pickle.dump(user_follower_dict, f)

        print(len(user_follower_dict))

if __name__ == "__main__":
    main()
