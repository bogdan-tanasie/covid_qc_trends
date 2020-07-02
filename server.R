#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(grid)
library(shinyjs)
library(tableHTML)
library(plotly)
library(tidyverse)
library(rsconnect)
library(extrafont)
library(car)
library(lubridate)
library(lme4)

require(ggplot2)
require(stringi)
require(ggthemes)

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
            label = "Mot-clé",
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
            label = "Mot-clé",
            choices = c(colnames(subset(getData_fr(input$category2fr), select=-date)))
        )
    })

   output$stats1a = renderUI({ 
        req(input$category1)
        v$data <- getData(input$category1)
        req(input$keyword1)
        print(as.numeric(date))
        print(eval(as.symbol(input$keyword1)))
        localReg <- loess(eval(as.symbol(input$keyword1))~as.numeric(date), span=0.18)
        paste("First Canada case: ", round((predict(localReg, 18296.04)-predict(localReg, 18286.04))/predict(localReg, 18286.04)*100, digits=2))
   })
   
   output$stats2a = renderUI({ 
       req(input$category1)
       v$data <- getData(input$category1)
       req(input$keyword1)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1)))
       localReg <- loess(eval(as.symbol(input$keyword1))~as.numeric(date), span=0.18)
       paste("First Quebec case: ", round((predict(localReg, 18328.95)-predict(localReg, 18318.95))/predict(localReg, 18318.95)*100, digits=2))
   })
   
   output$stats3a = renderUI({ 
       req(input$category1)
       v$data <- getData(input$category1)
       req(input$keyword1)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1)))
       localReg <- loess(eval(as.symbol(input$keyword1))~as.numeric(date), span=0.18)
       paste("Start of province shutdown: ", round((predict(localReg, 18344)-predict(localReg, 18334))/predict(localReg, 18334)*100, digits=2))
   })
   
   output$stats4a = renderUI({ 
       req(input$category1)
       v$data <- getData(input$category1)
       req(input$keyword1)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1)))
       localReg <- loess(eval(as.symbol(input$keyword1))~as.numeric(date), span=0.18)
       paste("Bigger gatherings permitted: ", round((predict(localReg, 18412.35)-predict(localReg, 18402.35))/predict(localReg, 18402.35)*100, digits=2))
   })
   
   output$stats1b = renderUI({ 
       req(input$category2)
       v$data2 <- getData(input$category2)
       req(input$keyword2)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2)))
       localReg <- loess(eval(as.symbol(input$keyword2))~as.numeric(date), span=0.18)
       paste("First Canada case: ", round((predict(localReg, 18296.04)-predict(localReg, 18286.04))/predict(localReg, 18286.04)*100, digits=2))
   })
   
   output$stats2b = renderUI({ 
       req(input$category2)
       v$data2 <- getData(input$category2)
       req(input$keyword2)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2)))
       localReg <- loess(eval(as.symbol(input$keyword2))~as.numeric(date), span=0.18)
       paste("First Quebec case: ", round((predict(localReg, 18328.95)-predict(localReg, 18318.95))/predict(localReg, 18318.95)*100, digits=2))
   })
   
   output$stats3b = renderUI({ 
       req(input$category2)
       v$data2 <- getData(input$category2)
       req(input$keyword2)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2)))
       localReg <- loess(eval(as.symbol(input$keyword2))~as.numeric(date), span=0.18)
       paste("Start of province shutdown: ", round((predict(localReg, 18344)-predict(localReg, 18334))/predict(localReg, 18334)*100, digits=2))
   })
   
   output$stats4b = renderUI({ 
       req(input$category2)
       v$data2 <- getData(input$category2)
       req(input$keyword2)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2)))
       localReg <- loess(eval(as.symbol(input$keyword2))~as.numeric(date), span=0.18)
       paste("Bigger gatherings permitted: ", round((predict(localReg, 18412.35)-predict(localReg, 18402.35))/predict(localReg, 18402.35)*100, digits=2))
   })
   
   output$stats1afr = renderUI({ 
       req(input$category1fr)
       v$data <- getData_fr(input$category1fr)
       req(input$keyword1fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1fr)))
       localReg <- loess(eval(as.symbol(input$keyword1fr))~as.numeric(date), span=0.18)
       paste("Premier cas au Canada: ", round((predict(localReg, 18296.04)-predict(localReg, 18286.04))/predict(localReg, 18286.04)*100, digits=2))
   })
   
   output$stats2afr = renderUI({ 
       req(input$category1fr)
       v$data <- getData_fr(input$category1fr)
       req(input$keyword1fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1fr)))
       localReg <- loess(eval(as.symbol(input$keyword1fr))~as.numeric(date), span=0.18)
       paste("Premier cas au Québec: ", round((predict(localReg, 18328.95)-predict(localReg, 18318.95))/predict(localReg, 18318.95)*100, digits=2))
   })
   
   output$stats3afr = renderUI({ 
       req(input$category1fr)
       v$data <- getData_fr(input$category1fr)
       req(input$keyword1fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1fr)))
       localReg <- loess(eval(as.symbol(input$keyword1fr))~as.numeric(date), span=0.18)
       paste("Fermeture de la province:  ", round((predict(localReg, 18344)-predict(localReg, 18334))/predict(localReg, 18334)*100, digits=2))
   })
   
   output$stats4afr = renderUI({ 
       req(input$category1fr)
       v$data <- getData_fr(input$category1fr)
       req(input$keyword1fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword1fr)))
       localReg <- loess(eval(as.symbol(input$keyword1fr))~as.numeric(date), span=0.18)
       paste("Rassemblements permis: ", round((predict(localReg, 18412.35)-predict(localReg, 18402.35))/predict(localReg, 18402.35)*100, digits=2))
   })
   
   output$stats1bfr = renderUI({ 
       req(input$category2fr)
       v$data2 <- getData_fr(input$category2fr)
       req(input$keyword2fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2fr)))
       localReg <- loess(eval(as.symbol(input$keyword2fr))~as.numeric(date), span=0.18)
       paste("Premier cas au Canada: ", round((predict(localReg, 18296.04)-predict(localReg, 18286.04))/predict(localReg, 18286.04)*100, digits=2))
   })
   
   output$stats2bfr = renderUI({ 
       req(input$category2fr)
       v$data2 <- getData_fr(input$category2fr)
       req(input$keyword2fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2fr)))
       localReg <- loess(eval(as.symbol(input$keyword2fr))~as.numeric(date), span=0.18)
       paste("Premier cas au Québec: ", round((predict(localReg, 18328.95)-predict(localReg, 18318.95))/predict(localReg, 18318.95)*100, digits=2))
   })
   
   output$stats3bfr = renderUI({ 
       req(input$category2fr)
       v$data2 <- getData_fr(input$category2fr)
       req(input$keyword2fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2fr)))
       localReg <- loess(eval(as.symbol(input$keyword2fr))~as.numeric(date), span=0.18)
       paste("Fermeture de la province:  ", round((predict(localReg, 18344)-predict(localReg, 18334))/predict(localReg, 18334)*100, digits=2))
   })
   
   output$stats4bfr = renderUI({ 
       req(input$category2fr)
       v$data2 <- getData_fr(input$category2fr)
       req(input$keyword2fr)
       print(as.numeric(date))
       print(eval(as.symbol(input$keyword2fr)))
       localReg <- loess(eval(as.symbol(input$keyword2fr))~as.numeric(date), span=0.18)
       paste("Rassemblements permis: ", round((predict(localReg, 18412.35)-predict(localReg, 18402.35))/predict(localReg, 18402.35)*100, digits=2))
   })
   

    # ENGLISH
    # Output main plot
    output$graph1 <- renderPlotly({
        req(input$category1)
        v$data <<- getData(input$category1)
        #if(is.null(v$data)) return()
        req(input$keyword1)
        ggplotly(ggplot(v$data, aes(x=date, y=eval(as.symbol(input$keyword1))), family="Garamond") +
                     ggtitle(input$keyword1) + ylab("search interest") + xlab("date") + 
                     geom_point(col="#ADD8E6") + geom_smooth(span=0.18, size=1, se=FALSE) +
                     theme_bw() + theme(panel.background=element_rect(fill="#F0F0F0")) +
                     theme(plot.background=element_rect(fill="#F0F0F0")) +
                     theme(panel.border=element_rect(colour="#F0F0F0")) +
                     geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "#000080") + 
                     geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "#C71585")  +
                     geom_vline(aes(xintercept = 18334), linetype = 2, colour = "#9400D3") +
                     geom_vline(aes(xintercept = 18402.35), linetype = 2, colour = "#2E8B57") +
                     theme(panel.grid.major=element_line(colour="#D0D0D0",size=.75)) +
                     theme(axis.ticks=element_blank()) +
                     theme(legend.position="none") +
                     theme(plot.title=element_text(face="bold",hjust=-.08,vjust=2,colour="#3C3C3C",size=14)) +
                     theme(axis.text.x=element_text(size=11,colour="#535353")) +
                     theme(axis.text.y=element_text(size=11,colour="#535353")) +
                     theme(axis.title.y=element_text(size=11,colour="#535353", vjust=1.5)) +
                     theme(axis.title.x=element_text(size=11,colour="#535353", vjust=-.5)) +
                     theme(plot.margin = unit(c(1, 1, .5, .7), "cm")) 
        )
        
    })
    # Output compare plot
    output$graph2 <- renderPlotly({
        req(input$category2)
        v$data2 <<- getData(input$category2)
        #if(is.null(v$data)) return()
        req(input$keyword2)
        ggplotly(ggplot(v$data2, aes_string(x=date, y=eval(as.symbol(input$keyword2))), family="Garamond") + 
                     ggtitle(input$keyword2) + ylab("intérêt de recherche") + xlab("date") +
                     geom_point(col="#ADD8E6") + geom_smooth(span=0.18, size=1, se=FALSE) +
                     theme_bw() + theme(panel.background=element_rect(fill="#F0F0F0")) +
                     theme(plot.background=element_rect(fill="#F0F0F0")) +
                     theme(panel.border=element_rect(colour="#F0F0F0")) +
                     geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "#000080") + 
                     geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "#C71585")  +
                     geom_vline(aes(xintercept = 18334), linetype = 2, colour = "#9400D3") +
                     geom_vline(aes(xintercept = 18402.35), linetype = 2, colour = "#2E8B57") +
                     theme(panel.grid.major=element_line(colour="#D0D0D0",size=.75)) +
                     theme(axis.ticks=element_blank()) +
                     theme(legend.position="none") +
                     theme(plot.title=element_text(face="bold",hjust=-.08,vjust=1,colour="#3C3C3C",size=14)) +
                     theme(axis.text.x=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.text.y=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.title.y=element_text(size=11,colour="#535353",face="bold" ,vjust=1.5)) +
                     theme(axis.title.x=element_text(size=11,colour="#535353",face="bold", vjust=-.5)) +
                     theme(plot.margin = unit(c(1, 1, .5, .7), "cm")) 
        )
    })
    
    #FRENCH
    # Output main plot
    output$graph1fr <- renderPlotly({
        req(input$category1fr)
        v$data <<- getData_fr(input$category1fr)
        #if(is.null(v$data)) return()
        req(input$keyword1fr)
        ggplotly(ggplot(v$data, aes_string(x=date, y=eval(as.symbol(input$keyword1fr))), family="Garamond") + 
                     ggtitle(input$keyword1fr) + ylab("intérêt de recherche") + 
                     xlab("date") + geom_point(col="#ADD8E6") + geom_smooth(span=0.18, size=1, se=FALSE) +
                     theme_bw() + theme(panel.background=element_rect(fill="#F0F0F0")) +
                     theme(plot.background=element_rect(fill="#F0F0F0")) +
                     theme(panel.border=element_rect(colour="#F0F0F0")) +
                     geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "#000080") + 
                     geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "#C71585")  +
                     geom_vline(aes(xintercept = 18334), linetype = 2, colour = "#9400D3") +
                     geom_vline(aes(xintercept = 18402.35), linetype = 2, colour = "#2E8B57") + 
                     theme(panel.grid.major=element_line(colour="#D0D0D0",size=.75)) +
                     theme(axis.ticks=element_blank()) +
                     theme(legend.position="none") +
                     theme(plot.title=element_text(face="bold",hjust=-.08,vjust=2,colour="#3C3C3C",size=14)) +
                     theme(axis.text.x=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.text.y=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.title.y=element_text(size=11,colour="#535353",face="bold", vjust=1.5)) +
                     theme(axis.title.x=element_text(size=11,colour="#535353",face="bold", vjust=-.5)) +
                     theme(plot.margin = unit(c(1, 1, .5, .7), "cm")) 
        )
    })
    # Output compare plot
    output$graph2fr <- renderPlotly({
        req(input$category2fr)
        v$data2 <<- getData_fr(input$category2fr) 
        #if(is.null(v$data)) return()
        req(input$keyword2fr)
        ggplotly(ggplot(v$data2, aes_string(x=date, y=eval(as.symbol(input$keyword2fr))), family="Garamond") + 
                     ggtitle(input$keyword2fr) + ylab("search interest") + xlab("date") + 
                     geom_point(col="#ADD8E6") + geom_smooth(span=0.18, size=1, se=FALSE) +
                     theme_bw() + theme(panel.background=element_rect(fill="#F0F0F0")) +
                     theme(plot.background=element_rect(fill="#F0F0F0")) +
                     theme(panel.border=element_rect(colour="#F0F0F0")) +
                     geom_vline(aes(xintercept = 18286.04), linetype = 2, colour = "#000080") + 
                     geom_vline(aes(xintercept = 18318.95), linetype = 2, colour = "#C71585")  +
                     geom_vline(aes(xintercept = 18334), linetype = 2, colour = "#9400D3") +
                     geom_vline(aes(xintercept = 18402.35), linetype = 2, colour = "#2E8B57") + 
                     theme(panel.grid.major=element_line(colour="#D0D0D0",size=.75)) +
                     theme(axis.ticks=element_blank()) +
                     theme(legend.position="none") +
                     theme(plot.title=element_text(face="bold",hjust=-.08,vjust=2,colour="#3C3C3C",size=14)) +
                     theme(axis.text.x=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.text.y=element_text(size=11,colour="#535353",face="bold")) +
                     theme(axis.title.y=element_text(size=11,colour="#535353",face="bold", vjust=1.5)) +
                     theme(axis.title.x=element_text(size=11,colour="#535353",face="bold", vjust=-.5)) +
                     theme(plot.margin = unit(c(1, 1, .5, .7), "cm")) 
        )
    })
}



