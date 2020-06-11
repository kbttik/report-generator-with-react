
library(httr)
library(readr)

# read html to string
# html_text <- readLines(file("from_report/test_from.html", "r", encoding = "UTF-8"))
html_text <- readr::read_file("from_report/test_from.html")

# POST
httr::POST(url = "http://localhost:8994/printer", body = html_text, encode = "raw")
