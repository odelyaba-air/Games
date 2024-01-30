from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_scores_service(url):
    driver = None

    try:
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(2)

        score_element = driver.find_element(By.ID, 'score')

        score = int(score_element.text)

        return 1 <= score <= 1000
    except Exception as e:
        print(f"Error during test: {str(e)}")
        return False
    finally:
        if driver is not None:
            driver.quit()


def main_function(url):
    if test_scores_service(url):
        print("Tests passed successfully.")
        return 0
    else:
        print("Tests failed.")
        return -1


# Example usage:
if __name__ == "__main__":
    app_url = "http://localhost:5000/"
    exit_code = main_function(app_url)
    exit(exit_code)
