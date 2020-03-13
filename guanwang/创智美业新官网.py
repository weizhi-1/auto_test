# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标悬停模块
driver = WebChrome()#打开浏览器
# driver.implicitly_wait(10)


auto_setup(__file__)
driver.get("http://createwit.com/")#进入创智美业官网
time.sleep(2)
driver.maximize_window()#浏览器窗口最大化
tag_element = driver.find_element_by_xpath("//a[@href='product.html']")#定位该元素
ActionChains(driver).move_to_element(tag_element).perform()#鼠标悬停到该元素
driver.find_element_by_link_text("ERP").click()#点击该元素
driver.assert_template(Template(r"tpl1583921002974.png", record_pos=(5.87, 1.895), resolution=(100, 100)), "是否定位至erp")
driver.find_element_by_xpath("//img[@src='images/product/js_1.png']").click()
driver.assert_template(Template(r"tpl1583921034507.png", record_pos=(7.63, 2.285), resolution=(100, 100)), "是否定位至讲师")
js="window.scrollTo(0,document.body.scrollHeight)" 
driver.execute_script(js)#页面滑动至最底部
time.sleep(1)
driver.assert_template(Template(r"tpl1583919799081.png", record_pos=(4.455, 7.99), resolution=(100, 100)), "验证是否滑动至最底部")
driver.find_element_by_xpath("//a[@href='about.html']").click()
driver.assert_template(Template(r"tpl1583918269179.png", record_pos=(3.38, 4.15), resolution=(100, 100)), "是否跳转至关于我们页面")
driver.find_element_by_xpath("//a[@href='download.html']").click()
driver.assert_template(Template(r"tpl1583918305017.png", record_pos=(3.245, 5.25), resolution=(100, 100)), "是否跳转至下载专区页面")
# driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[3]/a").click()
driver.find_element_by_xpath("//a[@href='#']").click()
driver.find_element_by_id("companyText").send_keys("看一下")
driver.find_element_by_xpath("//input[@placeholder='手机号:']").send_keys("13411111111")
driver.find_element_by_xpath("//input[@placeholder='验证码:']").send_keys("1023")
driver.find_element_by_xpath("//textarea[@placeholder='留言:']").send_keys("6666666")
driver.find_element_by_xpath("//div[@onclick='doSubmit()']").click()

time.sleep(4)
driver.quit()










