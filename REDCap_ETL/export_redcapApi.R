library(redcapAPI)

rcon <- redcapConnection(url='https://redcap.nubic.northwestern.edu/redcap/api/', token='9A8D419989B3518D4291C3F82AEE6A7E')
myData <- exportRecords(rcon)
myData

write.table(myData, file = '~/Box/NU-SCRIPT/REDCap/TestExport/records_all02190426.csv', sep = ",",eol = '\n', dec = '.',row.names = TRUE,
            col.names = TRUE, qmethod = c("escape", "double"),
            fileEncoding = "utf-8")

## 2019-02-19 need to check the field delimiters