
getwd()

setwd('C:/Users/Susan/Downloads')

pf <- read.csv('pseudo_facebook.tsv', sep = '\t')

library(ggplot2)
ggplot(aes(x = gender, y = age), data = pf) + geom_boxplot()


