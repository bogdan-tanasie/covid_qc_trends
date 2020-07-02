library(tidyverse)

dates <- read_csv("Data/date.csv")
attach(dates)

#EN
activities <- read_csv("Data/activities.csv")
names(activities)[1] <- "date"
attach(activities)

alcohol <- read_csv("Data/alcohol.csv")
names(alcohol)[1] <- "date"
attach(alcohol)

arts_entertainment <- read_csv("Data/arts_entertainment.csv")
names(arts_entertainment)[1] <- "date"
attach(arts_entertainment)

banks <- read_csv("Data/banks.csv")
names(banks)[1] <- "date"
attach(banks)

repair <- read_csv("Data/repair.csv")
names(repair)[1] <- "date"
attach(repair)

bathroom_supplies <- read_csv("Data/bathroom_supplies.csv")
names(bathroom_supplies)[1] <- "date"
attach(bathroom_supplies)

caffeine <- read_csv("Data/caffeine.csv")
names(caffeine)[1] <- "date"
attach(caffeine)

cars <- read_csv("Data/cars.csv")
names(cars)[1] <- "date"
attach(cars)

charity <- read_csv("Data/charity.csv")
names(charity)[1] <- "date"
attach(charity)

clothing_stores <- read_csv("Data/clothing_stores.csv")
names(clothing_stores)[1] <- "date"
attach(clothing_stores)

computers <- read_csv("Data/computers.csv")
names(computers)[1] <- "date"
attach(computers)

dating <- read_csv("Data/dating.csv")
names(dating)[1] <- "date"
attach(dating)

death_ <- read_csv("Data/death.csv")
names(death_)[1] <- "date"
attach(death_)

delivery <- read_csv("Data/delivery.csv")
names(delivery)[1] <- "date"
attach(delivery)

diet_ <- read_csv("Data/diet.csv")
names(diet_)[1] <- "date"
attach(diet_)

drugs <- read_csv("Data/drugs.csv")
names(drugs)[1] <- "date"
attach(drugs)

education <- read_csv("Data/education.csv")
names(education)[1] <- "date"
attach(education)

environment <- read_csv("Data/environment.csv")
names(environment)[1] <- "date"
attach(environment)

fast_food_restaurants <- read_csv("Data/fast_food_restaurants.csv")
names(fast_food_restaurants)[1] <- "date"
attach(fast_food_restaurants)

feelings <- read_csv("Data/feelings.csv")
names(feelings)[1] <- "date"
attach(feelings)

festivals <- read_csv("Data/festivals.csv")
names(festivals)[1] <- "date"
attach(festivals)

finance <- read_csv("Data/finance.csv")
names(finance)[1] <- "date"
attach(finance)

fitness <- read_csv("Data/fitness.csv")
names(fitness)[1] <- "date"
attach(fitness)

food <- read_csv("Data/food.csv")
names(food)[1] <- "date"
attach(food)

gambling <- read_csv("Data/gambling.csv")
names(gambling)[1] <- "date"
attach(gambling)

games <- read_csv("Data/games.csv")
names(games)[1] <- "date"
attach(games)

garderning_ <- read_csv("Data/gardening.csv")
names(garderning_)[1] <- "date"
attach(garderning_)

hairstyle_ <- read_csv("Data/hairstyle.csv")
names(hairstyle_)[1] <- "date"
attach(hairstyle_)

health <- read_csv("Data/health.csv")
names(health)[1] <- "date"
attach(health)

home_issues_ <- read_csv("Data/home_issues.csv")
names(home_issues_)[1] <- "date"
attach(home_issues_)

hotel_ <- read_csv("Data/hotel.csv")
names(hotel_)[1] <- "date"
attach(hotel_)

housing <- read_csv("Data/housing.csv")
names(housing)[1] <- "date"
attach(housing)

illnesses <- read_csv("Data/illnesses.csv")
names(illnesses)[1] <- "date"
attach(illnesses)

insurance <- read_csv("Data/insurance.csv")
names(insurance)[1] <- "date"
attach(illnesses)

jewelry_ <- read_csv("Data/jewelry.csv")
names(jewelry_)[1] <- "date"
attach(jewelry_)

job_areas <- read_csv("Data/job_areas.csv")
names(job_areas)[1] <- "date"
attach(job_areas)

jobs <- read_csv("Data/jobs.csv")
names(jobs)[1] <- "date"
attach(jobs)

kitchen_supplies <- read_csv("Data/kitchen_supplies.csv")
names(kitchen_supplies)[1] <- "date"
attach(kitchen_supplies)

learning <- read_csv("Data/learning.csv")
names(learning)[1] <- "date"
attach(learning)

makeup <- read_csv("Data/makeup.csv")
names(makeup)[1] <- "date"
attach(makeup)

marijuana_drugs <- read_csv("Data/marijuana_drugs.csv")
names(marijuana_drugs)[1] <- "date"
attach(marijuana_drugs)

marketplace <- read_csv("Data/marketplace.csv")
names(marketplace)[1] <- "date"
attach(marketplace)

mental_health <- read_csv("Data/mental_health.csv")
names(mental_health)[1] <- "date"
attach(mental_health)

movie_genre <- read_csv("Data/movie_genre.csv")
names(movie_genre)[1] <- "date"
attach(movie_genre)

music <- read_csv("Data/music.csv")
names(music)[1] <- "date"
attach(music)

news <- read_csv("Data/news.csv")
names(news)[1] <- "date"
attach(news)

office_supplies <- read_csv("Data/office_supplies.csv")
names(office_supplies)[1] <- "date"
attach(office_supplies)

pantry <- read_csv("Data/pantry.csv")
names(pantry)[1] <- "date"
attach(pantry)

pets <- read_csv("Data/pets.csv")
names(pets)[1] <- "date"
attach(pets)

pharmaceutical <- read_csv("Data/pharmaceutical.csv")
names(pharmaceutical)[1] <- "date"
attach(pharmaceutical)

political_parties <- read_csv("Data/political_parties.csv")
names(political_parties)[1] <- "date"
attach(political_parties)

politicians_personalities <- read_csv("Data/politicians_personalities.csv")
names(politicians_personalities)[1] <- "date"
attach(politicians_personalities)

porn_ <- read_csv("Data/porn.csv")
names(porn_)[1] <- "date"
attach(porn_)

racial_ethnic_minorities <- read_csv("Data/racial_ethnic_minorities.csv")
names(racial_ethnic_minorities)[1] <- "date"
attach(racial_ethnic_minorities)

recipies <- read_csv("Data/recipies.csv")
names(recipies)[1] <- "date"
attach(recipies)

relationship_ <- read_csv("Data/relationship.csv")
names(relationship_)[1] <- "date"
attach(relationship_)

religion <- read_csv("Data/religion.csv")
names(religion)[1] <- "date"
attach(religion)

retail <- read_csv("Data/retail.csv")
names(retail)[1] <- "date"
attach(retail)

retail_2 <- read_csv("Data/retail_2.csv")
names(retail_2)[1] <- "date"
attach(retail_2)

skin_care <- read_csv("Data/skin_care.csv")
names(skin_care)[1] <- "date"
attach(skin_care)

social_media <- read_csv("Data/social_media.csv")
names(social_media)[1] <- "date"
attach(social_media)

software <- read_csv("Data/software.csv")
names(software)[1] <- "date"
attach(software)

spices <- read_csv("Data/spices.csv")
names(spices)[1] <- "date"
attach(spices)

sports <- read_csv("Data/sports.csv")
names(sports)[1] <- "date"
attach(sports)

sports_teams_leagues <- read_csv("Data/sports_teams_leagues.csv")
names(sports_teams_leagues)[1] <- "date"
attach(sports_teams_leagues)

stis <- read_csv("Data/stis.csv")
names(stis)[1] <- "date"
attach(stis)

transportation <- read_csv("Data/transportation.csv")
names(transportation)[1] <- "date"
attach(transportation)

travel <- read_csv("Data/travel.csv")
names(travel)[1] <- "date"
attach(travel)

vegetables <- read_csv("Data/vegetables.csv")
names(vegetables)[1] <- "date"
attach(vegetables)

wedding <- read_csv("Data/wedding.csv")
names(wedding)[1] <- "date"
attach(wedding)

###############################################

#FR
activities_fr <- read_csv("Data/activities_fr.csv")
names(activities_fr)[1] <- "date"
attach(activities_fr)

alcohol_fr <- read_csv("Data/alcohol_fr.csv")
names(alcohol_fr)[1] <- "date"
attach(activities_fr)

arts_entertainment_fr <- read_csv("Data/arts_entertainment_fr.csv")
names(arts_entertainment_fr)[1] <- "date"
attach(arts_entertainment_fr)

banks_fr <- read_csv("Data/banks_fr.csv")
names(banks_fr)[1] <- "date"
attach(banks_fr)

repair_fr <- read_csv("Data/repair_fr.csv")
names(repair_fr)[1] <- "date"
attach(repair_fr)

bathroom_supplies_fr <- read_csv("Data/bathroom_supplies_fr.csv")
names(bathroom_supplies_fr)[1] <- "date"
attach(bathroom_supplies_fr)

caffeine_fr <- read_csv("Data/caffeine_fr.csv")
names(caffeine_fr)[1] <- "date"
attach(caffeine_fr)

cars_fr <- read_csv("Data/cars_fr.csv")
names(cars_fr)[1] <- "date"
attach(cars_fr)

charity_fr <- read_csv("Data/charity_fr.csv")
names(charity_fr)[1] <- "date"
attach(charity_fr)

clothing_stores_fr <- read_csv("Data/clothing_stores_fr.csv")
names(clothing_stores_fr)[1] <- "date"
attach(clothing_stores_fr)

computers_fr <- read_csv("Data/computers_fr.csv")
names(computers_fr)[1] <- "date"
attach(computers_fr)

dating_fr <- read_csv("Data/dating_fr.csv")
names(dating_fr)[1] <- "date"
attach(dating_fr)

death_fr <- read_csv("Data/death_fr.csv")
names(death_fr)[1] <- "date"
attach(death_fr)

delivery_fr <- read_csv("Data/delivery_fr.csv")
names(delivery_fr)[1] <- "date"
attach(delivery_fr)

diet_fr <- read_csv("Data/diet_fr.csv")
names(diet_fr)[1] <- "date"
attach(diet_fr)

drugs_fr <- read_csv("Data/drugs_fr.csv")
names(drugs_fr)[1] <- "date"
attach(drugs_fr)

education_fr <- read_csv("Data/education_fr.csv")
names(education_fr)[1] <- "date"
attach(education_fr)

environment_fr <- read_csv("Data/environment_fr.csv")
names(environment_fr)[1] <- "date"
attach(environment_fr)

fast_food_restaurants_fr <- read_csv("Data/fast_food_restaurants_fr.csv")
names(fast_food_restaurants_fr)[1] <- "date"
attach(fast_food_restaurants_fr)

feelings_fr <- read_csv("Data/feelings_fr.csv")
names(feelings_fr)[1] <- "date"
attach(feelings_fr)

festivals_fr <- read_csv("Data/festivals_fr.csv")
names(festivals_fr)[1] <- "date"
attach(festivals_fr)

finance_fr <- read_csv("Data/finance_fr.csv")
names(finance_fr)[1] <- "date"
attach(finance_fr)

fitness_fr <- read_csv("Data/fitness_fr.csv")
names(fitness_fr)[1] <- "date"
attach(fitness_fr)

food_fr <- read_csv("Data/food_fr.csv")
names(food_fr)[1] <- "date"
attach(food_fr)

gambling_fr <- read_csv("Data/gambling_fr.csv")
names(gambling_fr)[1] <- "date"
attach(gambling_fr)

games_fr <- read_csv("Data/games_fr.csv")
names(games_fr)[1] <- "date"
attach(games_fr)

garderning_fr <- read_csv("Data/gardening_fr.csv")
names(garderning_fr)[1] <- "date"
attach(garderning_fr)

hairstyle_fr <- read_csv("Data/hairstyle_fr.csv")
names(hairstyle_fr)[1] <- "date"
attach(hairstyle_fr)

health_fr <- read_csv("Data/health_fr.csv")
names(health_fr)[1] <- "date"
attach(health_fr)

home_issues_fr <- read_csv("Data/home_issues_fr.csv")
names(home_issues_fr)[1] <- "date"
attach(home_issues_fr)

hotel_fr <- read_csv("Data/hotel_fr.csv")
names(hotel_fr)[1] <- "date"
attach(hotel_fr)

housing_fr <- read_csv("Data/housing_fr.csv")
names(housing_fr)[1] <- "date"
attach(housing_fr)

illnesses_fr <- read_csv("Data/illnesses_fr.csv")
names(illnesses_fr)[1] <- "date"
attach(illnesses_fr)

insurance_fr <- read_csv("Data/insurance_fr.csv")
names(insurance_fr)[1] <- "date"
attach(insurance_fr)

jewelry_fr <- read_csv("Data/jewelry_fr.csv")
names(jewelry_fr)[1] <- "date"
attach(jewelry_fr)

job_areas_fr <- read_csv("Data/job_areas_fr.csv")
names(job_areas_fr)[1] <- "date"
attach(job_areas_fr)

jobs_fr <- read_csv("Data/jobs_fr.csv")
names(jobs_fr)[1] <- "date"
attach(jobs_fr)

kitchen_supplies_fr <- read_csv("Data/kitchen_supplies_fr.csv")
names(kitchen_supplies_fr)[1] <- "date"
attach(kitchen_supplies_fr)

learning_fr <- read_csv("Data/learning_fr.csv")
names(learning_fr)[1] <- "date"
attach(learning_fr)

makeup_fr <- read_csv("Data/makeup_fr.csv")
names(makeup_fr)[1] <- "date"
attach(makeup_fr)

marijuana_drugs_fr <- read_csv("Data/marijuana_drugs_fr.csv")
names(marijuana_drugs_fr)[1] <- "date"
attach(marijuana_drugs_fr)

marketplace_fr <- read_csv("Data/marketplace_fr.csv")
names(marketplace_fr)[1] <- "date"
attach(marketplace_fr)

mental_health_fr <- read_csv("Data/mental_health_fr.csv")
names(mental_health_fr)[1] <- "date"
attach(mental_health_fr)

movie_genre_fr <- read_csv("Data/movie_genre_fr.csv")
names(movie_genre_fr)[1] <- "date"
attach(movie_genre_fr)

music_fr <- read_csv("Data/music_fr.csv")
names(music_fr)[1] <- "date"
attach(music_fr)

news_fr <- read_csv("Data/news_fr.csv")
names(news_fr)[1] <- "date"
attach(news_fr)

office_supplies_fr <- read_csv("Data/office_supplies_fr.csv")
names(office_supplies_fr)[1] <- "date"
attach(office_supplies_fr)

pantry_fr <- read_csv("Data/pantry_fr.csv")
names(pantry_fr)[1] <- "date"
attach(pantry_fr)

pets_fr <- read_csv("Data/pets_fr.csv")
names(pets_fr)[1] <- "date"
attach(pets_fr)

pharmaceutical_fr <- read_csv("Data/pharmaceutical_fr.csv")
names(pharmaceutical_fr)[1] <- "date"
attach(pharmaceutical_fr)

political_parties_fr <- read_csv("Data/political_parties_fr.csv")
names(political_parties_fr)[1] <- "date"
attach(political_parties_fr)

politicians_personalities_fr <- read_csv("Data/politicians_personalities_fr.csv")
names(politicians_personalities_fr)[1] <- "date"
attach(politicians_personalities_fr)

porn_fr <- read_csv("Data/porn_fr.csv")
names(porn_fr)[1] <- "date"
attach(porn_fr)

racial_ethnic_minorities_fr <- read_csv("Data/racial_ethnic_minorities_fr.csv")
names(racial_ethnic_minorities_fr)[1] <- "date"
attach(racial_ethnic_minorities_fr)

recipies_fr <- read_csv("Data/recipies_fr.csv")
names(recipies_fr)[1] <- "date"
attach(recipies_fr)

relationship_fr <- read_csv("Data/relationship_fr.csv")
names(relationship_fr)[1] <- "date"
attach(relationship_fr)

religion_fr <- read_csv("Data/religion_fr.csv")
names(religion_fr)[1] <- "date"
attach(religion_fr)

retail_fr <- read_csv("Data/retail_fr.csv")
names(retail_fr)[1] <- "date"
attach(retail_fr)

retail_2_fr <- read_csv("Data/retail_2_fr.csv")
names(retail_2_fr)[1] <- "date"
attach(retail_2_fr)

skin_care_fr <- read_csv("Data/skin_care_fr.csv")
names(skin_care_fr)[1] <- "date"
attach(skin_care_fr)

social_media_fr <- read_csv("Data/social_media_fr.csv")
names(social_media_fr)[1] <- "date"
attach(social_media_fr)

software_fr <- read_csv("Data/software_fr.csv")
names(software_fr)[1] <- "date"
attach(software_fr)

spices_fr <- read_csv("Data/spices_fr.csv")
names(spices_fr)[1] <- "date"
attach(spices_fr)

sports_fr <- read_csv("Data/sports_fr.csv")
names(sports_fr)[1] <- "date"
attach(sports_fr)

sports_teams_leagues_fr <- read_csv("Data/sports_teams_leagues_fr.csv")
names(sports_teams_leagues_fr)[1] <- "date"
attach(sports_teams_leagues_fr)

stis_fr <- read_csv("Data/stis.csv")
names(stis_fr)[1] <- "date"
attach(stis_fr)

transportation_fr <- read_csv("Data/transportation_fr.csv")
names(transportation_fr)[1] <- "date"
attach(transportation_fr)

travel_fr <- read_csv("Data/travel_fr.csv")
names(travel_fr)[1] <- "date"
attach(travel_fr)

vegetables_fr <- read_csv("Data/vegetables_fr.csv")
names(vegetables_fr)[1] <- "date"
attach(vegetables_fr)

wedding_fr <- read_csv("Data/wedding_fr.csv")
names(wedding_fr)[1] <- "date"
attach(wedding_fr)


###############################################
###############################################
getData <- function(category){
  
  if(category == "activities"){
    #1
    return(activities)
  }
  if(category == "alcohol"){
    #2
    return(alcohol)
  }
  if(category == "arts & entertainment"){
    #3
    return(arts_entertainment)
  }
  if(category == "banks"){
    #4
    return(banks)
  }
  if(category == "repair"){
    #5
    return(repair)
  }
  if(category == "bathroom supplies"){
    #6
    return(bathroom_supplies)
  }
  if(category == "caffeine"){
    #7
    return(caffeine)
  }
  if(category == "cars"){
    #8
    return(cars)
  }
  if(category == "charity"){
    #9
    return(charity)
  }
  if(category == "clothing stores"){
    #10
    return(clothing_stores)
  }
  if(category == "computers"){
    #11
    return(computers)
  }
  if(category == "dating"){
    #12
    return(dating)
  }
  if(category == "death"){
    #13
    return(death_)
  }
  if(category == "delivery"){
    #14
    return(delivery)
  }
  if(category == "diet"){
    #15
    return(diet_)
  }
  if(category == "drugs"){
    #16
    return(drugs)
  }
  if(category == "education"){
    #17
    return(education)
  }
  if(category == "environment"){
    #18
    return(environment)
  }
  if(category == "fast food restaurants"){
    #19
    return(fast_food_restaurants)
  }
  if(category == "feelings"){
    #20
    return(feelings)
  }
  if(category == "festivals"){
    #21
    return(festivals)
  }
  if(category == "finance"){
    #22
    return(finance)
  }
  if(category == "fitness"){
    #23
    return(fitness)
  }
  if(category == "food"){
    #24
    return(food)
  }
  if(category == "gambling"){
    #25
    return(gambling)
  }
  if(category == "games"){
    #26
    return(games)
  }
  if(category == "gardening"){
    #27
    return(garderning_)
  }
  if(category == "hairstyle"){
    #28
    return(hairstyle_)
  }
  if(category == "health"){
    #29
    return(health)
  }
  if(category == "home issues"){
    #30
    return(home_issues_)
  }
  if(category == "hotel"){
    #31
    return(hotel_)
  }
  if(category == "housing"){
    #32
    return(housing)
  }
  if(category == "illnesses"){
    #33
    return(illnesses)
  }
  if(category == "insurance"){
    #34
    return(insurance)
  }
  if(category == "jewelry"){
    #35
    return(jewelry_)
  }
  if(category == "job areas"){
    #36
    return(job_areas)
  }
  if(category == "jobs"){
    #37
    return(jobs)
  }
  if(category == "kitchen supplies"){
    #38
    return(kitchen_supplies)
  }
  if(category == "learning"){
    #39
    return(learning)
  }
  if(category == "makeup"){
    #40
    return(makeup)
  }
  if(category == "marijuana"){
    #41
    return(marijuana_drugs)
  }
  if(category == "marketplace"){
    #42
    return(marketplace)
  }
  if(category == "mental health"){
    #43
    return(mental_health)
  }
  if(category == "movie genre"){
    #44
    return(movie_genre)
  }
  if(category == "music"){
    #45
    return(music)
  }
  if(category == "news"){
    #46
    return(news)
  }
  if(category == "office supplies"){
    #47
    return(office_supplies)
  }
  if(category == "pantry"){
    #48
    return(pantry)
  }
  if(category == "pets"){
    #49
    return(pets)
  }
  if(category == "pharmaceutical"){
    #50
    return(pharmaceutical)
  }
  if(category == "political parties"){
    #51
    return(political_parties)
  }
  if(category == "politicians & personalities"){
    #52
    return(politicians_personalities)
  }
  if(category == "porn"){
    #53
    return(porn_)
  }
  if(category == "racial & ethinic minorities"){
    #54
    return(racial_ethnic_minorities)
  }
  if(category == "recipies"){
    #55
    return(recipies)
  }
  if(category == "relationship"){
    #56
    return(relationship_)
  }
  if(category == "religion"){
    #57
    return(religion)
  }
  if(category == "retail"){
    #58
    return(retail)
  }
  if(category == "retail 2"){
    #59
    return(retail_2)
  }
  if(category == "skin care"){
    #60
    return(skin_care)
  }
  if(category == "social media"){
    #61
    return(social_media)
  }
  if(category == "software"){
    #62
    return(software)
  }
  if(category == "spices"){
    #63
    return(spices)
  }
  if(category == "sports"){
    #64
    return(sports)
  }
  if(category == "sport teams & leagues"){
    #65
    return(sports_teams_leagues)
  }
  if(category == "stis"){
    #66
    return(stis)
  }
  if(category == "transportation"){
    #67
    return(transportation)
  }
  if(category == "travel"){
    #68
    return(travel)
  }
  if(category == "vegetables"){
    #69
    return(vegetables)
  }
  if(category == "wedding"){
    #70
    return(wedding)
  }
  return(NULL)
}

###############################################
###############################################

getData_fr <- function(category){
  
  if(category == "activités"){
    #1
    return(activities_fr)
  }
  if(category == "alcool"){
    #2
    return(alcohol_fr)
  }
  if(category == "culture & loisirs"){
    #3
    return(arts_entertainment_fr)
  }
  if(category == "banques"){
    #4
    return(banks_fr)
  }
  if(category == "réparation"){
    #5
    return(repair_fr)
  }
  if(category == "accessoires de salle de bain"){
    #6
    return(bathroom_supplies_fr)
  }
  if(category == "caféine"){
    #7
    return(caffeine_fr)
  }
  if(category == "voitures"){
    #8
    return(cars_fr)
  }
  if(category == "charité"){
    #9
    return(charity_fr)
  }
  if(category == "magasins de vêtements"){
    #10
    return(clothing_stores_fr)
  }
  if(category == "ordinateurs"){
    #11
    return(computers_fr)
  }
  if(category == "rencontres"){
    #12
    return(dating_fr)
  }
  if(category == "mort"){
    #13
    return(death_fr)
  }
  if(category == "livraison"){
    #14
    return(delivery_fr)
  }
  if(category == "régime"){
    #15
    return(diet_fr)
  }
  if(category == "drogues"){
    #16
    return(drugs_fr)
  }
  if(category == "éducation"){
    #17
    return(education_fr)
  }
  if(category == "environment"){
    #18
    return(environment_fr)
  }
  if(category == "restauration rapide"){
    #19
    return(fast_food_restaurants_fr)
  }
  if(category == "emotions"){
    #20
    return(feelings_fr)
  }
  if(category == "festivals"){
    #21
    return(festivals_fr)
  }
  if(category == "finance"){
    #22
    return(finance_fr)
  }
  if(category == "fitness"){
    #23
    return(fitness_fr)
  }
  if(category == "aliments"){
    #24
    return(food_fr)
  }
  if(category == "jeux d'argent"){
    #25
    return(gambling_fr)
  }
  if(category == "jeux"){
    #26
    return(games_fr)
  }
  if(category == "jardinage"){
    #27
    return(garderning_fr)
  }
  if(category == "coiffure"){
    #28
    return(hairstyle_fr)
  }
  if(category == "santé"){
    #29
    return(health_fr)
  }
  if(category == "problèmes à la maison"){
    #30
    return(home_issues_fr)
  }
  if(category == "hôtel"){
    #31
    return(hotel_fr)
  }
  if(category == "logement"){
    #32
    return(housing_fr)
  }
  if(category == "maladies"){
    #33
    return(illnesses_fr)
  }
  if(category == "assurance"){
    #34
    return(insurance_fr)
  }
  if(category == "bijoux"){
    #35
    return(jewelry_fr)
  }
  if(category == "domaines d'emploi"){
    #36
    return(job_areas_fr)
  }
  if(category == "emplois"){
    #37
    return(jobs_fr)
  }
  if(category == "accessoires de cuisine"){
    #38
    return(kitchen_supplies_fr)
  }
  if(category == "apprendre"){
    #39
    return(learning_fr)
  }
  if(category == "maquillage"){
    #40
    return(makeup_fr)
  }
  if(category == "marijuana"){
    #41
    return(marijuana_drugs_fr)
  }
  if(category == "marché"){
    #42
    return(marketplace_fr)
  }
  if(category == "santé mentale"){
    #43
    return(mental_health_fr)
  }
  if(category == "genre de film"){
    #44
    return(movie_genre_fr)
  }
  if(category == "musique"){
    #45
    return(music_fr)
  }
  if(category == "nouvelles"){
    #46
    return(news_fr)
  }
  if(category == "accessoires de bureau"){
    #47
    return(office_supplies_fr)
  }
  if(category == "garde-manger"){
    #48
    return(pantry_fr)
  }
  if(category == "animaux domestiques"){
    #49
    return(pets_fr)
  }
  if(category == "pharmaceutique"){
    #50
    return(pharmaceutical_fr)
  }
  if(category == "partis politiques"){
    #51
    return(political_parties_fr)
  }
  if(category == "politiciens et personnalités"){
    #52
    return(politicians_personalities_fr)
  }
  if(category == "porno"){
    #53
    return(porn_fr)
  }
  if(category == "minorités raciales et éthiniques"){
    #54
    return(racial_ethnic_minorities_fr)
  }
  if(category == "recettes"){
    #55
    return(recipies_fr)
  }
  if(category == "relations"){
    #56
    return(relationship_fr)
  }
  if(category == "religion"){
    #57
    return(religion_fr)
  }
  if(category == "vente au détail"){
    #58
    return(retail_fr)
  }
  if(category == "vente au détail 2"){
    #59
    return(retail_2_fr)
  }
  if(category == "soin de la peau"){
    #60
    return(skin_care_fr)
  }
  if(category == "médias sociaux"){
    #61
    return(social_media_fr)
  }
  if(category == "logiciel"){
    #62
    return(software_fr)
  }
  if(category == "épices"){
    #63
    return(spices_fr)
  }
  if(category == "sports"){
    #64
    return(sports_fr)
  }
  if(category == "équipes et ligues sportives"){
    #65
    return(sports_teams_leagues_fr)
  }
  if(category == "itss"){
    #66
    return(stis_fr)
  }
  if(category == "transport"){
    #67
    return(transportation_fr)
  }
  if(category == "voyage"){
    #68
    return(travel_fr)
  }
  if(category == "légumes"){
    #69
    return(vegetables_fr)
  }
  if(category == "mariage"){
    #70
    return(wedding_fr)
  }
  return(NULL)
}


###############################################
###############################################

getData_fr <- function(category){
  
  if(category == "activités"){
    #1
    return(activities_fr)
  }
  if(category == "alcool"){
    #2
    return(alcohol_fr)
  }
  if(category == "culture & loisirs"){
    #3
    return(arts_entertainment_fr)
  }
  if(category == "banques"){
    #4
    return(banks_fr)
  }
  if(category == "réparation"){
    #5
    return(repair_fr)
  }
  if(category == "accessoires de salle de bain"){
    #6
    return(bathroom_supplies_fr)
  }
  if(category == "caféine"){
    #7
    return(caffeine_fr)
  }
  if(category == "voitures"){
    #8
    return(cars_fr)
  }
  if(category == "charité"){
    #9
    return(charity_fr)
  }
  if(category == "magasins de vêtements"){
    #10
    return(clothing_stores_fr)
  }
  if(category == "ordinateurs"){
    #11
    return(computers_fr)
  }
  if(category == "rencontres"){
    #12
    return(dating_fr)
  }
  if(category == "mort"){
    #13
    return(death_fr)
  }
  if(category == "livraison"){
    #14
    return(delivery_fr)
  }
  if(category == "régime"){
    #15
    return(diet_fr)
  }
  if(category == "drogues"){
    #16
    return(drugs_fr)
  }
  if(category == "éducation"){
    #17
    return(education_fr)
  }
  if(category == "environment"){
    #18
    return(environment_fr)
  }
  if(category == "restauration rapide"){
    #19
    return(fast_food_restaurants_fr)
  }
  if(category == "emotions"){
    #20
    return(feelings_fr)
  }
  if(category == "festivals"){
    #21
    return(festivals_fr)
  }
  if(category == "finance"){
    #22
    return(finance_fr)
  }
  if(category == "fitness"){
    #23
    return(fitness_fr)
  }
  if(category == "aliments"){
    #24
    return(food_fr)
  }
  if(category == "jeux d'argent"){
    #25
    return(gambling_fr)
  }
  if(category == "jeux"){
    #26
    return(games_fr)
  }
  if(category == "jardinage"){
    #27
    return(garderning_fr)
  }
  if(category == "coiffure"){
    #28
    return(hairstyle_fr)
  }
  if(category == "santé"){
    #29
    return(health_fr)
  }
  if(category == "problèmes à la maison"){
    #30
    return(home_issues_fr)
  }
  if(category == "hôtel"){
    #31
    return(hotel_fr)
  }
  if(category == "logement"){
    #32
    return(housing_fr)
  }
  if(category == "maladies"){
    #33
    return(illnesses_fr)
  }
  if(category == "assurance"){
    #34
    return(insurance_fr)
  }
  if(category == "bijoux"){
    #35
    return(jewelry_fr)
  }
  if(category == "domaines d'emploi"){
    #36
    return(job_areas_fr)
  }
  if(category == "emplois"){
    #37
    return(jobs_fr)
  }
  if(category == "accessoires de cuisine"){
    #38
    return(kitchen_supplies_fr)
  }
  if(category == "apprendre"){
    #39
    return(learning_fr)
  }
  if(category == "maquillage"){
    #40
    return(makeup_fr)
  }
  if(category == "marijuana"){
    #41
    return(marijuana_drugs_fr)
  }
  if(category == "marché"){
    #42
    return(marketplace_fr)
  }
  if(category == "santé mentale"){
    #43
    return(mental_health_fr)
  }
  if(category == "genre de film"){
    #44
    return(movie_genre_fr)
  }
  if(category == "musique"){
    #45
    return(music_fr)
  }
  if(category == "nouvelles"){
    #46
    return(news_fr)
  }
  if(category == "accessoires de bureau"){
    #47
    return(office_supplies_fr)
  }
  if(category == "garde-manger"){
    #48
    return(pantry_fr)
  }
  if(category == "animaux domestiques"){
    #49
    return(pets_fr)
  }
  if(category == "pharmaceutique"){
    #50
    return(pharmaceutical_fr)
  }
  if(category == "partis politiques"){
    #51
    return(political_parties_fr)
  }
  if(category == "politiciens et personnalités"){
    #52
    return(politicians_personalities_fr)
  }
  if(category == "porno"){
    #53
    return(porn_fr)
  }
  if(category == "minorités raciales et éthiniques"){
    #54
    return(racial_ethnic_minorities_fr)
  }
  if(category == "recettes"){
    #55
    return(recipies_fr)
  }
  if(category == "relations"){
    #56
    return(relationship_fr)
  }
  if(category == "religion"){
    #57
    return(religion_fr)
  }
  if(category == "vente au détail"){
    #58
    return(retail_fr)
  }
  if(category == "vente au détail 2"){
    #59
    return(retail_2_fr)
  }
  if(category == "soin de la peau"){
    #60
    return(skin_care_fr)
  }
  if(category == "médias sociaux"){
    #61
    return(social_media_fr)
  }
  if(category == "logiciel"){
    #62
    return(software_fr)
  }
  if(category == "épices"){
    #63
    return(spices_fr)
  }
  if(category == "sports"){
    #64
    return(sports_fr)
  }
  if(category == "équipes et ligues sportives"){
    #65
    return(sports_teams_leagues_fr)
  }
  if(category == "itss"){
    #66
    return(stis_fr)
  }
  if(category == "transport"){
    #67
    return(transportation_fr)
  }
  if(category == "voyage"){
    #68
    return(travel_fr)
  }
  if(category == "légumes"){
    #69
    return(vegetables_fr)
  }
  if(category == "mariage"){
    #70
    return(wedding_fr)
  }
  return(NULL)
}
###############################################

