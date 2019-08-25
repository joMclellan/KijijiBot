#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:19:45 2019
@author: joshmclellan
"""
#imports
import random
#import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Getters
def getLogins():
    strArrLogin = []
    f = open('logins.txt','r')
    for strLine in f.readlines():
        strArrLogin.append(strLine + "\n")
    f.close()
    return strArrLogin

def getTitle():
    f = open('title.txt','r')
    strTitle = f.readline()
    f.close()
    return strTitle
        

def getAddress():
    f = open('address.txt','r')
    strAddress = f.readline()
    f.close()
    return strAddress


def getpost():
    f = open('post.txt','r')
    strPost = f.readline()
    f.close()
    return strPost

#functionality
def login(strArrLogin, browser):
    x = random.randint(0,len(strArrLogin)-1)
    strLogin = strArrLogin[x].split(":")
    strEmail = strLogin[0]
    strPass = strLogin[1]
    element = browser.find_element_by_id("login-password")
    element.send_keys(strPass)
    element = browser.find_element_by_id("LoginEmailOrNickname")
    element.send_keys(strEmail)
    element.submit()
    return

def postTitle(strTitle, browser):
    time.sleep(3)
    element = browser.find_element_by_id("AdTitleForm")
    element.send_keys(strTitle, Keys.ENTER)
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='suggestionsContainer-1610687866']//li[1]//button[1]").click()
    return   

def post(strAddress, strPost, browser):
    element = browser.find_element_by_id("pstad-descrptn")
    element.send_keys(strPost)
    element = browser.find_element_by_id("pstad-map-address")
    element.send_keys(strAddress)
    element.submit()
    browser.find_element_by_xpath("//div[@class='table-3406774831']//div[1]//div[2]//div[2]//button[1]").click()
    browser.find_element_by_xpath("//button[@name='saveAndCheckout']").click()
    return

def navigation():
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')
    browser.get("https://bit.ly/2MEfACe")
    return browser

def main():
    strArrLogin = getLogins()
    strTitle = getTitle()
    strAddress = getAddress()
    strPost = getpost()
    browser = navigation()
    login(strArrLogin, browser)
    postTitle(strTitle, browser)
    time.sleep(1)
    post(strAddress, strPost, browser)
    return

main()