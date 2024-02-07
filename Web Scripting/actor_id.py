import requests
from bs4 import BeautifulSoup

def get_imdb_id(actor_name):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    search_url = f"https://www.imdb.com/find?q={actor_name}&s=nm"

    response = requests.get(search_url, headers= head)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('li', class_='ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-name-result')

    if result:
        href = result.find('a')['href']
        imdb_id = href.split('/')[2]
        return imdb_id
    else:
        return None

if __name__=="__main__":
    actor_name = input("Enter the name of the actor: ").lower().replace(" ", "+")
    imdb_id = get_imdb_id(actor_name)
    if imdb_id:
        print(f"IMDb ID for {actor_name.replace('+', ' ')} is {imdb_id}")
    else:
        print(f"No IMDb ID found for {actor_name.replace('+', ' ')}")
