#!/usr/bin/env Rscript
library(RCurl)
result <- postForm(
  uri='https://redcap.nubic.northwestern.edu/redcap/api/',
  token='9A8D419989B3518D4291C3F82AEE6A7E',
  content='record',
  format='csv',
  returnFormat='csv',
  type = 'flat',
  rawOrLabel='raw',
  rawOrLabelHeaders='raw',
  exportCheckboxLabel='false',
  exportSurveyFields='false',
  exportDataAccessGroups='false'

)
print(result)

write.table(result, file = '~/Box/NU-SCRIPT/REDCap/TestExport/records_all01.csv', sep = ";",eol = '\n', dec = '.',row.names = TRUE,
            col.names = TRUE, qmethod = c("escape", "double"),
            fileEncoding = "utf-8")
