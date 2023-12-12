import requests
from bs4 import BeautifulSoup
import pandas as pd

class GunViolenceDataCollector:
    """
    A class to systematically scrape and compile gun violence data from a specified website.

    The GunViolenceDataCollector class is designed to navigate through a website dedicated to reporting gun violence incidents. It leverages the BeautifulSoup library to parse HTML content and the pandas library to structure the extracted data. The class can process multiple years of data, handling website pagination to ensure comprehensive data collection.

    Attributes:
        base_url (str): The root URL of the website from where the data will be scraped.
        session (requests.Session): An instance of requests.Session to manage web requests, maintaining consistent headers and cookies.

    Methods:
        fetch_soup(url: str) -> BeautifulSoup:
            Sends a GET request to the given URL, handles response errors, and returns a BeautifulSoup object for HTML parsing.

        get_last_page_number(url: str) -> int:
            Identifies and returns the number of the last page of data for a specific year, aiding in pagination handling.

        collect_pagination_urls(year: int) -> List[str]:
            Generates a list of all URLs corresponding to the paginated data for a given year.

        scrape_data(year: int) -> pd.DataFrame:
            Extracts gun violence data for the specified year, parses it, and returns it as a pandas DataFrame. The data includes incident details and relevant hyperlinks.

        collect_data_for_years(start_year: int, end_year: int) -> pd.DataFrame:
            Aggregates gun violence data across a range of years into a consolidated pandas DataFrame. Each year's data is scraped and appended to form a comprehensive dataset.
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_soup(self, url):
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')

    def get_last_page_number(self, url):
        soup = self.fetch_soup(url)
        last_page_link = soup.find('li', class_='pager-last').find('a')['href']
        last_page_number = int(last_page_link.split('page=')[-1].split('&')[0])
        return last_page_number

    def collect_pagination_urls(self, year):
        url = f'{self.base_url}/reports/total-number-of-incidents?year={year}'
        last_page_number = self.get_last_page_number(url)
        return [f"{self.base_url}/reports/total-number-of-incidents?page={i}&year={year}" for i in range(last_page_number + 1)]

    def scrape_data(self, year):
        all_data = []
        pagination_urls = self.collect_pagination_urls(year)
        for url in pagination_urls:
            soup = self.fetch_soup(url)
            table = soup.find('table', {'class': 'responsive'})
            headers = [header.text.strip() for header in table.find_all('th')]
            headers.extend(['View Incident Link', 'View Source Link'])

            for row in table.find_all('tr'):
                cols = row.find_all('td')
                if cols:
                    row_data = [ele.text.strip() for ele in cols]
                    links = row.find_all('a', href=True)
                    incident_link = next((link['href'] for link in links if 'View Incident' in link.text), None)
                    source_link = next((link['href'] for link in links if 'View Source' in link.text), None)
                    row_data.extend([incident_link, source_link])
                    all_data.append(row_data)

        df = pd.DataFrame(all_data, columns=headers)
        df.drop(columns=['Operations'], inplace=True)
        df['View Incident Link'] = df['View Incident Link'].apply(lambda x: self.base_url + x if x else None)
        return df

    def collect_data_for_years(self, start_year, end_year):
        all_years_df = pd.DataFrame()
        for year in range(start_year, end_year + 1):
            year_df = self.scrape_data(year)
            all_years_df = pd.concat([all_years_df, year_df])
        return all_years_df



