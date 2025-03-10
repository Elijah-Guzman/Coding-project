import requests
from bs4 import BeautifulSoup

def scrape_job_data(job_url):
    try:
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Send request with headers
        response = requests.get(job_url, headers=headers)

        # Check if request was successful
        print(f"Status Code: {response.status_code}")

        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Print entire page source to debug
        print(soup.prettify())

    except Exception as e:
        print(f"Error scraping data: {e}")

# Example usage
job_url = 'https://www.onetonline.org/link/details/SPECIFIC_JOB_CODE'
job_skills = scrape_job_data(job_url)