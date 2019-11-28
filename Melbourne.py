import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures

os.makedirs('plots', exist_ok=True)

melbourne = pd.read_csv(filepath_or_buffer='melbourne-housing-market/Melbourne_housing_full.csv', sep=',', header=0)
melbourne_clean = melbourne.drop(['Address', 'Method', 'SellerG', 'Date', 'Postcode', 'Lattitude', 'Longtitude',
                                  'Propertycount'], axis=1)
melbourne_clean = melbourne_clean.dropna()
melbourne_clean = melbourne_clean.reset_index(drop=True)

fig, axes = plt.subplots(1, 1, figsize=(10, 10))
axes.scatter('Price', 'Regionname', data=melbourne_clean)
fig.tight_layout()
plt.savefig('plots/price_by_region.png')
plt.close()

encoded_type = pd.get_dummies(melbourne_clean['Type'])
encoded_region = pd.get_dummies(melbourne_clean['Regionname'])
encoded_suburb = pd.get_dummies(melbourne_clean['Suburb'])
encoded_council = pd.get_dummies(melbourne_clean['CouncilArea'])
melbourne_clean = pd.concat([melbourne_clean, encoded_type, encoded_region, encoded_suburb, encoded_council], axis=1)
melbourne_clean = melbourne_clean.drop(['Type', 'Regionname', 'Suburb', 'CouncilArea'], axis=1)
melbourne_clean.rename({'t': 'town house', 'u': 'unit', 'h': 'house'}, axis=1, inplace=True)

fig, ax = plt.subplots(figsize=(15, 15))
sns.heatmap(melbourne_clean.corr(), annot=True, cmap='autumn')
ax.set_xticklabels(melbourne_clean.columns, rotation=45)
ax.set_yticklabels(melbourne_clean.columns, rotation=45)
plt.savefig('plots/heatmap.png')
plt.close()

sns.scatterplot('Price', 'Rooms', data=melbourne_clean)
plt.savefig('plots/price_by_rooms.png')
plt.close()

sns.scatterplot('Price', 'Distance', data=melbourne_clean)
plt.savefig('plots/price_by_distance.png')
plt.close()

X = melbourne_clean.drop('Price', axis=1)
y = melbourne_clean['Price']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.45, random_state=101)

polynomial_features = PolynomialFeatures(degree=2)

x_poly = polynomial_features.fit_transform(X)
model = LinearRegression()
model.fit(x_poly, y)
y_predict = model.predict(x_poly)

for (real, predicted) in list(zip(y, y_predict)):
    print(f"Value: {real:.2f}, pred: {predicted:.2f}, diff: {(real - predicted):.2f}")

print(f"Mean Absolute Error error: {metrics.mean_absolute_error(y, y_predict)}")
print(f"R2 score: {metrics.r2_score(y, y_predict)}")

sns.scatterplot(y, y_predict)
plt.plot([0, 50], [0, 50], '--')
plt.xlabel('Real Value')
plt.ylabel('Predicted Value')
plt.tight_layout()
plt.savefig('plots/Real_Value_x_Predicted_Value.png')
plt.close()

residuals = y - y_predict
sns.scatterplot(y, residuals)
plt.plot([50, 0], [0, 0], '--')
plt.xlabel('Real Value')
plt.ylabel('Residual (difference)')
plt.tight_layout()
plt.savefig('plots/Real_Value_x_Residual.png')
plt.close()

sns.distplot(residuals, bins=20, kde=False)
plt.plot([0, 0], [50, 0], '--')
plt.title('Residual (difference) Distribution')
plt.tight_layout()
plt.savefig('plots/Residual_Distribution.png')
plt.close()