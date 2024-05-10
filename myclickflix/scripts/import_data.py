import pandas as pd 
from main.models import Movie, Actor, Category
import os 



def run_actor(country: str, b_year: int, num_year: int): 

    actor_df = pd.read_csv('../Data/Main_data/' + country + '_actor_id' + str(b_year) + 'done.csv')

    for i in range(b_year + 1, b_year + num_year): 
        actor_df = pd.concat([actor_df, pd.read_csv('../Data/Main_data/' + country + '_actor_id' +str(i) + 'done.csv')])

    actor_df = actor_df.drop_duplicates('id')
    actor_df = actor_df.dropna()
    actor_df = actor_df.drop(['Unnamed: 0'], axis = 1)

    for index, row in actor_df.iterrows(): 

        if not Actor.objects.filter(pk = row['id']).exists(): 
            actor = Actor(name = row['name'], birthday = row['birthday'], bio = row['bio'], image = row['image'], pk = row['id'])
            actor.save()


    print('Done!')



def run(): 
    run_actor('American', 1980, 10)