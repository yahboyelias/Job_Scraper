import requests
from bs4 import BeautifulSoup



# Get user input for job title and location
job_input = input("What job title are you looking for?: ")
location_input = input("Where?: ")

# Build the URL using user inputs
url = f"https://www.indeed.com/jobs?q={job_input}&l={location_input}&from=searchOnHP"

# Send a GET request to the constructed URL
pg_to_scrape = requests.get(url)

# Check if the request was successful
if pg_to_scrape.status_code == 200:
    # HTML Parser
    soup = BeautifulSoup(pg_to_scrape.text, "html.parser")

    # Find job listings
    job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    pg_to_scrape = requests.get(url, headers=headers)

    # Now you can parse and extract information from job_listings
    for job_listing in job_listings:
        # Extract job title and location
        job_title_element = job_listing.find("h2", class_="jobTitle")
        location_element = job_listing.find("div", class_="companyLocation")

        if job_title_element:
            job_title = job_title_element.get_text(strip=True)
        else:
            job_title = "N/A"

        if location_element:
            job_location = location_element.get_text(strip=True)
        else:
            job_location = "N/A"

        # You can print or store this information as needed
        print("Job Title:", job_title)
        print("Location:", job_location)
        print("\n")
else:
    print("Failed to fetch the page.")
