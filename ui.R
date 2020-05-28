library(shiny)
library(shinyjs)
library(tableHTML)
library(plotly)

# Define UI for application that draws a histogram
fluidPage(
  radioButtons("lang",
               label = "",
               choices = c("English" = "en", "Français" = "fr"),
  ),
  hr(),
  # Application title
  useShinyjs(),
  
  conditionalPanel(
    condition = "input.lang == 'en'",
    titlePanel("Quebec Google Trends Analysis"),
  ),
  conditionalPanel(
    condition = "input.lang == 'fr'",
    titlePanel("Analyse Google Trends au Québec"),
  ),
  
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      # ENGLISH
      conditionalPanel(
        condition = "input.lang == 'en'",
        
        helpText("Select a category and keyword you would like to explore."),
        selectInput("category1", 
                    label = "Category", 
                    choices = list("activities","alcohol", "arts & entertainment", "banks", "repair",
                                   "bathroom supplies", "caffeine", "cars", "charity", "clothing stores", "computers",
                                   "dating", "death", "delivery", "diet", "drugs", "education", "environment", "fast food restaurants",
                                   "feelings", "festivals", "finance", "fitness", "food", "gambling", "games", "gardening", "hairstyle",
                                   "health", "home issues", "hotel", "housing", "illnesses", "insurance", "jewelry", "job areas", "jobs", 
                                   "kitchen supplies", "learning", "makeup", "marijuana", "marketplace", "mental health", "movie genre",
                                   "music", "news", "office supplies", "pantry", "pets", "pharmaceutical", "political parties", 
                                   "politicians & personalities","porn", "racial & ethinic minorities", "recipies", "relationship", "religion",
                                   "retail", "retail 2", "skin care", "social media", "software", "spices", "sports", "sport teams & leagues",
                                   "stis", "transportation", "travel", "vegetables", "wedding"
                    ), 
                    selected = NULL),
        
        selectInput("keyword1", 
                    label = "Keyword", 
                    choices = NULL),
        
        checkboxInput("compare","Check to compare graphs", FALSE), 
        
        conditionalPanel(
          condition = "input.compare && input.lang == 'en'",
          hr(),
          helpText("Select a category and keyword you would like to compare."),
          selectInput("category2", 
                      label = "Category", 
                      choices = list("activities","alcohol", "arts & entertainment", "banks", "repair",
                                     "bathroom supplies", "caffeine", "cars", "charity", "clothing stores", "computers",
                                     "dating", "death", "delivery", "diet", "drugs", "education", "environment", "fast food restaurants",
                                     "feelings", "festivals", "finance", "fitness", "food", "gambling", "games", "gardening", "hairstyle",
                                     "health", "home issues", "hotel", "housing", "illnesses", "insurance", "jewelry", "job areas", "jobs", 
                                     "kitchen supplies", "learning", "makeup", "marijuana", "marketplace", "mental health", "movie genre",
                                     "music", "news", "office supplies", "pantry", "pets", "pharmaceutical", "political parties", 
                                     "politicians & personalities","porn", "racial & ethinic minorities", "recipies", "relationship", "religion",
                                     "retail", "retail 2", "skin care", "social media", "software", "spices", "sports", "sport teams & leagues",
                                     "stis", "transportation", "travel", "vegetables", "wedding"
                      ),  
                      selected = NULL),
          
          selectInput("keyword2", 
                      label = "Keyword", 
                      choices = NULL),
        ),
        hr(),
        HTML('<p style="font-weight: bold; color:black;">Legend:</p>'),
        HTML('<p style="display:inline; color:black;">First Canada case:</p>'), 
        HTML('<p style="display:inline; color:green;">Green</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">First Quebec case:</p>'), 
        HTML('<p style="display:inline; color:yellow;">Yellow</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">First testing clinics:</p>'), 
        HTML('<p style="display:inline; color:orange;">Orange</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">Full province shutdown:</p>'), 
        HTML('<p style="display:inline; color:red;">Red</p>'),
        p(),
        p(),
        helpText("Source: https://trends.google.com/trends/?geo=CA-QC"),
      ),
      
      # FRENCH
      conditionalPanel(
        condition = "input.lang == 'fr'",
        helpText("Sélectionnez une catégorie et un mot-clé que vous souhaitez explorer."),
        selectInput("category1fr", 
                    label = "Catégorie", 
                    choices = list("activités","alcool", "culture & loisirs", "banques", "réparation",
                                   "accessoires de salle de bain", "caféine", "voitures", "charité", "magasins de vêtements", "ordinateurs",
                                   "rencontres", "mort", "livraison", "régime", "drogues", "éducation", "environment", "restauration rapide",
                                   "emotions", "festivals", "finance", "fitness", "aliments", "jeux d'argent", "jeux", "jardinage", "coiffure",
                                   "santé", "problèmes à la maison", "hôtel", "logement", "maladies", "assurance", "bijoux", "domaines d'emploi", "emplois", 
                                   "accessoires de cuisine", "apprendre", "maquillage", "marijuana", "marché", "santé mentale", "genre de film",
                                   "musique", "nouvelles", "accessoires de bureau", "garde-manger", "animaux domestiques", "pharmaceutique", "partis politiques", 
                                   "politiciens et personnalités","porno", "minorités raciales et éthiniques", "recettes", "relations", "religion",
                                   "vente au détail", "vente au détail 2", "soin de la peau", "médias sociaux", "logiciel", "épices", "sports", "équipes et ligues sportives",
                                   "itss", "transport", "voyage", "légumes", "mariage"
                    ), 
                    selected = NULL),
        
        selectInput("keyword1fr", 
                    label = "Mot-clé", 
                    choices = NULL),
        
        checkboxInput("comparefr","Comparer les graphiques.", FALSE), 
        
        conditionalPanel(
          condition = "input.comparefr && input.lang == 'fr'",
          hr(),
          helpText("Sélectionnez une catégorie et un mot-clé que vous souhaitez comparer."),
          selectInput("category2fr", 
                      label = "Catégorie", 
                      choices = list("activités","alcool", "culture & loisirs", "banques", "réparation",
                                     "accessoires de salle de bain", "caféine", "voitures", "charité", "magasins de vêtements", "ordinateurs",
                                     "rencontres", "mort", "livraison", "régime", "drogues", "éducation", "environment", "restauration rapide",
                                     "emotions", "festivals", "finance", "fitness", "aliments", "jeux d'argent", "jeux", "jardinage", "coiffure",
                                     "santé", "problèmes à la maison", "hôtel", "logement", "maladies", "assurance", "bijoux", "domaines d'emploi", "emplois", 
                                     "accessoires de cuisine", "apprendre", "maquillage", "marijuana", "marché", "santé mentale", "genre de film",
                                     "musique", "nouvelles", "accessoires de bureau", "garde-manger", "animaux domestiques", "pharmaceutique", "partis politiques", 
                                     "politiciens et personnalités","porno", "minorités raciales et éthiniques", "recettes", "relations", "religion",
                                     "vente au détail", "vente au détail 2", "soin de la peau", "médias sociaux", "logiciel", "épices", "sports", "équipes et ligues sportives",
                                     "itss", "transport", "voyage", "légumes", "mariage"
                      ),  
                      selected = NULL),
          
          selectInput("keyword2fr", 
                      label = "Mot-clé", 
                      choices = NULL),
        ),
        hr(),
        HTML('<p style="font-weight: bold; color:black;">Légende:</p>'),
        HTML('<p style="display:inline; color:black;">Premier cas au Canada:</p>'), 
        HTML('<p style="display:inline; color:green;">Vert</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">Premier cas au Québec:</p>'), 
        HTML('<p style="display:inline; color:yellow;">Jaune</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">Premières cliniques de tests:</p>'), 
        HTML('<p style="display:inline; color:orange;">Orange</p>'),
        p(),
        HTML('<p style="display:inline; color:black;">Fermeture complète de la province:</p>'), 
        HTML('<p style="display:inline; color:red;">Rouge</p>'),
        p(),
        p(),
        helpText("Source: https://trends.google.com/trends/?geo=CA-QC"),
      )
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      conditionalPanel(
        condition = "input.lang == 'en'",
        plotlyOutput("graph1"),
        hr(),
      ),
      conditionalPanel(
        condition = "input.compare && input.lang == 'en'",
        plotlyOutput("graph2")
      ),
      conditionalPanel(
        condition = "input.lang == 'fr'",
        plotlyOutput("graph1fr"),
        hr(),
      ),
      conditionalPanel(
        condition = "input.comparefr && input.lang == 'fr'",
        plotlyOutput("graph2fr")
      ),
    )
  )
)