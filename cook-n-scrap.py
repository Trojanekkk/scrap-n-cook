import random

import requests
from lxml import html

class Recipe:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return 'Twój szczęśliwy przepis to "' + self.name + '", znajdziesz go pod adresem ' + self.url

if __name__ == "__main__":
    recipes_arr = []

    url_root = "https://www.kwestiasmaku.com"
    url_library = "/przepisy?page="

    session_req = requests.session()

    i_range = range(0,100)
    for i in i_range:

        url = url_root + url_library + str(i)
        result = session_req.get(url)

        tree = html.fromstring(result.text)
        recipes = tree.xpath("//span[contains(@class, 'field-content')]/a/@href")

        print("Sprawdzono " + "{:10.0f}".format(100*(i-i_range[0])/(len(i_range))) + "%")

        for r in recipes:

            if '/przepis.html' in r:
                r_name = r.split('/')[-2].replace('-', ' ').replace('_', ' ').capitalize()
            
            else:
                r_name = r.split('/')[-1].replace('-', ' ').replace('_', ' ').capitalize()
            
            r_url = url_root + r
            recipe = Recipe(r_name, r_url)
            
            recipes_arr.append(recipe)

    print(random.choice(recipes_arr))
    
