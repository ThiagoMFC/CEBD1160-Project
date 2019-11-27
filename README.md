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

<img width="433" alt="model_performance" src="https://user-images.githubusercontent.com/24575360/69679286-c6c15b00-1075-11ea-9f31-5a4811a634d7.png">

As shown above, the model had and R2 score of 0.89 and a Mean Absolute Error of around A$132k
