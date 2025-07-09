from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set up ChromeOptions for headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Use new headless mode for Chrome 109+
options.add_argument("--disable-gpu")   # Disable GPU acceleration (optional)
options.add_argument("--no-sandbox")    # Recommended for some Linux environments
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize WebDriver with options
driver = webdriver.Chrome(options=options)

# URL of your Streamlit app
app_url = "https://castoma.streamlit.app"

try:
    # Open the app
    driver.get(app_url)

    # Wait for page to load
    time.sleep(20)  # Adjust as needed or use explicit waits

    try:
        # Try to find the "Yes, get this app back up" button by its text
        wake_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Yes, get this app back up!')]")

        # If found, click the button
        if wake_button.is_displayed():
            print("App is in sleep mode. Clicking wake-up button...")
            wake_button.click()
            # Wait for app to wake up
            time.sleep(20)  # Adjust based on your app's wake-up time
        else:
            print("Wake-up button not visible.")
    except NoSuchElementException:
        print("App is not in sleep mode or wake-up button not found.")

    # Continue with your automation here...

finally:
    # Close the browser when done
    driver.quit()
