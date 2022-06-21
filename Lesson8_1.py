import requests 
import json
from operator import itemgetter


url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
heroes_list = resp.json()
with open ('C:\TEST\lesson9.json', 'w') as f:
    json.dump(resp.json(), f, ensure_ascii=False, indent=2) # для удобства и визуализации данных

heroes = ['Hulk', 'Captain America', 'Thanos'] # список героев

def intelligence_sort(heroes=heroes):
    intelligence_dict = {}
    for hero in heroes:
        for el in heroes_list:      
            if el['name'] == hero:
                intelligence_dict[hero] = el['powerstats']['intelligence']

    res_ = sorted(intelligence_dict.items(), key=itemgetter(1), reverse=True)
    print(f'Самый умный герой - {res_[0][0]} с интеллектом {res_[0][1]}')
    return res_[0][0]

if __name__ == '__main__':
    intelligence_sort(heroes)


