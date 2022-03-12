## Welcome To Arabic Dialect Classification Project

# Definition : 

This projects is for predicting the dialect from a given arabic text based on twitter dataset

# Approches : 

1 - Data Fetching : the data fetched from an API provided by AIM TECHNOLOGIES, the data was retrieved with a limitation of 1000 request per time 

2 - Data Preprocessing : The data had a lot of puntuations, emojis usernames and urls which needed to deal with some of them one by one

3 - ML - Data modeling : Here I tried different ML algorithms like Multinomial naive bayes, logistic regression and SVC, the last two had the best results but sticked with SVC 

4 - DL - Data modeling : Here I tried to implement arabert as this paper (link here) suggested but had some problems with so i tried to implement a simple LSTM 

5 - Web Deployment : And here I Deployed the two chosen models 


# To Do :

- I will try to correctly implement araBERT on this dataset and i will share the result

- Search for deploy the models on Heroku to be available for easy use
