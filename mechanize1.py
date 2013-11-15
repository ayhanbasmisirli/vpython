#! /usr/bin/python
import mechanize
def viewPage(url):
	browser=mechanize.Browser()
	page=browser.open(url)
	source_code=page.read()
	print source_code
#printing whatever url
viewPage("http://www.google.com")
#the most basic use of Mechanize: retrieving a website’s source code

