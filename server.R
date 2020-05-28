#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinyjs)
library(tableHTML)
library(plotly)
library(tidyverse)
library(rsconnect)

require(ggplot2)
require(stringi)

source("load_data.R")

# Define server logic required to draw a histogram
function(input, output, session) {
    v <- reactiveValues(data = NULL, data2 = NULL)
    # Observe change in category and update second selection
    observeEvent(input$category1,{
        updateSelectInput(
            session,
            "keyword1",
            label = "Keyword",
            choices = c(colnames(subset(getData(input$category1), select=-date)))
        )
    })
    
    observeEvent(input$category1fr,{
        updateSelectInput(
            session,
            "keyword1fr",
            label = "Keyword",
            choices = c(colnames(subset(getData_fr(input$category1fr), select=-date)))
        )
    })
    
    observe({
        updateSelectInput(
            session,
            "keyword2",
            label = "Keyword",
            choices = c(colnames(subset(getData(input$category2), select=-date)))
        )
        
        updateSelectInput(
            session,
            "keyword2fr",
            label = "Keyword",
            choices = c(colnames(subset(getData_fr(input$category2fr), select=-date)))
        )
   
    })
    
    # ENGLISH
    # Output main plot
    output$graph1 <- renderPlotly({
        req(input$category1)
        v$data <<- getData(input$category1)
        #if(is.null(v$data)) return()
        req(input$keyword1)
        ggplotly(ggplot(v$data, aes(x=date, y=eval(as.symbol(input$keyword1)))) + ggtitle(input$keyword1) + ylab("search interest") + xlab("date") + geom_point(col="gray") + geom_smooth() +
                    theme_bw() + geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "green") + geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "yellow")  +
                    geom_vline(aes(xintercept = 18329.75), linetype = 2, colour = "orange") + geom_vline(aes(xintercept = 18334), linetype = 2, colour = "red")) 
       
        
    })
    # Output compare plot
    output$graph2 <- renderPlotly({
        req(input$category2)
        v$data2 <<- getData(input$category2)
        #if(is.null(v$data)) return()
        req(input$keyword2)
        req(input$keyword2)
        ggplotly(ggplot(v$data2, aes_string(x=date, y=eval(as.symbol(input$keyword2)))) + ggtitle(input$keyword2) + ylab("intérêt de recherche") + xlab("date") + geom_point(col="gray") + geom_smooth() +
                     theme_bw() + geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "green") + geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "yellow")  +
                     geom_vline(aes(xintercept = 18329.75), linetype = 2, colour = "orange") + geom_vline(aes(xintercept = 18334), linetype = 2, colour = "red"))
    })
    
    #FRENCH
    # Output main plot
    output$graph1fr <- renderPlotly({
        req(input$category1fr)
        v$data <<- getData_fr(input$category1fr)
        #if(is.null(v$data)) return()
        req(input$keyword1fr)
        ggplotly(ggplot(v$data, aes_string(x=date, y=eval(as.symbol(input$keyword1fr)))) + ggtitle(input$keyword1fr) + ylab("intérêt de recherche") + xlab("date") + geom_point(col="gray") + geom_smooth() +
                     theme_bw() + geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "green") + geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "yellow")  +
                     geom_vline(aes(xintercept = 18329.75), linetype = 2, colour = "orange") + geom_vline(aes(xintercept = 18334), linetype = 2, colour = "red")) 
        
        
    })
    # Output compare plot
    output$graph2fr <- renderPlotly({
        req(input$category2fr)
        v$data2 <<- getData_fr(input$category2fr) 
        #if(is.null(v$data)) return()
        req(input$keyword2fr)
        ggplotly(ggplot(v$data2, aes_string(x=date, y=eval(as.symbol(input$keyword2fr)))) + ggtitle(input$keyword2fr) + ylab("search interest") + xlab("date") + geom_point(col="gray") + geom_smooth() +
                     theme_bw() + geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "green") + geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "yellow")  +
                     geom_vline(aes(xintercept = 18329.75), linetype = 2, colour = "orange") + geom_vline(aes(xintercept = 18334), linetype = 2, colour = "red"))
    })
}

