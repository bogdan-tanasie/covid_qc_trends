7# -*- coding: utf-8 -*-
"""
Spyder Editor

Bogdan Tanasie
"""

# Basic imports and settings
import pandas as pd
from pytrends.request import TrendReq
#from googletrans import Translator

import csv
import numpy as np
import time

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', None)

#translator = Translator()

pytrends = TrendReq(hl='en-US')

# Set time and location
timeframe = '2020-01-01 2020-06-21'
geo = 'CA-QC'

# ENGLISH
print("\nENGLISH")
#######################################################################################################################################
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
keywords = ['dating apps', 'Tinder', 'Bumble', 'Happn', 'Hinge', 'online dating', 'Facebook dating', 'Coffee Meets Bagel', 'sugar daddy', 'OKCupid']
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
keywords = ['Photoshop', 'Adobe', 'Winrar', 'Java', 'VLC	', 'Avast', 'Filehippo', 'SAP', 'Shopify	', 'Zoom']
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
keywords = ['Sephora', 'M.A.C', 'eyeliner', 'Glossier', 	"L'Oreal", 'eyeshadow', 'mascara	', 'makeup', 'eyebrow', 'makeup artist']
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
keywords = ['Expedia', 'Hotels.com', 'Airbnb', 'Flighthub', 'hotel', 'Trivago', 'Marriott', 'hostel', 'hotel booking', 'couchsurfing']
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
keywords = ['cruise', 'airplane tickets', 'road trip', 'beach vacations', 'retreats', 'resort', 'Bahamas', 'camping', 'world tour', 'bike trip']
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
keywords = ['BMW', 'sell car', 'car rental', 'used cars', 'auto trader', 'Toyota	', 'electric car', 'Mercedes Benz', 'Tesla', 'car dealership']
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
keywords = ['sushi', 'indian food', 'mexican food', 'asian food', 'vegetarian recipes', 'vegan', 'easy recipes', 'chicken recipes', 'healthy recipes', 'fine dining']
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
keywords = ['Starbucks', 'Tim Hortons', 'tea', 'coffee', 'Nespresso', 'cappuccino ', 'iced coffee', 'Red Bull', 'instant coffee', 'Espresso']
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
keywords = ['cat', 'dog', 'cat coronavirus', 'dog coronavirus', 'adopt a cat', 'adopt a dog', 'adopt a pet', 'adopt a puppy', 'Humane Society', 'SPCA']
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
keywords = ['seeds', 'garden', 'planting', 'fertilizer', 'plants', 'indoor plants', 'outdoor plants', 'soil', 'gardening	', 'when to plant']
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
keywords = ['blood pressure', 'hospitals near', 'dry cough', 'cancer symptoms', 'coronavirus symptoms', 'sore throat', 'HIV', 'health insurance', 'ambulance', 'fever']
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
keywords = ['Indeed', 'layoff', 'Linkedin', 'jobless', 'internship', 'placement', 'EI', 'employment insurance', 'laid off', 'unemployment']
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
keywords = ['solar energy', 'climate change', 'global warming', 'pollution', 'Greta Thunberg', 'recycling', 'waste', 'sustainability' , 'US EPA', 'covid pollution']
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
keywords = ['facial mask', 'dry skin', 'Kylie skin', 'Lumin skin', 'best skin care', 'toners', 'hand moisturizer', 'dry hands', 'pimples', 'men skin care']
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
keywords = ['loan', 'mortgage loan', 'Dow Jones', 'mortgage', 'interest rate', 'savings', 'debt', 'bonds', 'stock market	', 'mutual funds']
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
keywords = ['daycare', 'homeschooling', 'child abuse', 'domestic violence', 'divorce', 'separation', 'home issues', 'custody', 'pregnant', 'condom']
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
keywords = ['theatre', 'cinema', 'clubs', 'bars', 'restaurants', 'massage', 'spa	', 'cooking', 'hiking', 'cabane a sucre']
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
keywords = ['rap', 'rock', 'jazz	', 'blues', 'country music', 'heavy metal', 'hip hop', 'classical music', 'EDM', 'R&B']
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

print('25 sports teams & leagues')
keywords = ['Habs', 'Montreal Impact', 'MLS', 'NBA', 'Stanley Cup', 'NHL	', 'CFL', 'Champions League', 'BPL', 'UFC']
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
keywords = ['comedy', 'romantic', 'thriller', 'science fiction', 'horror', 'documentary', 'adventure', 'mystery', 'drama	', 'action']
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
keywords = ['laptop', 'tablet', 'Ipad', 'Iphone', 'Macbook', 'SSD', 'Microsoft', 'Zoom', '5G', 'gaming PC']
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
keywords = ['medical school', 'McGill', 'student loan', 'HEC Montreal', 'law school', 'student jobs', 'CEGEP', 'UQAM', 'Concordia', 'UdeM']
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
keywords = ['Remax', 'DuProprio', 'Kijiji', 'Centris', 'Zumper', 'Realtor', 'real estate agent', 'mortgage', 'Royal Lepage', 'Sutton']
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
keywords = ['CBC', 'CTV ', 'Fox News', 'CNN', 'La Presse', 'Global News', 'CityNews', 'TVA Nouvelles', 'MTL Blog', 'Montreal Gazette']
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
keywords = ['advil', 'tylenol', 'Jean Coutu', 'Uniprix', 'hydroxychloroquine', 'pharmacy	', 'Pharmaprix', 'Familiprix', 'remdesivir', 'vaccine']
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
keywords = ['orange line', 'green line', 'yellow line', 'blue line', 'STM', 'uber', 'taxi', 'cab	', 'bus', 'bixi']
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
keywords = ['Banana Republic', 'Old Navy	', 'Gap', 'Holt Renfrew', 'Harry Rosen', 'H&M', 'Zara', 'Neon', 'Winners', 'Forever 21']
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
keywords = ['Facebook', 'Instagram', 'Snapchat', 'Twitter', 'WeChat', 'WhatsApp', 'Skype', 'Tik Tok', 'Tumblr', 'Pinterest']
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
keywords = ['Netflix', 'Crave', 'Disney+	', 'Spotify', 'Audible', 'Prime video', 'Hulu', 'Hbo', 'Apple TV	', 'Apple Music']
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
keywords = ['jewelry', 'diamond ring', 'earrings', 'bracelet', 'watch', 'Pandora', 'Tiffany & Co	', 'Swarovski', 'piercing', 'ring']
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
keywords = ['allergies', 'flu', 'diarrhea', 'headache', 'stomach ache', 'anorexia', 'vomiting', 'asthma', 'bronchitis', 'back pain']
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
keywords = ['soccer', 'football', 'basketball', 'swimming', 'hockey', 'golf', 'UFC', 'Ski', 'snowboard', 'tennis']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('sports.csv', mode='a', header=True)


#############################################
#############################################

## diet
print('40 diet')
keywords = ['mediterranean diet', 'diet', 'atkins diet', 'dash diet', 'keto diet', 'weight loss', 'low carb diet', 'raw vegan', 'carnivore diet', 'plant based diet']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('diet.csv', mode='a', header=True)

#############################################
#############################################

### charity -> nonprofit
print('41 charity')
keywords = ['nonprofit', 'donate', 'food bank', 'charities', 'World Vision', 'Red Cross', 'Doctors Without Borders', 'blood donation', 'donation', 'thrift store']
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
keywords = ['learn french', 'Duolingo', 'TED', 'Khan Academy', 'Goodreads', 'translate', 'lessons', 'classes', 'online classes', 'summer courses']
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
keywords = ['bangs', 'hairstyle', 'haircut', 'beard', 'mullet', 'moustache', 'shave', 'buzz cut', 'afro', 'shaving']
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
keywords = ['board games', 'Minecraft', 'piccolo', 'Miniclip', 'online games', 'Xbox', 'World of Warcraft', 'Nintendo Switch', 'PlayStation', 'Risk']
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
keywords = ['Uber Eats', 'Foodora', 'Fedex', 'Amazon Prime', 'Cookit', 'Lufa', 'Iga delivery', 'Walmart delivery	', 'Provigo delivery', 'Metro delivery']
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
keywords = ['poker', 'sports betting', 'casino', 'online casino', 'Bet365', 'Primedice', 'betting', 'FlashScore', 'blackjack', 'Vegas Casino Online']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('gambling.csv', mode='a', header=True)

#############################################
#############################################

## death -> dying
## funderl -> ...
print('47 death')
keywords = ['funeral', 'death', 'coffin', 'dead', 'cremation', 'after death', 'heaven ', 'murder', 'hell', 'soul']
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
keywords = ['BDSM porn', 'porn', 'Redtube', 'Youporn', 'Pornhub', 'lesbian porn', 'sex', 'Chaturbate', 'hentai', 'gay porn']
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
keywords = ['happy', 'anxiety', 'angry', 'sad', 'depression', 'horny', 'lonely', 'bored', 'worried', 'in love']
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
keywords = ['Ikea', 'Target', 'Home Depot', 'Costco', 'Amazon', 'Couche Tard', 'IGA', 'Best Buy', 'Metro', 'Walmart', ]
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
keywords = ['Simons', 'Canadian Tire', 'La Baie', 'Home Hardware	', 'Old Navy', 'Sears', 'Aldo', 'Dollarama', 'Structube', 'Reitmans']
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
keywords = ['Bank of Montreal', 'Desjardins', 'Laurentian Bank', 'TD', 'CIBC', 'RBC', 'HSBC', 'Banque Nationale', 'BMO', 'Bitcoin']
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
keywords = ['beer', 'wine', 'liquor', 'cocktails', 'cider', 'Corona beer', 'Coors', 'rum', 'drunk', 'alcoholic']
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
keywords = ['SQDC', 'marijuana', 'weed', 'indica	', 'sativa', 'CBD', 'hash', 'cannabis', 'edibles	', 'THC']
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
keywords = ['staples', 'pens', 'envelopes', 'scissors', 'stapler	', 'quill', 'calculator', 'printer', 'printer ink', 'glue']
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
keywords = ['knife', 'cutting board', 'mixing bowl', 'measuring cup', 'can opener', 'spoon', 'spatula', 'tupperware', 'pan', 'dishwasher']
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
keywords = ['Kijiji', 'Facebook Marketplace', 'Ebay', 'Craigslist', 'AKC', 'Ali Express	', 'Alibaba', 'Taobao', 'Etsy', 'OLX']
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
keywords = ['Just For Laughs', 'Eventbrite', 'Osheaga', 'Piknic Electronik', 'Ticketmaster', 'Jazz Fest', 'Mural Festival', 'Francos de Montreal', 'Montreal Pride', 'Fringe Festival']
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
keywords = ['pilates', 'zumba', 'gym', 'aerobic', 'weight loss', 'yoga', 'jogging', 'squat', 'push-up', 'running']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('fitness.csv', mode='a', header=True)

#############################################
#############################################

print('61 repair')
keywords = ['car repair', 'home repair', 'maintenance', 'air conditioning', 'roof repair	', 'warranty', 'heating system', 'phone repair', 'glass repair', 'water heating']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('repair.csv', mode='a', header=True)

#############################################
#############################################

print('62 insurance')
keywords = ['Manulife', 'Sunlife', 'Desjardins insurance', 'auto insurance', 'health insurance', 'life insurance	', 'GEICO', 'dental insurance', 'farmers insurance', 'travel insurance']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('insurance.csv', mode='a', header=True)

#############################################
#############################################

print('63 bathroom supplies')
keywords = ['toilet paper', 'tissues', 'towels', 'soap', 'shampoo', 'razor', 'hair clipper', 'toothpaste', 'deodorant', 'conditioner']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('bathroom_supplies.csv', mode='a', header=True)

#############################################
#############################################

print('64 job areas')
keywords = ['Agriculture', 'Arts	', 'Education', 'Hospitality', 'IT', 'Health Services', 'Science	', 'Medicine', 'Human Resources', 'Lawyer']
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
keywords = ['salt', 'cumin', 'black pepper', 'cinnamon', 'turmeric', 'fennel', 'ginger', 'nutmeg', 'oregano', 'curry']
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
keywords = ['Christian', 'Bible', 'Catholic', 'church', 'Muslim', 'Islam	', 'Jewish', 'synagogue', 'God', 'Devil']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('religion.csv', mode='a', header=True)

print('DONE')
#############################################

# FRENCH
print("\nFRENCH")
# GOOGLE TRANSLATE WAS NOT PRECISE ENOUGH, NEEDED MANUAL TRANSLATION
#######################################################################################################################################
#kw = translator.translate(kw, src='en', dest='fr').text

#############################################

print('1 wedding')
keywords = ['bague de fiançailles', 'robe de mariée', 'lune de miel', 'anniversaire de mariage', 'avant mariage', 'mariée', 'en espèces', 'noces', 'salle de mariage', 'fiançailles']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('wedding_fr.csv', mode='a', header=True)

#############################################
#############################################

print('2 political parties')
keywords = ['Libertarien', 'Bloc Québecois', 'PQ', 'PPC' , 'Québec Solidaire', 'CAQ', 'Parti Conservateur', 'Parti Vert', 'Parti Libéral ', 'NDP']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('political_parties_fr.csv', mode='a', header=True)

#############################################
#############################################

print('3 dating')
keywords = ['sites de rencontres', 'Tinder', 'Bumble', 'Happn', 'Hinge', 'célibataire', 'rencontres Facebook', 'Coffee Meets Bagel', 'sugar daddy', 'OKCupid']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('dating_fr.csv', mode='a', header=True)

#############################################
#############################################

print('4 software')
keywords = ['Photoshop', 'Adobe', 'Winrar', 'Java', 'VLC	', 'Avast', 'Filehippo', 'SAP', 'Shopify	', 'Zoom']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('software_fr.csv', mode='a', header=True)

#############################################
#############################################

print('5 fast food restaurants')
keywords = ["McDonald", 'KFC', 'Pizza hut', 'Burger king', "Wendy's", 'A&W', 'St-Hubert', 'Subway', "Domino's", 'Taco Bell']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('fast_food_restaurants_fr.csv', mode='a', header=True)

#############################################
#############################################

print('6 STIs')
keywords = ['Chlamydia', 'VIH', 'Herpès', 'Blennorragie', 'HPV', 'Hépatite B', 'Syphilis', 'STI', 'ITSS', 'Hépatite A']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('stis_fr.csv', mode='a', header=True)

#############################################
#############################################

print('7 makeup')
keywords = ['Sephora', 'M.A.C', 'eyeliner', 'Glossier', 	"L'Oréal", 'fard', 'mascara', 'maquillage', 'sourcil', 'maquilleur']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('makeup_fr.csv', mode='a', header=True)

#############################################
#############################################

print('8 hotel')
keywords = ['Expedia', 'Hotels.com', 'Airbnb', 'Flighthub', 'hôtel', 'Trivago', 'Marriott', 'auberge', "réservation", 'couchsurfing']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('hotel_fr.csv', mode='a', header=True)

#############################################
#############################################


# Bahamas trip does not seem to work
print('9 travel')
keywords = ['croisière', "billets d'avion", 'road trip', 'plage', 'vacances', 'resort', 'Bahamas', 'camping', 'tour du monde', 'randonnée']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('travel_fr.csv', mode='a', header=True)

#############################################
#############################################

print('10 cars')
keywords = ['BMW', 'vendre une voiture', 'louer une voiture', "voiture", "acheter une voiture", 'Toyota', 'voiture électrique', 'Mercedes Benz', 'Tesla', 'concessionnaire']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('cars_fr.csv', mode='a', header=True)

#############################################
#############################################

print('11 recipies')
keywords = ['sushi', 'recette indienne', 'recette mexicaine', 'recette asiatique', 'recettes végétariennes', 'végétalien', 'recettes faciles', 'recettes au poulet', 'recettes santé', 'fine cuisine']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('recipies_fr.csv', mode='a', header=True)

#############################################
#############################################

print('12 caffeine')
keywords = ['Starbucks', 'Tim Hortons', 'thé', 'café', 'Nespresso', 'cappuccino ', 'café glacé', 'Red Bull', 'café instantané', 'Espresso']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('caffeine_fr.csv', mode='a', header=True)

#############################################
#############################################

print('13 politicians/personalities')
keywords = ['Justin Trudeau', 'Celine Dion', 'Ryan Renolds', 'Doug Ford', 'François Legault ', 'Valerie Plante', 'Donald Trump', 'Joe Biden', 'Pierre Arcand', 'Horacio Arruda']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('politicians_personalities_fr.csv', mode='a', header=True)

#############################################
#############################################

print('14 pets')
keywords = ['chat', 'chien', 'chat coronavirus', 'chien coronavirus', 'adopter un chat', 'adopter un chien', 'adopter un animal', 'adopter un chiot', 'Humane Society', 'SPCA']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pets_fr.csv', mode='a', header=True)

#############################################
#############################################

print('15 gardening')
keywords = ['graines', 'jardin', 'planter', 'engrais', 'plante', "plantes annuelles", "fleurs", 'sol', 'jardinage', 'quand planter']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('gardening_fr.csv', mode='a', header=True)

#############################################
#############################################

print('16 health')
keywords = ['pression artérielle', 'hôpitaux', 'toux sèche', 'symptômes du cancer', 'symptômes coronavirus', 'gorge irritée', 'VPH', 'assurance santé', 'ambulance', 'fièvre']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('health_fr.csv', mode='a', header=True)

#############################################
#############################################

print('17 jobs')
keywords = ['Indeed', 'licenciement', 'Linkedin', 'sans emploi', 'stage', 'placement', 'EI', 'assurances emploi', 'chômage', 'congé']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('jobs_fr.csv', mode='a', header=True)

#############################################
#############################################

print('18 environment')
keywords = ['énergie solaire', 'changement climatique', 'réchauffement climatique', 'pollution', 'Greta Thunberg', 'recyclage', 'déchets', 'durabilité' , 'US EPA', 'pollution covid']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('environment_fr.csv', mode='a', header=True)

#############################################
#############################################

print('19 skin care')
keywords = ['masque facial', 'peau sèche', 'Kylie skin', 'Lumin skin', 'soins de la peau', 'tonifiant', 'hydratant', 'mains sèches', 'acnée', 'soins visage']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('skin_care_fr.csv', mode='a', header=True)

#############################################
#############################################

print('20 finance')
keywords = ['prêt', 'prêt hypothécaire', 'Dow Jones', 'hypothèque', "intérêt", 'épargnes', 'dette', 'obligations', 'marché financier', 'fonds communs de placement']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('finance_fr.csv', mode='a', header=True)

#############################################
#############################################

print('21 home_issues')
keywords = ['garderie', 'école à la maison', 'abus', 'violence domestique', 'divorce', 'séparation', 'maison', 'garde', 'enceinte', 'condom']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('home_issues_fr.csv', mode='a', header=True)

#############################################
#############################################

print('22 activities')
keywords = ['théâtre', 'cinéma', 'clubs', 'bars', 'restaurants', 'massage', 'spa	', 'cuisiner', 'randonnée', 'cabane à sucre']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('activities_fr.csv', mode='a', header=True)

#############################################
#############################################

print('23 music')
keywords = ['rap', 'rock', 'jazz	', 'blues', 'musique country', 'heavy metal', 'hip hop', 'musique classique', 'EDM', 'R&B']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('music_fr.csv', mode='a', header=True)

#############################################
#############################################

print('24 food')
keywords = ['crème glacée', 'gâteau', 'poutine', 'hamburger', 'hot dog', 'pizza', 'chips', 'frites', 'sandwich', 'fromage']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('food_fr.csv', mode='a', header=True)

#############################################
#############################################

print('25 sports teams & leagues')
keywords = ['Habs', 'Impact Montréal', 'MLS', 'NBA', 'Coupe Stanley', 'NHL', 'CFL', 'Ligue des champions', 'BPL', 'UFC']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('sports_teams_leagues_fr.csv', mode='a', header=True)

#############################################
#############################################

print('26 movie genre')
keywords = ['comédie', 'romantique', 'thriller', 'science fiction', 'horreur', 'documentaire', 'aventure', 'mystère', 'drame', 'action']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('movie_genre_fr.csv', mode='a', header=True)

#############################################
#############################################

print('27 computers')
keywords = ['laptop', 'tablette', 'Ipad', 'Iphone', 'Macbook', 'SSD', 'Microsoft', 'Zoom', '5G', 'PC de jeu']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe,geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('computers_fr.csv', mode='a', header=True)

#############################################
#############################################

print('28 relationship')
keywords = ['relation', 'tricher', 'condom', 'sexting', 'fréquentation', 'accouplement', 'mariage', 'jaloux', 'longue distance', 'rompre']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('relationship_fr.csv', mode='a', header=True)

#############################################
#############################################

print('29 education')
keywords = ['faculté de médecine', 'McGill', 'prêt étudiant', 'HEC Montréal', 'faculté de droit', 'emplois étudiants', 'CÉGEP', 'UQAM', 'Concordia', 'UdeM']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('education_fr.csv', mode='a', header=True)

#############################################
#############################################

print('30 housing')
keywords = ['Remax', 'DuProprio', 'Kijiji', 'Centris', 'Zumper', 'Realtor', 'agent immobilier', 'hypothèque', 'Royal Lepage', 'Sutton']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('housing_fr.csv', mode='a', header=True)

#############################################
#############################################

print('31 news')
keywords = ['CBC', 'CTV ', 'Fox News', 'CNN', 'La Presse', 'Global News', 'CityNews', 'TVA Nouvelles', 'MTL Blog', 'Montréal Gazette']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('news_fr.csv', mode='a', header=True)

#############################################
#############################################

print('32 pharmaceutical')
keywords = ['advil', 'tylenol', 'Jean Coutu', 'Uniprix', 'hydroxychloroquine', 'pharmacie', 'Pharmaprix', 'Familiprix', 'remdesivir', 'vaccins']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pharmaceutical_fr.csv', mode='a', header=True)

#############################################
#############################################

print('33 transportation')
keywords = ['ligne orange', 'ligne verte', 'ligne verte', 'ligne bleue', 'STM', 'uber', 'taxi', 'chauffeur', 'bus', 'bixi']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo='CA-QC', gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('transportation_fr.csv', mode='a', header=True)

#############################################
#############################################

print('34 clothing_stores')
keywords = ['Banana Republic', 'Old Navy	', 'Gap', 'Holt Renfrew', 'Harry Rosen', 'H&M', 'Zara', 'Neon', 'Winners', 'Forever 21']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('clothing_stores_fr.csv', mode='a', header=True)

#############################################
#############################################

print('35 social_media')
keywords = ['Facebook', 'Instagram', 'Snapchat', 'Twitter', 'WeChat', 'WhatsApp', 'Skype', 'Tik Tok', 'Tumblr', 'Pinterest']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('social_media_fr.csv', mode='a', header=True)

#############################################
#############################################

print('36 arts & entertainment')
keywords = ['Netflix', 'Crave', 'Disney+	', 'Spotify', 'Audible', 'Prime video', 'Hulu', 'Hbo', 'Apple TV	', 'Apple Music']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('arts_entertainment_fr.csv', mode='a', header=True)

#############################################
#############################################

print('37 jewelry')
keywords = ['bijoux', 'bague de diamant', "boucles d'oreilles", 'braclet', 'montre', 'Pandora', 'Tiffany & Co', 'Swarovski', 'percer', 'bague']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('jewelry_fr.csv', mode='a', header=True)

#############################################
#############################################

print('38 illnesses')
keywords = ['allergies', 'grippe', 'diarrhée', 'mal de tête', 'mal au ventre', 'anorexie', 'vomissement', 'asthme', 'bronchite', 'mal au dos']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('illnesses_fr.csv', mode='a', header=True)

#############################################
#############################################

print('39 sports')
keywords = ['soccer', 'football', 'basketball', 'natation', 'hockey', 'golf', 'UFC', 'Ski', 'snowboard', 'tennis']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('sports_fr.csv', mode='a', header=True)


#############################################
#############################################

## diet
print('40 diet')
keywords = ['diète méditerranéenne', 'diète', 'régime atkins', 'régime', 'keto', 'perte du poids', 'maigrir', 'végétalien', 'carnivore', 'sans sucre']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('diet_fr.csv', mode='a', header=True)

#############################################
#############################################

### charity -> nonprofit
print('41 charity')
keywords = ['non lucratif', 'faire un don', 'banque alimentaire', 'charité', 'World Vision', 'Red Cross', 'Doctors Without Borders', 'donner du sang', 'donation', 'friperie']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('charity_fr.csv', mode='a', header=True)

#############################################
#############################################

print('42 learning')
keywords = ['learn english', 'Duolingo', 'TED', 'Khan Academy', 'Goodreads', 'traduire', 'cours', 'classes', 'cours en ligne', "cours été"]
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('learning_fr.csv', mode='a', header=True)

#############################################
#############################################

print('43 hairstyle')
keywords = ['frange', 'coiffure', 'coupe de cheveux', 'barbe', 'mulet', 'moustache', 'couper', 'coupe maison', 'afro', 'rasage']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('hairstyle_fr.csv', mode='a', header=True)

#############################################
#############################################

print('44 games')
keywords = ['jeux de société', 'Minecraft', 'piccolo', 'Miniclip', 'jeux en ligne', 'Xbox', 'World of Warcraft', 'Nintendo Switch', 'PlayStation', 'Risk']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('games_fr.csv', mode='a', header=True)

#############################################
#############################################

print('45 delivery')
keywords = ['Uber Eats', 'Foodora', 'Fedex', 'Amazon Prime', 'Cookit', 'Lufa', 'Iga delivery', 'Walmart delivery	', 'Provigo delivery', 'Metro delivery']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('delivery_fr.csv', mode='a', header=True)

#############################################
#############################################

print('46 gambling')
keywords = ['poker', 'paris sportif', 'casino', 'casino en ligne', 'Bet365', 'Primedice', 'betting', 'FlashScore', 'blackjack', 'Vegas Casino Online']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('gambling_fr.csv', mode='a', header=True)

#############################################
#############################################

## death -> dying
## funderl -> ...
print('47 death')
keywords = ['funérailles', 'mourrir', 'coffin', 'mort', 'incinération', 'après mort', 'paradis', 'meurtre', 'enfer', 'esprit']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('death_fr.csv', mode='a', header=True)

#############################################
#############################################

print('48 porn')
keywords = ['porno BDSM', 'porno', 'Redtube', 'Youporn', 'Pornhub', 'porno lesbien', 'sex', 'Chaturbate', 'hentai', 'porno gay']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('porn_fr.csv', mode='a', header=True)

#############################################
#############################################

print('49 feelings')
keywords = ['heureux', 'anxiété', 'fâché', 'triste', 'dépression', 'excité', 'seul', 'ennuyé', 'stressé', 'en amour']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('feelings_fr.csv', mode='a', header=True)

#############################################
#############################################

print('50 retail')
keywords = ['Ikea', 'Target', 'Home Depot', 'Costco', 'Amazon', 'Couche Tard', 'IGA', 'Best Buy', 'Metro', 'Walmart', ]
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('retail_fr.csv', mode='a', header=True)

#############################################
#############################################

print('51 retail 2')
keywords = ['Simons', 'Canadian Tire', 'La Baie', 'Home Hardware	', 'Old Navy', 'Sears', 'Aldo', 'Dollarama', 'Structube', 'Reitmans']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('retail_2_fr.csv', mode='a', header=True)

#############################################
#############################################

print('52 banks')
keywords = ['Banque de Montréal', 'Desjardins', 'Banque Laurentienne', 'TD', 'CIBC', 'RBC', 'HSBC', 'Banque Nationale', 'BMO', 'Bitcoin']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('banks_fr.csv', mode='a', header=True)

#############################################
#############################################

print('53 alcohol')
keywords = ['bière', 'vin', 'alcool', 'cocktails', 'cidre', 'bière Corona', 'Coors', 'rhum', 'soul', 'alcoolique']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('alcohol_fr.csv', mode='a', header=True)

#############################################
#############################################

print('54 marijuana/drugs')
keywords = ['SQDC', 'marijuana', 'cannabis', 'indica', 'sativa', 'CBD', 'hash', 'herbe', 'comestibles', 'THC']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('marijuana_drugs_fr.csv', mode='a', header=True)

#############################################
#############################################

print('55 mental health')
keywords = ['anxiété', 'dépression', 'méditation	', 'psychothérapie', 'thérapie en ligne', 'santé mentale', 'anxiété sociale', 'télésanté', 'ADHD', 'insomnie']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('mental_health_fr.csv', mode='a', header=True)

#############################################
#############################################

print('56 office supplies')
keywords = ['agrafes', 'stylos', 'enveloppes', 'ciseaux', 'agrafeuse', 'plume', 'calculatrice', 'imprimante', 'encre', 'colle']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('office_supplies_fr.csv', mode='a', header=True)


#############################################
#############################################

print('57 kitchen supplies')
keywords = ['couteau', 'planche à découper', 'bol', 'tasse', 'ouvre-boîte', 'cuillère', 'spatule', 'tupperware', 'poêle', 'lave-vaisselle']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('kitchen_supplies_fr.csv', mode='a', header=True)

#############################################
#############################################

print('58 marketplace')
keywords = ['Kijiji', 'Facebook Marketplace', 'Ebay', 'Craigslist', 'AKC', 'Ali Express	', 'Alibaba', 'Taobao', 'Etsy', 'OLX']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('marketplace_fr.csv', mode='a', header=True)

#############################################
#############################################

print('59 festivals')
keywords = ['Juste Pour Rire', 'Eventbrite', 'Osheaga', 'Piknic Electronik', 'Ticketmaster', 'Jazz Fest', 'Mural Festival', 'Francos de Montréal', 'Fierté Montréal', 'Fringe Festival']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('festivals_fr.csv', mode='a', header=True)

#############################################
#############################################

print('60 fitness')
keywords = ['pilates', 'zumba', 'gym', 'aerobic', 'maigrir', 'yoga', 'jogging', 'squat', 'push-up', 'courir']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('fitness_fr.csv', mode='a', header=True)

#############################################
#############################################

print('61 repair')
keywords = ['réparation voiture', 'réparation maison', 'entretien', 'climatisation', 'réparation toit', 'garantie', 'système de chauffage', 'réparation de téléphone', 'réparation verre', 'chauffage eau']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('repair_fr.csv', mode='a', header=True)


#############################################
#############################################

print('62 insurance')
keywords = ['Manulife', 'Sunlife', 'assurance Desjardins', 'assurance auto', 'assurance santé', 'assurance vie', 'GEICO', 'assurance dentaire', 'assurance ferme', 'assurance voyage']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('insurance_fr.csv', mode='a', header=True)

#############################################
#############################################

print('63 bathroom supplies')
keywords = ['papier toilette', 'tissus', 'serviettes', 'savon', 'shampooing', 'rasoir', 'tondeuse à cheveux', 'dentifrice', 'déodorant', 'conditionneur']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('bathroom_supplies_fr.csv', mode='a', header=True)

#############################################
#############################################

print('64 job areas')
keywords = ['Agriculture', 'Arts	', 'Education', 'Hospitalité', 'TI', 'Services de santé', 'Science', 'Médicine', 'Ressources Humaines', 'Avocat']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('job_areas_fr.csv', mode='a', header=True)

#############################################
#############################################

print('65 racial/ethnic minorities')
keywords = ['noir', 'asiatique', 'latino', 'indien', 'africain', 'européen', 'chinois', 'mexicain', 'italien', 'immigrant']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('racial_ethnic_minorities_fr.csv', mode='a', header=True)

#############################################
#############################################

print('66 drugs')
keywords = ['LSD', 'tabac', 'champignons magiques', 'crack', 'héroïne', 'opioïdes', 'cocaïne', 'meth', 'MDMA', 'stéroïdes']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('drugs_fr.csv', mode='a', header=True)

#############################################
#############################################

print('67 vegetables')
keywords = ['oignons', 'tomates', 'laitue', 'concombre', 'maïs', 'ail', 'carottes', 'poivrons', 'céleri', 'chou']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('vegetables_fr.csv', mode='a', header=True)

#############################################
#############################################

print('68 spices')
keywords = ['sel', 'cumin', 'poivre noir', 'cannelle', 'turmeric', 'fenouil', 'gingembre', 'noix de muscade', 'origan', 'curry']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('spices_fr.csv', mode='a', header=True)

#############################################
#############################################

print('69 pantry')
keywords = ['bananes', 'citron', 'fraises', 'sucre', 'pain', 'fromage', 'beurre', 'levure', 'oeufs', 'sirop érable']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('pantry_fr.csv', mode='a', header=True)

#############################################
#############################################

print('70 religion')
keywords = ['chrétien', 'Bible', 'catholique', 'église', 'musulman', 'Islam', 'juif', 'synagogue', 'Dieu', 'diable']
print(len(keywords))
res = pd.DataFrame()

for kw in keywords:
    pytrends.build_payload(kw_list=[kw], cat=0, timeframe=timeframe, geo=geo, gprop='')
    df = pytrends.interest_over_time()

    res = res.append(df[kw])

res.T.to_csv('religion_fr.csv', mode='a', header=True)

print('DONE')
#############################################
