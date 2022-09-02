from scrape_requirements import request_websites
from json import load
import pandas

def get_uci_samples():
    
    open_urls = open('../../other/program_Urls.json')
    all_urls = load(open_urls)

    for major, website in all_urls.items():
        soup = request_websites(website)
        table = soup.find('table', class_='sc_plangrid')
        if table:
            create_tables(table)


def create_tables(table):
    years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    quarters = ['FALL', 'WINTER', 'SPRING']
    


if __name__ == "__main__":
    get_uci_samples()