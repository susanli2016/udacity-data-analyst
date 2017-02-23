
getwd()

setwd('C:/Users/Susan/Downloads')

getwd()

library(ggplot2)
pf <- read.csv('pseudo_facebook.tsv', sep = '\t')
ggplot(aes(x = gender, y = age), data = subset(pf, !is.na(gender))) +
  geom_boxplot() + 
  stat_summary(fun.y = mean, shape = 4, geom = 'point')

ggplot(aes(x = age, y = friend_count), data = subset(pf, !is.na(gender))) +
  geom_line(aes(color = gender), stat = 'summary', fun.y = median)

library(dplyr)
age_gender_group <- group_by(pf, age, gender)
pf.fc_by_age_gender <- summarize(age_gender_group, 
                                 median_friend_count = median(friend_count), 
                                 mean_friend_count = mean(friend_count), 
                                 n = n())
ggplot(aes(x = age, y = median_friend_count), 
       data = subset(pf.fc_by_age_gender, !is.na(gender))) +
  geom_line(aes(color = gender))

library(reshape2)
pf.fc_by_age_gender.wide <- dcast(subset(pf.fc_by_age_gender, !is.na(gender)),  
                             age ~ gender, 
                             value.var = 'median_friend_count')

ggplot(aes(x = age, y = female/male), data = pf.fc_by_age_gender.wide) +
  geom_line() + 
  geom_hline(aes(yintercept = 1), linetype = 2)

pf$year_joined <- floor(2014 - pf$tenure / 365)

pf$year_joined.bucket <- cut(pf$year_joined, breaks = c(2004, 2009, 2011, 2012, 2014))

ggplot(aes(x = age, y = friend_count), data = subset(pf, !is.na(year_joined.bucket))) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = median)

ggplot(aes(x = age, y = friend_count), data = subset(pf, !is.na(year_joined.bucket))) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) +
  geom_line(linetype = 2, stat = 'summary', fun.y = mean)

right_tenure <- subset(pf, tenure != 0)
right_tenure$friending_rate <- right_tenure$friend_count/right_tenure$tenure
summary(right_tenure$friending_rate)

ggplot(aes(x = tenure, y = friendships_initiated/tenure), data = subset(pf, tenure >= 1)) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean)

ggplot(aes(x = tenure, y = friendships_initiated/tenure), data = subset(pf, tenure >= 1)) + 
  geom_smooth(aes(color = year_joined.bucket))

ggplot(aes(x = tenure, y = friendships_initiated / tenure),
       data = subset(pf, tenure >= 1)) +
  geom_line(aes(color = year_joined.bucket),
            stat = 'summary',
            fun.y = mean)

ggplot(aes(x = 7 * round(tenure / 7), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)

ggplot(aes(x = 30 * round(tenure / 30), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)

ggplot(aes(x = 90 * round(tenure / 90), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)

yo <- read.csv('yogurt.csv')
str(yo)

yo$id <- factor(yo$id)
str(yo)

ggplot(aes(x = price), data = yo) +
  geom_histogram()

summary(yo$price)
table(yo$price)
length(unique(yo$price))

yo <- transform(yo, all.purchases = strawberry + blueberry + pina.colada + plain + mixed.berry)

ggplot(aes(x = all.purchases), data = yo) + geom_histogram(binwidth = 1, color = 'black', fill = '#099DD9')

ggplot(aes(x = time, y = price), data = yo) +
  geom_jitter(alpha = 1/20, color = 'orange')

set.seed(0987)
sample.ids <- sample(levels(yo$id), 16)

ggplot(aes(x = time, y = price), data = subset(yo, id %in% sample.ids)) +
  facet_wrap(~ id) +
  geom_line() +
  geom_point(aes(size = all.purchases), pch = 1)

nci <- read.table("nci.tsv")
colnames(nci) <- c(1:64)

nci.long.samp <- melt(as.matrix(nci[1:200,]))
names(nci.long.samp) <- c("gene", "case", "value")
head(nci.long.samp)

ggplot(aes(y = gene, x = case, fill = value),
  data = nci.long.samp) +
  geom_tile() +
  scale_fill_gradientn(colours = colorRampPalette(c("blue", "red"))(100))
