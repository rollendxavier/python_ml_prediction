import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
sales_data = pd.read_csv("data\sales_data.csv")
print(sales_data.shape)
print(sales_data.describe())
# X = sales_data.drop("product",axis=0)
# y = sales_data["product"]

# model = DecisionTreeClassifier()
# model.fit(X.values, y)
# predictions = model.predict([[21,'male'],[22,'female']])
# print(predictions)