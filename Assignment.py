import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    search_postings_heading = None
    for li in soup.find_all('li', class_='navbar2-item'):
        if "Search Postings" in li.get_text(strip=True):
            search_postings_heading = li
            break

    if search_postings_heading:
        postings_list = None
        for sibling in search_postings_heading.find_next_siblings():
            if sibling.name == 'ul':
                postings_list = sibling
                break

        if postings_list:
            postings = postings_list.find_all('li')[:5]
            if postings:
                for posting in postings:
                    est_value_notes = posting.find('div', class_='est-value-notes')
                    description = posting.find('div', class_='description')
                    closing_date = posting.find('div', class_='closing-date')

                    est_value_notes_text = est_value_notes.get_text(strip=True) if est_value_notes else 'N/A'
                    description_text = description.get_text(strip=True) if description else 'N/A'
                    closing_date_text = closing_date.get_text(strip=True) if closing_date else 'N/A'

                    print(f"Est. Value Notes: {est_value_notes_text}")
                    print(f"Description: {description_text}")
                    print(f"Closing Date: {closing_date_text}")
                    print("-" * 50)
            else:
                print("No postings found.")
        else:
            print("No postings list found.")
    else:
        print("Search Postings heading not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
