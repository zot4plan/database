import requests
from bs4 import BeautifulSoup


def request_websites(url):
    """
    request_websites attains permission from the server - with the intend to scrape and turn
    the link into a Soup object
    """

    link = requests.get(url).text
    soup = BeautifulSoup(link, 'lxml')
    return soup


def get_requirements_websites():
    """
    get_requirements_websites scrapes all the redirected websites in the main page of UCI major requirements.
    return: a list of all the URL addresses that display UCI major requirements
    """

    major_urls = {}
    all_href = []
    soup = request_websites("http://catalogue.uci.edu/undergraduatedegrees/")
    for elem in soup.find_all('ul'):
        for each in elem.find_all('a'):
            href = each.get('href')
            get_type = href.split('_')
            website = 'http://catalogue.uci.edu/' + href
            name = each.text
            if get_type[-1] in ['minor/', 'bs/', 'ba/', 'bfa/'] and name not in major_urls:
                all_href.append([each.text, website])
                major_urls[name] = website

    # write_url(major_urls)
    return all_href


def get_courses_websites():
    """
    get_courses_websites scrapes all of the websites that can be redirected from the main UCI
    course website. 
    """

    all_websites = set()
    soup = request_websites("http://catalogue.uci.edu/allcourses/")
    for elem in soup.find_all('a'):
        get_href = elem.get('href')
        if '/allcourses' in str(get_href):
            all_websites.add('http://catalogue.uci.edu' + get_href)

    all_websites = [elem for elem in all_websites]
    return sorted(all_websites)[1:]