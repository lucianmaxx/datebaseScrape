from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.fakenamegenerator.com')
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/users.txt', 'w') as users:

    for x in range(0, 50):
        sleep(2)
        fullName = driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3').text
        firstName = str(fullName).split(" ")[0]
        lastName = str(fullName).split(" ")[-1]
        emailAddress = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/' +
                                                        'div[2]/div/div[2]/dl[9]/dd').text).split('\n')[0]
        password = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[11]/dd').text)
        birthday = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[6]/dd').text)
        addressCity = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/div').text).split('\n')[-1].split(",")[0]

        gender = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[1]/div/div[1]/img').get_attribute('alt'))
        occupation = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[18]/dd').text)
        phone = str(driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd').text)

        users.write(str(firstName + '\t' + lastName + '\t' + emailAddress + '\t' + password + '\t' + birthday + '\t' +
                        addressCity + '\t' + gender + '\t' + occupation + '\t' + phone + '\n'))
        driver.find_element_by_xpath('//*[@id="genbtn"]').click()
    driver.close()
