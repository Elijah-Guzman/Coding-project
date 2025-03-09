import requests
from bs4 import BeautifulSoup

# First, install required libraries
# pip install requests beautifulsoup4

def scrape_job_data(job_url):
    try:
        # Send a request to the website
        response = requests.get(job_url)

        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract job skills
        skills_section = soup.find('div', class_='skills-section')

        # Extract specific job details
        job_skills = skills_section.find_all('li')

        # Process and store skills
        skills_list = [skill.text.strip() for skill in job_skills]

        return skills_list

    except Exception as e:
        print(f"Error scraping data: {e}")
        return []

# Example usage
job_url = 'https://www.onetonline.org/link/details/SPECIFIC_JOB_CODE'
job_skills = scrape_job_data(job_url)
print(job_skills)