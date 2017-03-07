Financial Contributions to 2016 Presidential Campaigns in Massachusetts
=======================================================================

By Susan Li

March 6, 2017

Abstract
========

This is an exploration of 2016 US presidential campaign donations in the
state of Massachusetts. For this exploration data analysis, I am
researching the 2016 presidential campaign finance data from [Federal
Election Commission](http://fec.gov/disclosurep/PDownload.do). The
dataset contains financial contribution transaction from April 18 2015
to November 24 2016.

Throughout the analysis, I will attempt to answer the following
questions:

1.  Which candidate receive the most money?
2.  Which candidate have the most supporters?
3.  Who are those donors? What do they do?
4.  How do those donors donate? Is there a pattern? If so, what is it?
5.  Does Hillary Clinton receive more money from women than from men?
6.  Is that possible to predict a donor’s contributing party giving his
    (or her) other characteristics?

Univariate Plots Section
========================

    ## [1] 295667     18

    ## 'data.frame':    295667 obs. of  18 variables:
    ##  $ cmte_id          : chr  "C00577130" "C00577130" "C00577130" "C00577130" ...
    ##  $ cand_id          : chr  "P60007168" "P60007168" "P60007168" "P60007168" ...
    ##  $ cand_nm          : chr  "Sanders, Bernard" "Sanders, Bernard" "Sanders, Bernard" "Sanders, Bernard" ...
    ##  $ contbr_nm        : chr  "LEDWELL, BENJAMIN" "LEDWELL, BENJAMIN" "LEDWELL, BENJAMIN" "LEDWELL, BENJAMIN" ...
    ##  $ contbr_city      : chr  "NEWBURYPORT" "NEWBURYPORT" "NEWBURYPORT" "NEWBURYPORT" ...
    ##  $ contbr_st        : chr  "MA" "MA" "MA" "MA" ...
    ##  $ contbr_zip       : int  19504700 19504700 19504700 19504700 10269501 2420 21392903 24621313 25542718 12016408 ...
    ##  $ contbr_employer  : chr  "ANDOVER POLICE, MA." "ANDOVER POLICE, MA." "ANDOVER POLICE, MA." "ANDOVER POLICE, MA." ...
    ##  $ contbr_occupation: chr  "POLICE OFFICER" "POLICE OFFICER" "POLICE OFFICER" "POLICE OFFICER" ...
    ##  $ contb_receipt_amt: num  40 35 50 27 100 ...
    ##  $ contb_receipt_dt : chr  "04-Mar-16" "04-Mar-16" "06-Mar-16" "06-Mar-16" ...
    ##  $ receipt_desc     : chr  "" "" "" "" ...
    ##  $ memo_cd          : chr  "" "" "" "" ...
    ##  $ memo_text        : chr  "* EARMARKED CONTRIBUTION: SEE BELOW" "* EARMARKED CONTRIBUTION: SEE BELOW" "* EARMARKED CONTRIBUTION: SEE BELOW" "* EARMARKED CONTRIBUTION: SEE BELOW" ...
    ##  $ form_tp          : chr  "SA17A" "SA17A" "SA17A" "SA17A" ...
    ##  $ file_num         : int  1077404 1077404 1077404 1077404 1077404 1146165 1091718 1091718 1091718 1077404 ...
    ##  $ tran_id          : chr  "VPF7BKWGAE6" "VPF7BKWGCP3" "VPF7BKYF9S6" "VPF7BM0K9E6" ...
    ##  $ election_tp      : chr  "P2016" "P2016" "P2016" "P2016" ...

This dataset contains 295667 contributions and 18 variables. To start, I
want to have a glance how the contribution distributed.

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-3-1.png)

I realized that there were so many outliers(extreme high and extreme low
values), it was impossible to see details. And there were negative
contributions too.

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-4-1.png)

    ## 
    ##     5    10   100    50    25 
    ## 16780 26856 34241 36978 39546

    ##     Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
    ## -84240.0     15.0     28.0    116.1    100.0  86940.0

Transforming to log10 to better understand the distribution of the
contribution. The distribution looks normal and the data illustrated
that most donors made small amount of contributions.

Interesting to see how people donate. the most frequent amount is $25,
followed by $50, then $100. And the minimum donation was -$84240 and
maximum donation was $86940.

To perform in depth analysis, I decided to omit the negative
contributions which I believe they were refund and contributions that
exceed $2700 limit, because it breaks [Federal Election Campaign
Act](http://www.fec.gov/pages/fecrecord/2015/february/contriblimits20152016.shtml)
and will be refunded. This means 5897 contributions are omitted.

    sum(ma$contb_receipt_amt >= 2700)

    ## [1] 3244

    sum(ma$contb_receipt_amt < 0)

    ## [1] 2653

I will need to add more variables such as candidate party affiliate,
donors’ gender and donors’ zipcodes.

After processing the data and I have added 5 additional variables to
help with the analysis, and removed 5897 observations because they were
either negative amount or amount exceed $2700.

The additional variables are:

-   party: candidates party affilliation.
-   contbr\_first\_nm: contributor’s first name will be used to predict
    gender.
-   gender: contributor’s gender.
-   Latitude: Donor’s latitude for map creation.
-   Longitute: Donor’s longitude for map creation.

After adding the variables, I wonder what the contribution distribution
looks like across the parties, candidates, genders and occupations.

    ## # A tibble: 3 × 5
    ##        party  sum_party number_of_candidate mean_party      n
    ##        <chr>      <dbl>               <int>      <dbl>  <int>
    ## 1   democrat 25832080.8                   5  5166416.2 243358
    ## 2     others   270771.3                   3    90257.1    981
    ## 3 republican  4605409.9                  17   270906.5  24556

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-6-1.png)

    ## [1] 268895

Until November, 2016, total number of donations made to the presidential
election near 269K, and the Democratic party took more than 243K and
almost 10 times of the number of donations made to the Republican party.

    ## 
    ##                 Bush, Jeb       Carson, Benjamin S. 
    ##                       388                      2591 
    ##  Christie, Christopher J.   Clinton, Hillary Rodham 
    ##                       133                    147534 
    ## Cruz, Rafael Edward 'Ted'            Fiorina, Carly 
    ##                      5624                       469 
    ##      Gilmore, James S III        Graham, Lindsey O. 
    ##                         1                       110 
    ##            Huckabee, Mike             Jindal, Bobby 
    ##                        91                         1 
    ##             Johnson, Gary           Kasich, John R. 
    ##                       457                       755 
    ##          Lessig, Lawrence            McMullin, Evan 
    ##                       130                        20 
    ##   O'Malley, Martin Joseph         Pataki, George E. 
    ##                       269                         3 
    ##                Paul, Rand    Perry, James R. (Rick) 
    ##                       490                         2 
    ##              Rubio, Marco          Sanders, Bernard 
    ##                      1578                     95408 
    ##      Santorum, Richard J.               Stein, Jill 
    ##                        15                       504 
    ##          Trump, Donald J.             Walker, Scott 
    ##                     12256                        49 
    ##     Webb, James Henry Jr. 
    ##                        17

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-7-1.png)

There were total 25 candidates, Hillary Clinton was the leader in the
number of contributions, followed by Bernard Sanders, then Donald Trump.

    ## # A tibble: 2 × 3
    ##   gender  sum_gen  n_gen
    ##    <chr>    <dbl>  <int>
    ## 1 female 15029545 150055
    ## 2   male 15678717 118840

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-8-1.png)

Interesting to know that there were a lot more women than men to made
donations, about 26% difference. Was it because of Hillary Clinton? We
will find out later.

Who are those donors?

    ## # A tibble: 10 × 4
    ##    contbr_occupation  sum_occu mean_occu     n
    ##                <ord>     <dbl>     <dbl> <int>
    ## 1            RETIRED 4480345.1 108.43830 41317
    ## 2       NOT EMPLOYED 1417174.5  53.55103 26464
    ## 3            TEACHER  389587.2  56.29060  6921
    ## 4           ATTORNEY 1313684.0 212.50146  6182
    ## 5          PROFESSOR  876504.6 142.56744  6148
    ## 6          PHYSICIAN  842674.2 160.11290  5263
    ## 7         CONSULTANT  805573.5 192.12342  4193
    ## 8  SOFTWARE ENGINEER  361221.3  96.48006  3744
    ## 9          HOMEMAKER  686431.1 205.39530  3342
    ## 10          ENGINEER  309927.2  99.68709  3109

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-9-1.png)

When we count the number of donors, retired people take the first place,
followed by not employed people, teacher comes to the third, homemaker
and engineer are among the least in terms of number of contributions.

    ##         Min.      1st Qu.       Median         Mean      3rd Qu. 
    ## "2014-09-25" "2016-03-12" "2016-06-01" "2016-06-01" "2016-09-18" 
    ##         Max. 
    ## "2016-12-30"

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-10-1.png)

And it is also interesting to see when people made contributions. The
date distribution appears bimodal with period peaking around March 2016
or so and again close to the election.

Univariate Analysis
===================

### What is the structure of your dataset?

There are 268895 contributions and 18 variables. The variables that
interest to me and I will be using are:

-   cand\_nm: Candidate Name
-   contbr\_zip: Contributor Zipcode
-   contbr\_nm: Contributor name (first name in particular)
-   contbr\_occupation: Contributor Occupation
-   contb\_receipt\_amt: Contribution Amount
-   contb\_receipt\_dt: Contribution date

Othere observations:

-   Most people contribute small amount of money.
-   The median contribution amount is $28.
-   The democratic party receive the most number of donations.
-   Hillary Clinton have the most supporters.
-   There were 26% more women than men to make contributions.
-   Retired people make the most number of contributions.

### What is(are) the main features of interest in your dataset?

The main features in the dataset are party, candidate and contribution
amount. I’d like to find the answers to my questions at the beginning of
this report. I’d also like to try to use combination of variables to
build a logistics regression model to predictive a donor’s contribution
party.

### What other features in the dataset do you think will help support your investigation into your feature(s) of interest?

Gender, occupation, time of the contribution, location are likely
contribute to the contribution amount and contribution party. I think
occupation probably contributes most to the average contribution amount,
and gender probably contributes most to the contribution party.

### Did you create any new variables from existing variables in the dataset?

I created 5 variables:

-   party: candidates party affilliation.
-   contbr\_first\_nm: contributor’s first name will be used to predict
    gender.
-   gender: contributor’s gender.
-   Latitude: Donor’s latitude for map creation.
-   Longitute: Donor’s longitude for map creation.

### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?

I omitted negative contributions because I believe they were refund, and
I omitted contributions that exceed $2700 because because it breaks
[Federal Election Campaign
Act](http://www.fec.gov/pages/fecrecord/2015/february/contriblimits20152016.shtml)
and will be refunded.

Bivariate Plots Section
=======================

    ## # A tibble: 3 × 5
    ##        party  sum_party number_of_candidate mean_party      n
    ##        <ord>      <dbl>               <int>      <dbl>  <int>
    ## 1   democrat 25832080.8                   5  5166416.2 243358
    ## 2     others   270771.3                   3    90257.1    981
    ## 3 republican  4605409.9                  17   270906.5  24556

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-11-1.png)![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-11-2.png)

    ## ma$cand_nm
    ##             Jindal, Bobby    Perry, James R. (Rick) 
    ##                    250.00                    750.00 
    ##      Gilmore, James S III         Pataki, George E. 
    ##                   2700.00                   3950.00 
    ##      Santorum, Richard J.            McMullin, Evan 
    ##                   7620.10                   9305.00 
    ##            Huckabee, Mike     Webb, James Henry Jr. 
    ##                  11048.00                  12100.09 
    ##             Walker, Scott                Paul, Rand 
    ##                  46345.00                  75241.48 
    ##          Lessig, Lawrence            Fiorina, Carly 
    ##                  88483.86                 111371.48 
    ##               Stein, Jill        Graham, Lindsey O. 
    ##                 112948.03                 147830.00 
    ##             Johnson, Gary  Christie, Christopher J. 
    ##                 148518.27                 161570.00 
    ##   O'Malley, Martin Joseph       Carson, Benjamin S. 
    ##                 206496.39                 269372.60 
    ##                 Bush, Jeb           Kasich, John R. 
    ##                 399839.00                 410268.30 
    ## Cruz, Rafael Edward 'Ted'              Rubio, Marco 
    ##                 447206.14                 622812.22 
    ##          Trump, Donald J.          Sanders, Bernard 
    ##                1887235.59                4603428.95 
    ##   Clinton, Hillary Rodham 
    ##               20921571.54

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-11-3.png)

    ## [1] 30708262

The total contribution amount made to the presidential candidates
grossed over 30 million US dollars in Massachusetts. We can easily see
where the money went.

Democratic party takes the majority share of donor contribution.
Democratic party got more than 25.8 mollion US dollars in total, which
is 5.6 times of what the Republican received. It is getting worse for
the Republican when comes to the average amount, as there were 17
Republican candidates and only 5 Democratic candidates.

Same with the number of contributions, Hillary Clinton received the most
contribution amount followed by Bernard Sanders then Donald Trump.

There is no surprise as Massachusetts is the home of Kennedy family, and
routinely voted for the Democratic party in federal elections. And
Hillary Clinton has decades-deep roots in Massachusetts politics.

To see contribution patterns between parties and candidates, I start
with boxplots.

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-12-1.png)

However, it is very hard to compare contributions among all parties at a
glance because there are so many outliers. I will apply log scale and
remove the ‘others’ party from now on because my analysis is focused on
the Democratic party and the Republican party.

    ## ma$party: democrat
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.04   15.00   27.00  106.10   75.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$party: republican
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.80   27.17   50.00  187.50  100.00 2700.00

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-13-1.png)

Now it is much better. Although the Republican has the higher median and
mean, the Democrat has more variations and the distribution is more
spread out. This indicates that the Democrat has more big and small
donors.

    ## ma$cand_nm: Bush, Jeb
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##       5     100     267    1031    2700    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Carson, Benjamin S.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##       1      25      50     104     100    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Christie, Christopher J.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##      20     250    1000    1215    2700    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Clinton, Hillary Rodham
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.04   19.00   36.30  141.80  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Cruz, Rafael Edward 'Ted'
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    1.00   25.00   50.00   79.52  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Fiorina, Carly
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     3.0    25.0   100.0   237.5   200.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Gilmore, James S III
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    2700    2700    2700    2700    2700    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Graham, Lindsey O.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##       5     500    1000    1344    2300    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Huckabee, Mike
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     2.0    16.0    50.0   121.4   100.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Jindal, Bobby
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     250     250     250     250     250     250 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Kasich, John R.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    10.0    50.0   200.0   543.4   500.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Lessig, Lawrence
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     5.0   100.0   250.0   680.6   500.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: O'Malley, Martin Joseph
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    10.0   100.0   500.0   767.6  1000.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Pataki, George E.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     250     625    1000    1317    1850    2700 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Paul, Rand
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     1.0    25.0    50.0   153.6   100.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Perry, James R. (Rick)
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   250.0   312.5   375.0   375.0   437.5   500.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Rubio, Marco
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    3.05   25.00   75.00  394.70  250.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Sanders, Bernard
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    1.00   15.00   27.00   48.25   50.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Santorum, Richard J.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    5.00   17.55  100.00  508.00  500.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Trump, Donald J.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.80   28.00   72.02  154.00  150.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Walker, Scott
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    75.0   250.0   500.0   945.8  1000.0  2700.0 
    ## -------------------------------------------------------- 
    ## ma$cand_nm: Webb, James Henry Jr.
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   100.0   100.1   250.0   711.8   500.0  2700.0

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-14-1.png)

Now the picture looks interesting. Christopher Christie, Lindsey Graham
and George Patake have the highest median, Jeb Bush has the greatest
interquartile range while Hillary Clinton and Bernard Sanders seem to
have the lowest median. But Hillary Clinton has the most outliers(big
pocket donors) than anyone else. Bernard Sanders has significant number
of outliers as well.

Now let’s examine within parties.

    ## Source: local data frame [22 x 5]
    ## Groups: party [2]
    ## 
    ##         party                cand_nm  sum_can  mean_can     n
    ##         <chr>                  <chr>    <dbl>     <dbl> <int>
    ## 1  republican          Jindal, Bobby   250.00  250.0000     1
    ## 2  republican Perry, James R. (Rick)   750.00  375.0000     2
    ## 3  republican   Gilmore, James S III  2700.00 2700.0000     1
    ## 4  republican      Pataki, George E.  3950.00 1316.6667     3
    ## 5  republican   Santorum, Richard J.  7620.10  508.0067    15
    ## 6  republican         Huckabee, Mike 11048.00  121.4066    91
    ## 7    democrat  Webb, James Henry Jr. 12100.09  711.7700    17
    ## 8  republican          Walker, Scott 46345.00  945.8163    49
    ## 9  republican             Paul, Rand 75241.48  153.5540   490
    ## 10   democrat       Lessig, Lawrence 88483.86  680.6451   130
    ## # ... with 12 more rows

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-15-1.png)![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-15-2.png)

Within each party, majority of the donations were received by only few
candidates. For Democratic party, Hillary Clinton and Bernard Sanders
take almost 99% of all donations to the Democratic party, and of which,
81% went to Hillary Clinton. For the Republican party, Donald Trump led
the way taking 41% of all donations to the Republican party. Donald
Trump, Marco Rubio, Ted Cruz, John Kasich, Jeb Bush all together taking
83% of all donations to the Republican party, the remaining 17% were
shared by the other 12 Republican candidates.

From the above charts, we are able to see who were the top candidates in
each party in Massachusetts. I will examine the following candidates who
received at least 9% of total donations in their party in details later.

    ## [1] "Clinton, Hillary Rodham"   "Sanders, Bernard"         
    ## [3] "Trump, Donald J."          "Rubio, Marco"             
    ## [5] "Cruz, Rafael Edward 'Ted'"

We have seen earlier that women made 26% more number of contributions
than men. Is that the same for the amount of money donated? And do women
tend to donate more to the liberals and/or to woman candidate?

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-17-1.png)

    ## ma$gender: female
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.04   15.00   27.00   99.78   72.00 2700.00 
    ## -------------------------------------------------------- 
    ## ma$gender: male
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.24   19.00   35.00  131.10  100.00 2700.00

On average, male donated $131.1 and female donated $99.78, there is a
31% difference between genders. Female contributed much less than male
when we look at median, mean and third quartile.

    ## # A tibble: 2 × 3
    ##   gender  sum_gen      n
    ##    <chr>    <dbl>  <int>
    ## 1 female 14934709 149682
    ## 2   male 15502782 118232

![](projectTemplate_files/figure-markdown_strict/gender_data-1.png)

However, when we look at the total contribution amount between genders,
they were very close.

    ## Source: local data frame [10 x 3]
    ## Groups: cand_nm [?]
    ## 
    ##                      cand_nm gender sum_gen_can
    ##                        <chr>  <chr>       <dbl>
    ## 1    Clinton, Hillary Rodham female  11598864.9
    ## 2    Clinton, Hillary Rodham   male   9322706.6
    ## 3  Cruz, Rafael Edward 'Ted' female    137480.1
    ## 4  Cruz, Rafael Edward 'Ted'   male    309726.0
    ## 5               Rubio, Marco female    178444.7
    ## 6               Rubio, Marco   male    444367.6
    ## 7           Sanders, Bernard female   1987548.9
    ## 8           Sanders, Bernard   male   2615880.1
    ## 9           Trump, Donald J. female    437974.0
    ## 10          Trump, Donald J.   male   1449261.5

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-18-1.png)

Female in Massachusetts contributed a little less than 15 million US
Dollars in total to the presidential campaign in 2016, of which, more
than 11 million Dollars went toward Hillary Clinton. This confirms that
Massachusetts women donate more to the liberals and/or to woman
candidate.

Earlier we have seen that retired people make the most number of
contributions, how about total contribution amount and average
contribution amount cross top 10 occupations?

    ## # A tibble: 10 × 4
    ##    contbr_occupation  sum_occu mean_occu     n
    ##                <ord>     <dbl>     <dbl> <int>
    ## 1            RETIRED 4480345.1 108.43830 41317
    ## 2       NOT EMPLOYED 1417174.5  53.55103 26464
    ## 3            TEACHER  389587.2  56.29060  6921
    ## 4           ATTORNEY 1313684.0 212.50146  6182
    ## 5          PROFESSOR  876504.6 142.56744  6148
    ## 6          PHYSICIAN  842674.2 160.11290  5263
    ## 7         CONSULTANT  805573.5 192.12342  4193
    ## 8  SOFTWARE ENGINEER  361221.3  96.48006  3744
    ## 9          HOMEMAKER  686431.1 205.39530  3342
    ## 10          ENGINEER  309927.2  99.68709  3109

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-19-1.png)![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-19-2.png)

Again, retired people take the first place in terms of total
contribution amount followed by not employed people, attorney comes to
the third. However, when we look at the average contribution amount,
attorney comes to the first, and homemaker takes the second place
(presumably most of homemakers are women). Unemployed people contribute
the least on average. This does make sense.

Surprisingly, software engineer in Massachusetts has been stingy giving
their above average income and long history of reliable source of
presidential donations. Perhaps [this
article](http://fortune.com/2016/08/09/clinton-trump-tech-campaign-donors/)
can answer my question.

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-20-1.png)

I want to dive deeper to investigate the contribution amount
distribution among occupations. a boxplot sounds like a good idea. But
this one is hard to see because there are so many outliers.

    ## top_occu_df$contbr_occupation: ATTORNEY
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.04   25.00   50.00  212.60  200.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: CONSULTANT
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.24   25.00   50.00  191.50  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: ENGINEER
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    1.00   25.00   40.50   98.23  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: HOMEMAKER
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     1.0    10.0    25.0   202.9   100.0  2700.0 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: NOT EMPLOYED
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.05   13.50   27.00   53.55   50.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: PHYSICIAN
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.44   25.00   50.00  159.80  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: PROFESSOR
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.45   23.00   50.00  142.20  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: RETIRED
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##     0.5    20.0    35.0   108.1   100.0  2700.0 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: SOFTWARE ENGINEER
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    1.00   15.00   35.00   93.86  100.00 2700.00 
    ## -------------------------------------------------------- 
    ## top_occu_df$contbr_occupation: TEACHER
    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.97   15.00   25.00   56.15   50.00 2700.00

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-21-1.png)

This looks much better. After I filtered out outliers (donations that
are extreme high), a boxplot confirms my above observation. The median
contribution of teacher, homemaker and unemployed are relatively low.

It is still apparent that attorney made the large contribution with the
highest average donation and the largest variability. Some of them
contributed 4 times of their respective median.

Bivariate Analysis
==================

### Talk about some of the interesting findings you observed in this part of the investigation.

-   Most of the total contribution in Massachusetts (84%) went towad the
    Democratic party.
-   There were 5 Democratic candidates and 17 Republican candidates.
    Therefore, there is even bigger difference when we compare average
    amount between parties.
-   Within each party, the majority of contributions are received by a
    few candidates.
-   In Massachusetts there are more female donors than male donors, but
    female donate much less than male on average.
-   In Massachusetts, majority of the contributions from female donors
    went toward Democratic party and/or woman candidate.
-   Retired people contribute the most in total amount, and software
    engineers and engineers are among the least in total contribution
    amount.
-   Lawyers had the highest average contribution amount and greatest
    interquartile range, unemployed people have the lowest average
    contribution amount and one of the smallest interquartile ranges.

### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?

Surprisingly, homemakers had the 2nd highest average contribution
amount, but the median contribution in this group is among the lowest.
It suggests that the distribution of the data is right skewed with many
outliers. Also my presumption is that most of the homemakers are women.

### What was the strongest relationship you found?

Men had higher donation amount than women.

Multivariate Plots Section
==========================

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-22-1.png)![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-22-2.png)

We know that Hillary Clinton raised the most money and had the most
supporters in Massachusetts. But is this always true throughout the
campaign process? When I look at above 2 graphs, I notice 2 things:

1.  Bernard Sanders actually raised more money than Hillary Clinton
    started from January 2016 lasted for a few months.
2.  Bernard Sanders actually had more supporters than Hillary Clinton
    from January 2016 onward until June 2016 when he announced to
    endorse Hillary Clinton that [broke his supporters’
    hearts](https://www.nytimes.com/2016/07/13/us/politics/bernie-sanders-reaction.html?_r=0).

This only reinforces my doubt that what if Bernard Sanders would have
run against Donald Trump? Even Donald Trump himself famously stated the
following: [I would rather run against Crooked Hillary Clinton than
Bernie Sanders and that will happen because the books are cooked against
Bernie](http://all-that-is-interesting.com/bernie-sanders-electoral-map)!

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-23-1.png)

Interesting to see every top candidates’ time series trend. Ted Cruz had
a slow and steady growth in contribution amount, that ended as soon as
he suspended his campaign in May 2016. Marco Rubio dopped out even
earlier in March 2016. Donald Trump’s contribution donation had a steady
growth until around September 2016. His campaign probably did not spend
a lot of money in Massachusetts.

As a side note, although Donald Trump did not win in Massachusetts, [A
Third of Massachusetts Voters Picked
Trump](http://www.bostonmagazine.com/news/blog/2016/11/10/massachusetts-trump-voters/)
and [The Trump effect happened in Massachusetts,
too](https://www.bostonglobe.com/metro/2016/11/13/the-trump-effect-happened-massachusetts-too/fOGkVgbSQ2LHpuixIHxi0H/story.html).

Where do those donors reside?

![](projectTemplate_files/figure-markdown_strict/data_map-1.png)

It looks like more republicans concentrated around Boston area, this
does make sense as Boston is the largest city in Massachusetts. But
look, how blue the state is!

Predictive Modeling
===================

In this section, I will attempt to apply logistic regression method to
predict a donor’s contributing party giving his (or her) location
(latitude, longitude), gender and donation amount. I will be taking the
following steps:

1.  Subset the original dataset selecting the relevant columns only and
    make sure to filter out the ‘other’ party.
2.  Clean and format data.
3.  Remove negative sign in longitude for calculations.
4.  Create a model to predict a donor’s contributing party based on
    gender, latitude, longitude and contribution receipt amount.

<!-- -->

    ## 
    ## Call:
    ## glm(formula = party ~ ., family = binomial(link = "logit"), data = train)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -1.1990  -0.5264  -0.3468  -0.3227   2.6417  
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)        3.520e+01  1.206e+00  29.196  < 2e-16 ***
    ## contb_receipt_amt  3.798e-04  1.544e-05  24.591  < 2e-16 ***
    ## gendermale         1.000e+00  1.475e-02  67.788  < 2e-16 ***
    ## latitude          -7.499e-01  2.751e-02 -27.253  < 2e-16 ***
    ## longitude         -8.896e-02  1.233e-02  -7.217 5.31e-13 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 150246  on 239877  degrees of freedom
    ## Residual deviance: 143860  on 239873  degrees of freedom
    ##   (122 observations deleted due to missingness)
    ## AIC: 143870
    ## 
    ## Number of Fisher Scoring iterations: 5

### Interpreting the Results of the Logistic Regression Model

-   For a one unit increase in latitude, the log odds of contributing to
    Republican decreases by 0.75.
-   For a one unit increase in abs(longitude), the log odds of
    contributing to Republican decreases by 0.09.
-   For a one unit increase in contribution amount, the log odds of
    contributing to Republican increase by 0.0004.
-   If all other variables being equal, the male donor is more likely to
    contribute to Republican.

### Assessing the predictive Ability of the Model

    ##                     
    ## model_pred_direction democrat republican
    ##           democrat      26150       1761
    ##           republican        0          3

    ## [1] "Accuracy 0.936913376800172"

Wow! The 0.94 accuracy on the test set is a very good result. However,
this result is based on the mannul split of the data I created earlier.
It may not be precise enough.

Multivariate Analysis
=====================

### Talk about some of the relationships you observed in this part of the investigation.

-   While closer to the election, more big pocket donors supported
    Hillary Clinton.
-   While closer to the election, less donation went toward Donald
    Trump.

### Were there any interesting or surprising findings?

For a certain period of time, Bernard Sanders received more donations
and gained more popularity than Hillary Clinton.

Final Plots and Summary
-----------------------

### Most Donations went toward a few candidates.

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-24-1.png)

In Massachusetts, the financial donations to the presidential campaign
were distributed unevenly. Especially in Democrat, 99% of the donations
for Democrat went to two candidates and Hillary Clinton took 81%. It is
obvious that Massachusetts is among the bluest of states and Clinton has
decades-deep roots in Massachusetts politics.

Contribution by Occupation
--------------------------

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-25-1.png)

The total contribution across occupations differ substantially. If I was
asked which occupation contributed the most to presidential candidates
in Massachusetts in 2016, I would have guessed ‘lawyers’ or ‘CEOs’.
Wrong.

The top occupation isn’t really an ‘occupation’, but individuals who
lists their occupation as ‘retired’ in federal documents. Unlike lawyers
or consultants whose donations may covered by their companies, retired
people more likely pay from their own pockets.

It is continue surprising me that software engineer among the lowest in
total contribution, considering their presumably above average salary.
But any further conclusion requires better knowledge of industry
political background.

### Time Series of Top Candidates

![](projectTemplate_files/figure-markdown_strict/unnamed-chunk-26-1.png)

Hillary Clinton dominated the contribution amount and number of
contributions, the closer to the election, the more supporters with more
money came to her.

On the other hand, Bernard Sanders had a steady growth in terms of
donation amount and number of donors, until he gave up his run.

Reflection
----------

### Challenges and Struggles

The original Massachusetts 2016 presidential campaign contributions data
contains over 295000 entries from April 2015 until November 2016.
Throughout the analysis, I had to deal with several issues:

-   The original dataset did not contain gender information, to analyze
    the relationship between gender and donations, I added gender column
    using R’s gender package which used to predict gender from donor’s
    first name.
-   To see a better picture of donors’ geographic location, I added
    latitude and longitude columns using zipcode package and I was able
    to create a map using ggmap after that.
-   I chose to omit negative contributions and contributions that exceed
    $2700 because of the [Contribution Limits for 2015-2015 Federal
    Elections](http://www.fec.gov/info/contriblimitschart1516.pdf).
    However, I may have omitted big dolar donors. So use the data with
    caution.
-   I created a logistic aggression model in an attempt to predict
    donors’ contributing party based on other characteristics. However,
    I am not sure it is a good way to predict an individual’s
    contribution party.
-   I am not familar with ggmap and logistics regression, and spent a
    lot of time on them.

### Success

-   The ggplot2 and dplyr packages are the most important packages for
    this project. I also learned gender and zipcode packages and found
    they are powerful.
-   I learned a lot of new things throughout this project. Thanks to
    [ggmap
    quickstart](https://www.nceas.ucsb.edu/~frazier/RSpatialGuides/ggmap/ggmapCheatsheet.pdf),
    [R-bloggers](https://www.r-bloggers.com/how-to-perform-a-logistic-regression-in-r/)
    and [Logistic Regression in R
    tutorial](https://www.youtube.com/watch?v=mteljf020EE) to make my
    project possible. It was a great experience.

### Conclusion

By analyzing Massachusetts financial donation data, I found several
interesting characteristics:

-   It is no doubt that Massachusetts is one of the bluest states.
-   Few candidates collected the most donations.
-   Female tend to donate more to liberals and/or to female candidate.
-   The retired people are the largest contribution group, and software
    engineers make very small contributions considering [Boston is among
    the best-paying cities for software
    engineers](https://www.forbes.com/pictures/feki45ehede/7-boston-ma/#590f5e3a1196).
-   Bernard Sanders gained more popularity than Hillary Clinton until he
    gave up his run.

### Future Work

The analysis I conducted is for Massachusetts state only. It would be
interesting to analyze campaign finance data for some swing states such
as Ohio or Florida, as well as campaign finance data nationwide. I am
sure the picture would be very different.

Although the election is over, Americans have seen the [post-election
surge in
donations](https://www.theatlantic.com/business/archive/2016/11/donald-trump-donations/507668/).
There will be more interesting financial contribution data to analyze.
