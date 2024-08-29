import requests
import json
import time

def fetch_anime_details(pages=1):
    all_details = []
    for page in range(1, pages + 1):
        url = f"https://api.jikan.moe/v4/anime?page={page}"
        response = requests.get(url)
        time.sleep(1)
        if response.status_code == 200:
            data = response.json()
            anime_details = [{
                'title': anime['title'],
                'synopsis': anime['synopsis'],
                'rating': anime['score'],
                'similar_anime': [sim['name'] for sim in anime.get('related', {}).get('other', [])]
            } for anime in data['data']]
            all_details.extend(anime_details)
            print(f"Fetch sucesfull: {page}: {response.status_code}")
        else:
            print(f"Failed to fetch data {page}: {response.status_code}")
    return all_details

def save_details_to_file(details, filename="anime_details.json"):
    with open(filename, 'w') as file:
        json.dump(details, file, indent=4)

if __name__ == "__main__":
    details = fetch_anime_details(pages = 1086)
    save_details_to_file(details)
    print(f"Saved details of {len(details)} anime to anime_details.json")
