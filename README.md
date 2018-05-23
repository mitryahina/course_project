# course_project


This project is devoted to analyzing whether activity in social media, especially Twitter is 
connected with the news in traditional media.
Using the NewsApi(https://newsapi.org/) and Twitter API through tweepy(http://www.tweepy.org/) I will
get everyday data and then find correlations among it.

Modules: 

twitter_geo.py - is used to get worldwide Twitter trends.
                 Based on Tweepy function trends_place(location)
              
API_trial.py - is used to obtain worldwide news. News API's 
               function get_headlines() is used.
            
            
headline.py - store realization of Headline class and methods
              to form a headline instance from file.
              
headline.py - store realization of Headline class and methods
              to form a headline instance from file.
              
compare.py - contains main functions for linguitic analysis.

main.py -  One Module to rule them all, One Module to find them,
           One Module to bring them all and in the darkness bind them.
           
data_parsing.py - allows to work with the results, which APIs return in json 
                  format
           
Folders:

data - news and trends collected from 8 to 25 of May, 2018.

results - results of comparison news and trends for each day. 
          A headline and a trend are considered similar if similarity
          coefficient returned by the compare() function in compare.py
          is greater than 0.4 Then the headline and trend are written 
          to a file in format 'headline trend coefficient'.
          
