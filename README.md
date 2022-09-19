# Hack Technology / Project Attempted


## What you built? 

I built a full-stack web app that uses machine learning to predict a professor's teaching quality using only their photo.

![Example Web-App Prediction](hack-a-thing-1-22f-liam\ex_prediction_1.png)  

The web-app is built with React, Python, Flask, and MongoDB. A user inputs a professor's name and a URL to their photo. An analysis with the different observed criteria appears on the right and a list of all analyzed professors with predicted ratings is maintained on the left.  

The predictions are made using a linear regression using training data I made by combining 20 professor reviews from DartHub with four image criteria from their headshots: facial emotion, attractiveness, picture quality (blur), and colorfulness. The facial emotion and attractiveness are determined by integrating two machine learning models I found online. Blur and colorfulness are computed by analyzing pixels with algorithms I also found online.  

Unsurprisingly, the regression isn't very accurate and there's a low correlation between the criteria I accepted and a professor's teaching ability. I didn't expect a significant relationship, but I did think it'd be funny to make.  

![Example Web-App Prediction](hack-a-thing-1-22f-liam\prof_tregubov_analysis.png)  

I also made sure to do a bit of rigging where it counts.  

## Who Did What?

Solo project, so I completed everything except a basic framework from a tutorial and where otherwise cited.

## What you learned

### What worked:

I don't have experience developing full-stack web apps or integrating machine learning models. My goal for this project was to change that, which I believe I successfully achieved. I learned some React to build the frontend, built a Python backend, and learned how to interact with MongoDB using Flask. It was a lot of work but I had fun.  

I integrated two machine learning models and some algorithms for pixel analysis. I also spent a lot of time collecting data from DartHub and analyzing photos to build the regression.  

### What didn't work:

The regression isn't very accurate, of course, and the model for attractiveness is pretty awful in my opinion. I also didn't collect much training data since it was a very labor-intensive process and I didn't want to build a pipeline to scrape everything. The contextualized analysis information is also very arbitrary. That being said, I was aware of these limitations going into the project.  

## Authors

Liam Prevelige, Dartmouth '23

## Acknowledgments

* [https://dev.to/kouul/frmp-stack-5g9](https://dev.to/kouul/frmp-stack-5g9)
* [https://www.tensorflow.org/tutorials](https://www.tensorflow.org/tutorials)
* [https://www.knowledgefactory.net/2020/12/reactjs-python-mongodb-crud-application.html](https://www.knowledgefactory.net/2020/12/reactjs-python-mongodb-crud-application.html)
* Resources for styles, models, and algorithms referenced throughout the code