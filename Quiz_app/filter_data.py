import requests
import random

def get_data(limit=3, category='', diffoculty='easy', type_a='multiple'):
    
    d={'Multiple Choice':'multiple','True&False':'boolean'}
            
    diffoculty=diffoculty.lower()
    type_a=d[type_a]
    cat = {'any category': "any",
           "General Knowledge": 9,
           "Entertainment Books": 10,
           "Entertainment Film": 11,
           "Entertainment Music": 12,
           "Entertainment Musicals & Theatres": 13,
           "Entertainment Television": 14,
           "Entertainment Video Games": 15,
           "Entertainment Board Games": 16,
           "Science & Nature": 17,
           "Science Computers": 18,
           "Science Mathematics": 19,
           "Mythology": 20,
           "Sports": 21,
           "Geography": 22,
           "History": 23,
           "Politics": 24,
           "Art": 25,
           "Celebrities": 26,
           "Animals": 27,
           "Vehicles": 28,
           "Entertainment: Comics": 29,
           "Science Gadgets": 30,
           "Entertainment Japanese Anime & Manga": 31,
           "Entertainment Cartoon & Animations": 32,
           }
    for i in cat.keys():
        if i == category:
            category = cat[i]
            break
    if category == '':
        category = random.randint(9, 32)

    try:
        # print(limit,category,diffoculty,type_a,'\n======================================================')
        url = f'https://opentdb.com/api.php?amount={limit}&category={category}&difficulty={diffoculty}&type={type_a}'
        response = requests.request("GET", url)
        return response.json()
    except Exception as e:
        return e

# This part will execute the function when this file is imported
if __name__ == "__main__":
    print(get_data(limit=3, category='', diffoculty='easy', type='multiple'))
