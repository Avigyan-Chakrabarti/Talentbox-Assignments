import streamlit as st
import requests
from bs4 import BeautifulSoup
import actor_id as aid

def get_actor_filmography(actor_name):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    actor_imdb_id = aid.get_imdb_id(actor_name)
    actor_url = f"https://www.imdb.com/name/{actor_imdb_id}/filmotype"

    actor_response = requests.get(actor_url,headers=head)
    actor_soup = BeautifulSoup(actor_response.text, 'html.parser')
    filmography_section = actor_soup.find("div", id="filmography")

    filmography = {}
    actor_category = []
    for category in filmography_section.find_all("div", class_="head"):
        actor_category.append(category.a.text.strip())
    i = 0
    for category in filmography_section.find_all("div",class_="filmo-category-section"):
            category_name = actor_category[i]
            filmography[category_name] = []
            for item in category.find_all("div",class_="filmo-row"):
                film_title = item.b.a.text.strip()
                film_year = item.span.text.strip()
                filmography[category_name].append((film_title, film_year))
            i+=1
    return filmography

def print_filmography(actor_name, filmography):
    st.write(f"\nFilmography for {actor_name.replace('+',' ')} in descending order:")
    for category,films in filmography.items():
        st.write(f"\n{category}:")
        for film, year in films:
            st.write(f"{film} ({year})")

if __name__ == "__main__":
    st.title("Actor Filmography Viewer")
    actor_name = st.text_input("Enter the name of the actor:")
    if actor_name:
        actor_name = actor_name.lower().replace(' ','+')
        filmography = get_actor_filmography(actor_name)
        print_filmography(actor_name, filmography)