# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:40:44 2022

@author: olavg

Sources:
    manga
        https://onepiecechapters.com/mangas/5/one-piece from translation group 'TCB scans'
    beautiful soup
        https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_all#searching-the-tree
    image to pdf
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

"""


import requests
from bs4 import BeautifulSoup as bs
from fpdf import FPDF
from PIL import Image
from io import BytesIO
from math import ceil

#Define the website
website_url = 'https://onepiecechapters.com'
manga_url_extension = '/mangas/5/one-piece'

#Get html and parse it for url to chapter
manga_request = requests.get(website_url + manga_url_extension)
manga_soup = bs(manga_request.content, 'html.parser')

#Find all elements 'a' that have a chapter
chapter_elements = manga_soup.body.main.find_all('a')

#Get link to the latest chapter
chapter_url_extension=chapter_elements[0].get('href')
        
#Get chapter html and parse it for the manga pages
chapter_request = requests.get(website_url+chapter_url_extension)
chapter_soup = bs(chapter_request.content, 'html.parser')
manga_page_elements = chapter_soup.body.main.find_all('picture')


#Get the string of the page link, make the string a list, then extend the manga_page_links list with the manga page link
manga_page_links = []
for element in manga_page_elements:
    manga_page_links.extend([element.img.get('src')])

#Create pdf: Get the image, save it, add it to the pdf
manga_pdf = FPDF()
for page_link in manga_page_links:
    img_name = page_link.split("/")[-1]
    img_to_save = requests.get(page_link).content #get the image in bytes
    img_obj = Image.open(BytesIO(img_to_save)) #make PIL image from file object from bytes
    img_obj_gray = img_obj.convert('L')

    width, height = img_obj_gray.size
    if width > height*1.20:
        left_page = img_obj_gray.crop((0,0,ceil(width/2),height))
        right_page = img_obj_gray.crop((ceil(width/2),0,width,height))
        manga_pdf.add_page()
        manga_pdf.image(right_page,0,0,210,297)
        manga_pdf.add_page()        
        manga_pdf.image(left_page,0,0,210,297)
    else:        
        manga_pdf.add_page()
        manga_pdf.image(img_obj_gray,0,0,210,297)
chapter_title = chapter_soup.find('title').text
manga_pdf.output(chapter_title[:-11] + ".pdf", "F")

#Next step: Fix and add functions to test_emailer
#Next step2: add code to send to kindle
#Next step3: add code to execute once a day 
#Next step4: how to run script every day on RPi?

