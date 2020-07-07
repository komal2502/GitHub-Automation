
# Setup
#--------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Invoke chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# Navigate to Github login page
driver.get("https://github.com/login?return_to=%2FGithub")
driver.maximize_window()

# Pass the login details and login
driver.find_element_by_id("login_field").send_keys("komal2502")
driver.find_element_by_id("password").send_keys("Shanu!12345678")
driver.find_element_by_name("commit").click()

# Explicit wait
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"dropdown-caret")))
driver.find_element_by_class_name("dropdown-caret").click()

# Challenge 1 - Repository Creation
#---------------------------------------------------------------------------------------------------------------
# Select New repository link
driver.find_element_by_link_text("New repository").click()

# Create new Repo
driver.find_element_by_id("repository_name").send_keys("Demo_Repository_1")
driver.find_element_by_id("repository_description").send_keys("Automate the creation of a repository on Github")
driver.find_element_by_xpath("//button[@type='submit' and @data-disable-with='Creating repository…']").click()

#Challenge 2 - Issue Creation
#------------------------------------------------------------------------------------------------------
#Create new issue
driver.find_element_by_xpath("//span[@data-content='Issues']").click()
driver.find_element_by_xpath("//span[@class='d-none d-md-block']").click()
driver.find_element_by_id("issue_title").send_keys("issue1")
driver.find_element_by_id("issue_body").send_keys("issue1 description")
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

# Create another issue
driver.find_element_by_xpath("//a[@class='btn btn-sm btn-primary m-0 ml-0 ml-md-2']").click()
driver.find_element_by_id("issue_title").send_keys("issue2")
driver.find_element_by_id("issue_body").send_keys("issue2 description and referring to issue1 #1")
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

# Challenge 3 - Comment to an issue
#----------------------------------------------------------------------------------------------------
# Adding comment to the issue created in challenge 2
driver.find_element_by_id("new_comment_field").send_keys("Adding comment to the issue2 created in Challenge 2")
driver.find_element_by_xpath("//div[@class='bg-gray-light ml-1']/button[@class='btn btn-primary']").click()

# Adding Emoji in Issue 1
driver.find_element_by_link_text("#1").click()
driver.find_element_by_xpath("//summary[@class='btn-link link-gray timeline-comment-action']/*[local-name()='svg']").click()
driver.find_element_by_xpath("//button[@value='THUMBS_UP react']/g-emoji[@alias='+1']").click()


# Challenge 4 - Issue mention in comments to issue
#------------------------------------------------------------------------------------------------------
# Create a new comment and mention any of the previous issue
driver.find_element_by_id("new_comment_field").send_keys("Creating a new comment and mentioning issue 2 from challenge 2 #2")
driver.find_element_by_xpath("//div[@class='bg-gray-light ml-1']/button[@class='btn btn-primary']").click()

# Navigate to the issue from the comment.
driver.find_element_by_partial_link_text("#2").click()

# Challenge 5 - Delete Repository
#-------------------------------------------------------------------------------------------------------
# Go to settings
driver.find_element_by_xpath("//span[@data-content='Settings']").click()

# Wait for the page to open
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//details[@class='details-reset details-overlay details-overlay-dark']/summary[@class='btn btn-danger boxed-action']")))

# Delete the Repo
driver.find_element_by_xpath("//details[@class='details-reset details-overlay details-overlay-dark']/summary[@class='btn btn-danger boxed-action']").click()
driver.find_element_by_xpath("//div[@class='Box-body overflow-auto']/form/p/input[@type='text' and @class='form-control input-block']").send_keys("komal2502/Demo_Repository_1")
driver.find_element_by_xpath("//div[@class='Box-body overflow-auto']/form/button[@type='submit' and @class='btn btn-block btn-danger']").click()



