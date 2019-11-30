# CEBD116-Project: Melbourne Housing Market

| Name           | Date          |
| -------------- | ------------- |
| Thiago Marques |   11/26/2019  |

## Resources

 * [Python script](https://github.com/ThiagoMFC/CEBD1160-Project/blob/master/Melbourne.py)
 * [Results](https://github.com/ThiagoMFC/CEBD1160-Project/tree/master/plots)
 * [Dockerfile](https://github.com/ThiagoMFC/CEBD1160-Project/blob/master/Dockerfile)
 * [RUNME.md](https://github.com/ThiagoMFC/CEBD1160-Project/blob/master/RUNME.md)
 
## Research Question

 given a specific area and its characteristics, and a house and its characteristics, can we predict the resale value of said house?
 
 ### Abstract
 
From the Melbourne Housing Market dataset we can have an insight of the situation of the real estate market in Melbourne, Australia. With it we can understand what makes up the value of properties and create a tool to find the best possible value to help both sellers and buyers. In this exercise we tried to create a model to predict the value of those properties based on their features as well as the region where they are located. In the current state the model displays a "hit or miss" behavior, mostly due to a lack of entries with a determined set of features. 

### Introduction

This dataset was found on [Kaggle](https://www.kaggle.com/anthonypino/melbourne-housing-market/data#) and was extracted from a popular web-platform to buy and sell real estate properties in Australia called [Domain](https://www.domain.com.au).

### Methods

The method chosen was [Polynomial Regression](https://towardsdatascience.com/polynomial-regression-bbe8b9d97491) with degree 2. this method was chosen because of the complexity of the dataset and Linear Regression alone is prone to underfitting the model in this case.

Because of the dataset particularities the best results came when using the whole dataset as training dataset.

### Results

![Real_Value_x_Residual](https://user-images.githubusercontent.com/24575360/69826419-0789b300-11e1-11ea-9ec4-7791c5493cf1.png)

As shown above, the model had a decent performance for values up to around 3 million AUD$ but above that, because of the lack of entry points, it became completely unreliable.

Overall, the model had and R2 score of 0.89 and a Mean Absolute Error of around AUD$130k

### Discussion

As said before, the model had a "hit or miss" behaviour, being near perfet in some cases
<img width="433" alt="model_performance_accurate" src="https://user-images.githubusercontent.com/24575360/69827305-c4c9da00-11e4-11ea-8bf7-bf7280135985.png"><br/>
<img width="433" alt="model_performance_accurate2" src="https://user-images.githubusercontent.com/24575360/69827307-c6939d80-11e4-11ea-888d-031dd05b5824.png"><br/>
<img width="433" alt="model_performance_accurate3" src="https://user-images.githubusercontent.com/24575360/69827310-c98e8e00-11e4-11ea-9588-8b44bd1e95d1.png"><br/>
and really far-off in others <br/>
<img width="433" alt="model_performance_innacurate" src="https://user-images.githubusercontent.com/24575360/69827614-1e7ed400-11e6-11ea-8af7-0023ba9dd86e.png"><br/>
<img width="433" alt="model_performance_inaccurate2" src="https://user-images.githubusercontent.com/24575360/69827615-20489780-11e6-11ea-905f-467a2f87790c.png"><br/>
<img width="433" alt="model_performance_inaccurate3" src="https://user-images.githubusercontent.com/24575360/69827617-2179c480-11e6-11ea-98fd-789ba4bcc6fc.png"><br/>

This is is caused by some regions that after the data cleaning ended up with no more than 20 datapoints. this also helps explain why the R2 score was so much higher when using the entire dataset as training rather than a subset of it.

One way to improve this model could be instead of dropping rows with null values, we could split the dataset into those different regions and infer the missing values to potencially have more datapoints for every region.








