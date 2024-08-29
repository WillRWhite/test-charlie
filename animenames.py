import requests
import json
import time

def fetch_anime_titles(pages = 1084):
    all_titles = []
    for page in range(1, pages + 1):
        url = f"https://api.jikan.moe/v4/anime?page={page}"
        response = requests.get(url)
        time.sleep(0.8)
        if response.status_code == 200:
            data = response.json()
            titles = [anime['title'] for anime in data['data']]
            all_titles.extend(titles)
            print(f"Fetch sucesfull: {page}: {response.status_code}")
        else:
            print(f"Failed to fetch data {page}: {response.status_code}")
    return all_titles
    
def save_titles_to_file(titles, filename = "anime_titles.json"):
    with open(filename, "w") as file:
        json.dump(titles, file, indent = 4)


if __name__ == "__main__":
    titles = fetch_anime_titles()
    save_titles_to_file(titles)
    print(f"saved {len(titles)} titles to anime_titles.json")
    