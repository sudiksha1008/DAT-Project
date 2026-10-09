source("R/data.R")
source("R/analysis.R")
source("R/plots.R")

library(shiny)

ui <- fluidPage(
  
  titlePanel("Social Media Analytics Dashboard"),
  
  sidebarLayout(
    
    sidebarPanel(
      
      selectInput(
        "platform",
        "Select Platform:",
        choices = c(
          "Twitter",
          "Instagram",
          "YouTube"
        )
      )
      
    ),
    
    mainPanel(
      
      h3("Social Media Analysis"),
      
      plotOutput("mainPlot"),
      
      tableOutput("summaryTable")
      
    )
  )
)

server <- function(input, output) {
  
  output$mainPlot <- renderPlot({
    
    if (input$platform == "Twitter") {
      
      twitter_sentiment_bar()
      
    } else if (input$platform == "Instagram") {
      
      instagram_category_bar()
      
    } else {
      
      youtube_category_bar()
      
    }
    
  })
  
  output$summaryTable <- renderTable({
    
    if (input$platform == "Twitter") {
      
      twitter_sentiment_summary
      
    } else if (input$platform == "Instagram") {
      
      instagram_category_summary
      
    } else {
      
      youtube_category_summary
      
    }
    
  })
  
}

shinyApp(
  ui = ui,
  server = server
)