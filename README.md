# CEBD116-Project: Melbourne Housing Market

| Name           | Date          |
| -------------- | ------------- |
| Thiago Marques |   11/26/2019  |

## Resources

 *
 *
 *
 *
 
## Research Question

 given a specific area and its characteristics, and a house and its characteristics, can we predict the resale value of said house?
 
 ### Abstract
 
From the Melbourne Housing Market dataset we can have an insight of the situation of the real estate market in Melbourne, Australia. With it we can understand what makes up the value of properties and create a tool to find the best possible value to help both sellers and buyers. In this exercise we tried to create a model to predict the value of those properties based on the properties features as well as the region where they are located. In the current state the model displays a "hit or miss" behavior, mostly due to the dataset itself caused by the lack of entries with a determined set of features. 

### Introduction

This dataset was found on Kaggle (https://www.kaggle.com/anthonypino/melbourne-housing-market/data#) and was extracted from a popular web-platform to buy and sell real estate properties in Australia.

### Methods

The method chosen was PolynomialFeatures with degree 2 from sklearn. this method was chosen because of the complexity of the dataset and Linear Regression alone is prone to underfitting the model in this case.

Because of the dataset particularities the best results came when using the whole dataset as training dataset.

### Results

![Real_Value_x_Residual](https://user-images.githubusercontent.com/24575360/69826419-0789b300-11e1-11ea-9ec4-7791c5493cf1.png)

As shown above, the model had a decent performance for values up to around 3 million AUD$ but above that, because of the lack of entry points, it became completely unreliable.

<img width="433" alt="model_performance" src="https://user-images.githubusercontent.com/24575360/69679286-c6c15b00-1075-11ea-9f31-5a4811a634d7.png">

Overall, the model had and R2 score of 0.89 and a Mean Absolute Error of around AUD$132k

### Discussion

For regions where we had enough data, the model had near perfet predictions

After some cleaning, the dataset came down from around 35 thousand entries to just below 9 thousand, which is still a good number but after a deeper exploration, some regions ended up with no more than 20 datapoints. this helps explain why the R2 score was so much higher when using the entire dataset as training rather than a subset of it. It also helps explain why some predictions are so off-target.





