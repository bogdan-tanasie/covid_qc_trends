7# -*- coding: utf-8 -*-
"""
Spyder Editor

Bogdan Tanasie
"""

# Basic imports and settings
import pandas as pd
from pytrends.request import TrendReq

import csv
import numpy as np
import time

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', None)

pytrends = TrendReq(hl='en-US', tz=360)

# Set time and location
timeframe = '2020-01-01 2020-05-14'
geo = 'CA-QC'

#############################################

print('1 wedding')
keywords = ['engagement ring', 'wedding dress', 'groom', 'wedding anniversary', 'bridal shower', 'bride', 'cash', 'wedding invitation', 'wedding venue', 'engagement']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('wedding.csv', mode='a', header=True)

#############################################
#############################################

print('2 political parties')
keywords = ['Libertarian', 'Bloc Quebecois', 'PQ', 'PPC' , 'Quebec Solidaire', 'CAQ', 'Conservative Party', 'Green Party', 'Liberal Party', 'NDP']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('political_parties.csv', mode='a', header=True)

#############################################
#############################################

print('3 dating')
keywords = ['Dating apps', 'tinder', 'bumble', 'happn', 'Hinge', 'online dating', 'Facebook dating', 'coffee meets bagel', 'sugar daddy', 'OKCupid']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('dating.csv', mode='a', header=True)

#############################################
#############################################

print('4 software')
keywords = ['Photoshop', 'Adobe', 'winrar', 'Java', 'vlc	', 'avast', 'filehippo', 'SAP', 'Shopify	', 'Zoom']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('software.csv', mode='a', header=True)

#############################################
#############################################

print('5 fast food restaurants')
keywords = ["McDonald's", 'KFC', 'Pizza hut', 'Burger king', "Wendy's", 'A&W', 'St-Hubert', 'Subway', "Domino's", 'Taco Bell']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('fast_food_restaurants.csv', mode='a', header=True)

#############################################
#############################################

print('6 STIs')
keywords = ['Chlamydia', 'HIV', 'Herpes', 'Gonorrhea', 'HPV', 'Hepatitis B', 'Syphilis', 'STI', 'STD', 'Hepatitis A']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('stis.csv', mode='a', header=True)

#############################################
#############################################

print('7 makeup')
keywords = ['Sephora', 'M.A.C', 'Eyeliner', 'Glossier', 	"L'Oreal", 'Eyeshadow', 'Mascara	', 'Makeup', 'Eyebrow', 'Makeup artist']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('makeup.csv', mode='a', header=True)

#############################################
#############################################

print('8 hotel')
keywords = ['expedia', 'hotels.com', 'Airbnb', 'Flighthub', 'hotel', 'Trivago', 'marriott', 'hostel', 'hotel booking', 'couchsurfing']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('hotel.csv', mode='a', header=True)

#############################################
#############################################


# Bahamas trip does not seem to work
print('9 travel')
keywords = ['Cruise', 'airplane tickets', 'road trip', 'beach vacations', 'retreats', 'Resort', 'Bahamas', 'Camping', 'World tour', 'Bike trip']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('travel.csv', mode='a', header=True)

#############################################
#############################################

print('10 cars')
keywords = ['BMW', 'sell car', 'Car rental', 'Used Cars', 'auto trader', 'toyota	', 'electric car', 'Mercedes Benz', 'Tesla', 'car dealership']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('cars.csv', mode='a', header=True)

#############################################
#############################################

print('11 recipies')
keywords = ['sushi', 'indian food', 'mexican food', 'asian food', 'vegetarian recipes', 'vegan', 'Easy recipes', 'Chicken recipes', 'Healthy recipes', 'fine dining']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('recipies.csv', mode='a', header=True)

#############################################
#############################################

print('12 caffeine')
keywords = ['Starbucks', 'Tim Hortons', 'tea', 'coffee', 'nespresso', 'cappuccino ', 'iced coffee', 'red bull', 'instant coffee', 'espresso']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('caffeine.csv', mode='a', header=True)

#############################################
#############################################

print('13 politicians/personalities')
keywords = ['Justin Trudeau', 'Celine Dion', 'Ryan Renolds', 'Doug Ford', 'Francois Legault ', 'Valerie Plante', 'Donald Trump', 'Joe Biden', 'Pierre Arcand', 'Horacio Arruda']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('politicians_personalities.csv', mode='a', header=True)

#############################################
#############################################

print('14 pets')
keywords = ['cat', 'dog', 'cat coronavirus', 'dog coronavirus', 'adopt a cat', 'adopt a dog', 'adopt a pet', 'adopt a puppy', 'Humane society', 'spca']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pets.csv', mode='a', header=True)

#############################################
#############################################

print('15 gardening')
keywords = ['Seeds', 'garden', 'planting', 'fertilizer', 'plants', 'indoor plants', 'outdoor plants', 'soil', 'gardening	', 'seeds']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('gardening.csv', mode='a', header=True)

#############################################
#############################################

print('16 health')
keywords = ['blood pressure', 'hospitals near', 'Dry Cough', 'Cancer symptoms', 'coronavirus symptoms', 'sore throat', 'HIV', 'health insurance', 'ambulance', 'fever']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('health.csv', mode='a', header=True)

#############################################
#############################################

print('17 jobs')
keywords = ['indeed', 'layoff', 'linkedin', 'jobless', 'Internship', 'placement', 'EI', 'employment insurance', 'laid off', 'unemployment']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('jobs.csv', mode='a', header=True)

#############################################
#############################################

print('18 environment')
keywords = ['solar energy', 'climate change', 'Global warming', 'pollution', 'Greta', 'Recycling	', 'Waste', 'sustainability' , 'us epa', 'covid pollution']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('environment.csv', mode='a', header=True)

#############################################
#############################################

print('19 skin care')
keywords = ['Facial mask', 'Dry Skin', 'kylie skin', 'lumin skin', 'best skin care', 'Toners', 'hand moisturizer', 'dry hands', 'pimples', 'men skin care']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('skin_care.csv', mode='a', header=True)

#############################################
#############################################

print('20 finance')
keywords = ['loan', 'mortgage loan', 'dow jones', 'mortgage', 'interest rate', 'savings', 'debt', 'bonds', 'stock market	', 'mutual funds']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('finance.csv', mode='a', header=True)

#############################################
#############################################

print('21 home_issues')
keywords = ['daycare', 'Homeschooling', 'child abuse', 'domestic violence', 'divorce', 'separation', 'home issues', 'custody', 'pregnant', 'condom']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('home_issues.csv', mode='a', header=True)

#############################################
#############################################

print('22 activities')
keywords = ['theatre', 'cinema', 'clubs', 'bars', 'restaurants', 'massage', 'spa	', 'cooking', 'hiking', 'Cabane a sucre']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('activities.csv', mode='a', header=True)

#############################################
#############################################

print('23 music')
keywords = ['rap', 'rock', 'jazz	', 'blues', 'country', 'heavy metal', 'hip hop', 'classical music', 'bob marley', 'beatles']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('music.csv', mode='a', header=True)

#############################################
#############################################

print('24 food')
keywords = ['ice cream', 'cake', 'poutine', 'hamburger', 'hot dog', 'pizza', 'chips', 'fries', 'sandwich', 'cheese']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('food.csv', mode='a', header=True)

#############################################
#############################################

print('25 sports teams/leagues')
keywords = ['Habs', 'Montreal Impact', 'MLS', 'NBA', 'Stanley Cup', 'NHL	', 'CFL', 'curling', 'Cycling', 'MMA']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('sports_teams_leagues.csv', mode='a', header=True)

#############################################
#############################################

print('26 movie genre')
keywords = ['Comedy', 'romantic', 'thriller', 'Science Fiction', 'horror', 'documentary', 'adventure', 'mystery', 'drama	', 'action']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('movie_genre.csv', mode='a', header=True)

#############################################
#############################################

print('27 computers')
keywords = ['laptop', 'tablet', 'ipad', 'iphone', 'macbook', 'ssd', 'microsoft', 'zoom', '5G', 'gaming pc']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe,geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('computers.csv', mode='a', header=True)

#############################################
#############################################

print('28 relationship')
keywords = ['relationship', 'cheating', 'condom', 'sexting', 'frequentation', 'mating', 'marriage', 'jealous', 'long distance', 'breakup']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('relationship.csv', mode='a', header=True)

#############################################
#############################################

print('29 education')
keywords = ['Medical school', 'McGill', 'student loan', 'HEC Montreal', 'Law School', 'student jobs', 'cegep', 'UQAM', 'concordia', 'UdeM']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('education.csv', mode='a', header=True)

#############################################
#############################################

print('30 housing')
keywords = ['remax', 'DuProprio', 'kijiji', 'centris', 'zumper', 'realtor', 'real estate agent', 'mortgage', 'Royal Lepage', 'Sutton']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('housing.csv', mode='a', header=True)

#############################################
#############################################

print('31 news')
keywords = ['CBC', 'ctv ', 'fox news', 'cnn', 'La Presse', 'global news', 'City News', 'TVA nouvelles', 'MTL Blog', 'montreal gazette']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('news.csv', mode='a', header=True)

#############################################
#############################################

print('32 pharmaceutical')
keywords = ['advil', 'tylenol', 'Jean Coutu', 'Uniprix', 'hydroxychloroquine', 'pharmacy	', 'pharmaprix', 'familiprix', 'remdesivir', 'vaccine']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pharmaceutical.csv', mode='a', header=True)

#############################################
#############################################

print('33 transportation')
keywords = ['Orange line', 'Green line', 'yellow line', 'blue line', 'STM', 'uber', 'taxi', 'cab	', 'bus', 'Bixi']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo='CA-QC', gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('transportation.csv', mode='a', header=True)

#############################################
#############################################

print('34 clothing_stores')
keywords = ['banana republic', 'old navy	', 'gap', 'Holt Renfrew', 'Harry Rosen', 'H&M', 'Zara', 'Neon', 'Winners', 'forever 21']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('clothing_stores.csv', mode='a', header=True)

#############################################
#############################################

print('35 social_media')
keywords = ['facebook', 'instagram', 'snapchat', 'twitter', 'wechat', 'whatsapp', 'skype', 'tik tok', 'Tumblr', 'Pinterest']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('social_media.csv', mode='a', header=True)

#############################################
#############################################

print('36 arts & entertainment')
keywords = ['netflix', 'crave', 'disney+	', 'spotify', 'audible', 'prime video', 'hulu', 'Hbo', 'Apple TV	', 'Apple Music']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('arts_entertainment.csv', mode='a', header=True)

#############################################
#############################################

print('37 jewelry')
keywords = ['jewelry', 'diamond ring', 'earrings', 'bracelet', 'watch', 'pandora', 'tiffany & co	', 'swarovski', 'piercing', 'ring']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('jewelry.csv', mode='a', header=True)

#############################################
#############################################

print('38 illnesses')
keywords = ['Allergies', 'Flu', 'Diarrhea', 'Headache', 'Stomach Ache', 'anorexia', 'vomiting', 'asthma', 'Bronchitis', 'back pain']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('illnesses.csv', mode='a', header=True)

#############################################
#############################################

print('39 sports')
keywords = ['soccer', 'football', 'basketball', 'swimming', 'hockey', 'golf', 'UFC', 'Ski', 'Snowboard', 'tennis']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('sports.csv', mode='a', header=True)


#############################################
#############################################

print('40 diet')
keywords = ['blue zone diet', 'diet', 'atkins diet', 'dash diet', 'keto diet', 'weight loss', 'low carb diet', 'raw vegan', 'carnivore diet', 'plant based diet']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('diet.csv', mode='a', header=True)

#############################################
#############################################

print('41 charity')
keywords = ['charity', 'donate', 'food bank', 'charities	', 'World Vision', 'Red Cross', 'Doctors Without Borders', 'blood donation', 'donation', 'thrift store']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('charity.csv', mode='a', header=True)

#############################################
#############################################

print('42 learning')
keywords = ['learn french', 'duolingo', 'TED', 'khan academy', 'goodreads', 'translate', 'lessons', 'classes', 'online classes', 'summer courses']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('learning.csv', mode='a', header=True)

#############################################
#############################################

print('43 hairstyle')
keywords = ['bangs', 'hairstyle', 'haircut', 'beard', 'mullet', 'moustache', 'shave', 'buzz cut', 'afro', 'shave']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('hairstyle.csv', mode='a', header=True)

#############################################
#############################################

print('44 games')
keywords = ['board games', 'minecraft', 'piccolo', 'miniclip', 'online games', 'xbox', 'world of warcraft', 'Nintendo Switch', 'PlayStation', 'risk']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('games.csv', mode='a', header=True)

#############################################
#############################################

print('45 delivery')
keywords = ['uber eats', 'foodora', 'fedex', 'amazon prime', 'Cookit', 'Lufa', 'iga delivery', 'walmart delivery	', 'provigo delivery', 'metro delivery']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('delivery.csv', mode='a', header=True)

#############################################
#############################################

print('46 gambling')
keywords = ['poker', 'sports betting', 'casino', 'online casino', 'bet365', 'primedice', 'betting', 'flashscore', 'blackjack', 'Vegas Casino Online']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('gambling.csv', mode='a', header=True)

#############################################
#############################################

print('47 death')
keywords = ['funeral', 'death', 'coffin', 'dead', 'cremation', 'funeral', 'heaven', 'murder', 'hell', 'soul']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('death.csv', mode='a', header=True)

#############################################
#############################################

print('48 porn')
keywords = ['bdsm porn', 'porn', 'redtube', 'youporn', 'pornhub', 'lesbian porn', 'sex', 'chaturbate', 'hentai', 'gay porn']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('porn.csv', mode='a', header=True)

#############################################
#############################################

print('49 feelings')
keywords = ['Happy', 'anxiety', 'angry', 'sad', 'depression', 'horny', 'lonely', 'bored', 'Worried', 'in love']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('feelings.csv', mode='a', header=True)

#############################################
#############################################

print('50 retail')
keywords = ['walmart', 'ikea', 'target', 'home depot', 'costco', 'amazon	', 'couche tard', 'IGA', 'best buy', 'metro']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('retail.csv', mode='a', header=True)

#############################################
#############################################

print('51 retail 2')
keywords = ['Simons', 'Canadian tire', 'La baie', 'Home hardware	', 'Old Navy', 'Sears', 'Aldo', 'Dollarama', 'Structube', 'Reitmans']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('retail_2.csv', mode='a', header=True)

#############################################
#############################################

print('52 banks')
keywords = ['Bank of Montreal', 'Desjardins', 'Laurentian Bank', 'TD', 'CIBC', 'RBC', 'HSBC', 'Banque Nationale', 'BMO', 'bitcoin']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('banks.csv', mode='a', header=True)

#############################################
#############################################

print('53 alcohol')
keywords = ['Beer', 'Wine', 'spirits', 'cocktails', 'Cider', 'Corona Beer', 'Coors', 'rum', 'drunk', 'alcoholic']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('alcohol.csv', mode='a', header=True)

#############################################
#############################################

print('54 marijuana/drugs')
keywords = ['SQDC', 'Marijuana', 'weed', 'indica	', 'sativa', 'CBD', 'hash', 'cannabis', 'edibles	', 'THC']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('marijuana_drugs.csv', mode='a', header=True)

#############################################
#############################################

print('55 mental health')
keywords = ['anxiety', 'depression', 'meditation	', 'psychotherapy', 'online therapy', 'mental health clinic', 'social anxiety', 'telehealth', 'ADHD', 'insomnia']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('mental_health.csv', mode='a', header=True)

#############################################
#############################################

print('56 office supplies')
keywords = ['staples', 'pens', 'Envelopes', 'scissors', 'stapler	', 'quill', 'calculator', 'printer', 'printer ink', 'glue']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('office_supplies.csv', mode='a', header=True)

#############################################
#############################################

print('57 kitchen supplies')
keywords = ['knife', 'cutting board', 'mixing bowl', 'measuring cup', 'can opener', 'spoon', 'spatula', 'tupperware', 'measuring cup', 'dishwasher']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('kitchen_supplies.csv', mode='a', header=True)

#############################################
#############################################

print('58 marketplace')
keywords = ['kijiji', 'facebook marketplace', 'ebay', 'craigslist', 'AKC', 'ali express	', 'alibaba', 'taobao', 'etsy', 'olx']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('marketplace.csv', mode='a', header=True)

#############################################
#############################################

print('59 festivals')
keywords = ['just for laughs', 'eventbrite', 'osheaga', 'piknic electronik', 'ticketmaster', 'jazz fest', 'mural festival', 'francos de montreal', 'Montreal Pride', 'Fringe Festival']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('festivals.csv', mode='a', header=True)

#############################################
#############################################

print('60 fitness')
keywords = ['pilates', 'zumba', 'gym', 'aerobic', 'weight loss', 'yoga', 'jogging', 'Squat', 'push-up', 'running']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('fitness.csv', mode='a', header=True)

#############################################
#############################################

print('61 bathroom supplies')
keywords = ['car repair', 'home repair', 'maintenance', 'air conditioning', 'roof repair	', 'warranty', 'heating system', 'phone repair', 'glass repair', 'water heating']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('bathroom_supplies.csv', mode='a', header=True)

#############################################
#############################################

print('62 insurance')
keywords = ['manulife', 'sunlife', 'desjardins insurance', 'auto insurance', 'health insurance', 'life insurance	', 'geico', 'dental insurance', 'farmers insurance', 'travel insurance']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('insurance.csv', mode='a', header=True)

#############################################
#############################################

print('63 bathroom supplies 2')
keywords = ['toilet paper', 'tissues', 'towels', 'soap', 'shampoo', 'razor', 'hair clipper', 'toothpaste', 'deodorant', 'conditioner']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('bathroom_supplies_2.csv', mode='a', header=True)

#############################################
#############################################

print('64 job areas')
keywords = ['Agriculture', 'Arts	', 'Education', 'Hospitality', 'IT', 'Health Services', 'Science	', 'Dentist', 'Human Resources', 'Lawyer']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('job_areas.csv', mode='a', header=True)

#############################################
#############################################

print('65 racial/ethnic minorities')
keywords = ['black', 'asian', 'latino', 'indian', 'african', 'european', 'chinese', 'mexican', 'italian', 'immigrant']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('racial_ethnic_minorities.csv', mode='a', header=True)

#############################################
#############################################

print('66 drugs')
keywords = ['LSD', 'tobacco', 'magic mushrooms', 'crack', 'heroin', 'opioids', 'cocaine', 'meth', 'MDMA', 'steroids']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('drugs.csv', mode='a', header=True)

#############################################
#############################################

print('67 vegetables')
keywords = ['onions', 'tomatoes', 'lettuce', 'cucumber', 'corn', 'garlic	', 'carrots', 'peppers', 'celery	', 'cabbage']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('vegetables.csv', mode='a', header=True)

#############################################
#############################################

print('68 spices')
keywords = ['salt', 'cumin', 'black pepper', 'Cinnamon', 'Turmeric', 'fennel', 'ginger', 'nutmeg', 'oregano', 'curry']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('spices.csv', mode='a', header=True)

#############################################
#############################################

print('69 pantry')
keywords = ['bananas', 'lemon', 'strawberries', 'sugar', 'bread', 'cheese', 'butter', 'baking powder', 'eggs', 'maple syrup']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pantry.csv', mode='a', header=True)

#############################################
#############################################

print('70 religion')
keywords = ['Christian', 'bible', 'Catholic', 'church', 'Muslim', 'Islam	', 'jewish', 'synagogue', 'god', 'devil']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('religion.csv', mode='a', header=True)

#############################################









