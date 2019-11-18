#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:11:56 2019

@author: inabahu
"""
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


user=input('Please input your student number:')
pwd=input('Please input your account password:')
driver = webdriver.Firefox()
driver.get("http://219.243.47.181:8080")
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_name("submit").click()

driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"辐射防护")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[3]").click()
driver.find_element_by_link_text(u"浏览模式").click()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"辐射防护")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[3]").click()
driver.find_element_by_link_text(u"浏览模式").click()
#driver.find_element_by_partial_link_text("")
time.sleep(2)
dict1=list()

f = open('1.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(187):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict1.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict1:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('1a.txt','w')
f1.write(''.join(t))
f1.close()


time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"化学危险品")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[4]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict2=list()

f = open('2.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(625):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict2.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict2:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('2a.txt','w')
f1.write(''.join(t))
f1.close()



time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"机械类")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[5]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict3=list()

f = open('3.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(331):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict3.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict3:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('3a.txt','w')
f1.write(''.join(t))
f1.close()


time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"生物医学")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[6]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict4=list()

f = open('4.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(203):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict4.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict4:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('4a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"实验室安全")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[7]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict5=list()

f = open('5.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(161):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict5.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict5:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('5a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"土木工程")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[8]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict6=list()

f = open('6.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(32):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict6.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict6:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('6a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"消防安全")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[9]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict7=list()

f = open('7.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(76):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict7.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict7:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('7a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"新生安全")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[10]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict8=list()

f = open('8.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(68):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict8.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict8:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('8a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"用电安全")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[11]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict9=list()

f = open('9.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(196):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict9.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict9:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('9a.txt','w')
f1.write(''.join(t))
f1.close()




time.sleep(2)
driver.back()
driver.find_element_by_link_text(u"自学").click()
driver.find_element_by_id("knowid").click()
Select(driver.find_element_by_id("knowid")).select_by_visible_text(u"治安防范")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='使用学校题库进行自学：'])[1]/following::option[12]").click()
driver.find_element_by_link_text(u"浏览模式").click()
time.sleep(2)
dict10=list()

f = open('10.txt')
T=f.read()
f.close()
t=T.split("正确答案")
for n in range(9):
    url="da_"+str(n)
    driver.find_element_by_id(url).click()
    url2="an_"+str(n)
    a=driver.find_element_by_id(url2).text
    dict10.append(a)
    #dict=[dict a]
#print(dict1)
i=0
for a in dict10:
   t[i]=t[i]+'正确答案:'+a
   i+=1
#T.replace(str(n+1))
f1 = open('10a.txt','w')
f1.write(''.join(t))
f1.close()


dict_sum=list()
for i in range(10):
    num=str(i+1)
    f = open(num+'a.txt')
    T=f.read()
    dict_sum.append(T)
    f.close()
    
f1 = open('安全知识题库.txt','w')
f1.write(''.join(dict_sum))
f1.close()