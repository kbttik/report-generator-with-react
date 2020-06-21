
library(httr)
library(readr)

# read html to string
# html_text <- readLines(file("from_report/test_from.html", "r", encoding = "UTF-8"))
html_text <- readr::read_file("from_report/test_from.html")
test_tags <- c("テスト", "good", "analysis")

# POST
#httr::POST(url = "http://localhost:8994/printer", body = html_text, encode = "raw")
#httr::POST(url = "http://localhost:8994/printer", body = upload_file(path = "from_report/test_from.html", type = "txt"), encode = "raw")
#httr::POST(url = "http://localhost:8994/printer", body = list(html = upload_file(path = "from_report/test_from.html", type = "txt")), httr::add_headers(title = "テストレポート"), httr::add_headers(tags = paste(test_tags, collapse = ",")), encode = "multipart")

httr::POST(url = "http://localhost:8994/printer", body = upload_file(path = "from_report/test_from.html", type = "text/html"), httr::add_headers(title = "テストレポート"), httr::add_headers(tags = paste(test_tags, collapse = ",")), encode = "raw")
