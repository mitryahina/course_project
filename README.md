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
                  
app.py - Flask app, which allows to show results of comparison as a words clouds.
        #toDo: ability to submit date in an app and dynamically show the results.
        The reason for not making an app fully dynamical is that to the time of
        API's response is about 3 seconds and then it takes about 15 minutes to
        analyze ~ 40 000 combinations of news and trends, so the response time of 
        the app would be undecent.
           
Folders:

data - news and trends collected from 8 to 25 of May, 2018.

results - results of comparison news and trends for each day. 
          A headline and a trend are considered similar if similarity
          coefficient returned by the compare() function in compare.py
          is greater than 0.4 Then the headline and trend are written 
          to a file in format 'headline trend coefficient'.
          
templates - HTML templates for Flask app

static/js, static/css - web-folders for app
          
  
          
