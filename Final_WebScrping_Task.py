# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:04:27 2023

@author: Mediatec
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:27:05 2023

@author: Mediatec
"""
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
links_array= []
all_details = []
Names_array=[]
row_array=[]


driver=webdriver.Chrome("C:/Users/Mediatec/Documents/Downloads/chromedriver_win32 (2)/chromedriver.exe")
driver.get("https://search.lboro.ac.uk/s/search.html?collection=loughborough-courses")
all_details = []
for c in range(1,380,10):
        driver.get("https://search.lboro.ac.uk/s/search.html?collection=loughborough-courses&start_rank={}".format(c))
        print("https://search.lboro.ac.uk/s/search.html?collection=loughborough-courses&start_rank={}".format(c))
        program_name_elements = driver.find_elements(By.CLASS_NAME,'result__heading')
        for program_name_element in program_name_elements:
                   Names_array.append(program_name_element.text)
        #print(Names_array)
        links=driver.find_elements(By.CLASS_NAME,'result__link')
        for link in  links:
            links_array.append(link.get_property("href"))
for l in links_array:
            driver.get(url=l)
            
            program_type = driver.find_elements(By.CLASS_NAME,'site-header__title')
            if program_type[0].text=='Undergraduate study':
                program_type='Undergraduate study'
                program_duration = driver.find_elements(By.CLASS_NAME,'course-info__subheading')[0].text
                program_overview = driver.find_elements(By.CLASS_NAME,'text-overflow')[0].text
                program_requirements= driver.find_elements(By.CLASS_NAME,'entry-requirements__alerts')[0].text
                program_fees= driver.find_elements(By.CLASS_NAME,'course-fees-container')[0].text
            else:
                program_type='postgraduate study'
                program_duration='null'
                program_overview ='null'
                program_requirements=driver.find_elements(By.CLASS_NAME,'lead-paragraph--centred')[0].text
                program_fees=driver.find_elements(By.CLASS_NAME,'degree-fees-wrapper')[0].text
row_array = [
                 
        [Names_array[links_array.index(l)],
        program_type,
        program_overview,
        program_duration,
        program_requirements,
        program_fees]
    for l in links_array]
print(len(row_array))

            
            
            
df = pd.DataFrame(row_array, columns=['Proram Name','Program Type','Program OverView','Program Duration','Program Requirements','Program Fees'])

df.to_csv("H:/ITI_AI/Data Prep/Final_Data.csv", header=True, index=False)

time.sleep(3)
driver.close()