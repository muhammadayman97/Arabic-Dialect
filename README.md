## Welcome To Arabic Dialect Classification Project

# Definition : 

This projects is for predicting the dialect from a given arabic text based on twitter dataset

# Project Steps : 

1 - Data Fetching : the data fetched from an API provided by AIM TECHNOLOGIES, the data was retrieved with a limitation of 1000 request per time 

2 - Data Preprocessing : The data had a lot of puntuations, emojis usernames and urls which needed to deal with some of them one by one

3 - ML - Data modeling : Here I tried different ML algorithms like Multinomial naive bayes, logistic regression and SVC, the last two had the best results but sticked with SVC 

4 - DL - Data modeling : Here I tried to implement arabert as this paper (link here) suggested but had some problems with so i tried to implement a simple LSTM 

5 - Web Deployment : And here I Deployed the two chosen models 


# To Do :

- I will try to correctly implement araBERT on this dataset and i will share the result

- Search for deploy the models on Heroku to be available for easy use

# Results :

- ازيك ياسطا

![My Image](https://raw.githubusercontent.com/muhammadayman97/Arabic-Dialect/main/Screenshot%20(49).png)

# References : 

- https://arxiv.org/pdf/2005.06557.pdf

- https://towardsdatascience.com/machine-learning-advancements-in-arabic-nlp-c6982b2f602b

- https://aliabdelaal.github.io/blog/intro-to-nlp-p1/#%D8%AA%D8%AD%D8%AF%D9%8A%D8%AF-%D9%86%D9%88%D8%B9-%D8%A7%D9%84%D9%86%D8%B5-text-classification

- https://stackoverflow.com/questions/66988153/removing-arabic-diacritic-using-python
