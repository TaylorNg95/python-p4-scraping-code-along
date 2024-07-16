from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:

    def __init__(self):
        self.courses = []

    def get_page(self):
        html = requests.get('https://learn-co-curriculum.github.io/site-for-scraping/courses')
        doc = BeautifulSoup(html.text, 'html.parser')
        return doc

    def get_courses(self):
        courses = self.get_page().select('.post')
        return courses

    def make_courses(self):
        courses = self.get_courses()
        for course in courses:
            title = course.select('h2')[0].text if course.select('h2') else ''
            schedule = course.select('.date')[0].text if course.select('.date') else ''
            description = course.select('p')[0].text if course.select('p') else ''
            new_course = Course(title=title, schedule=schedule, description=description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        courses = self.make_courses()
        for course in courses:
            print(course)

Scraper().print_courses()