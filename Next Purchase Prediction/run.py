import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import roc_auc_score
import random
from sklearn.cluster import KMeans

print("Reading File...")
Table = pd.read_csv(r'JOINED.csv', encoding = "ISO-8859-1")

Table_train = Table.loc[Table['eval_set'] == 'train']
Table_prior = Table.loc[Table['eval_set'] == 'prior']

Table_Rand = pd.DataFrame(np.random.randn(419313, 2))
pos = np.random.rand(len(Table_Rand)) < 0.8

Train = Table_train[pos]
Train = pd.concat([Train, Table_prior], axis = 0)
Test = Table_train[~pos]

Attributes = ["add_to_cart_order", "order_dow", "order_hour_of_day", "days_since_prior_order", "count(user_id)"]

#train predictors & target
train_x = Train[Attributes]
train_y = Train[["reordered"]]

#test predictors & target
test_y = Test[["reordered"]]
test_x = Test[Attributes]
print("############################################################################################## <TREE> #############################################################################")
tree = DecisionTreeClassifier(max_depth=8, random_state=1)
tree.fit(train_x, train_y) 
prediction = tree.predict(test_x)
print("Accuracy Score:",(accuracy_score(test_y, prediction))*100,"%")
Test_1 = Test.assign(predictions = prediction)
reorder = Test_1.loc[Test_1['predictions'] == 1] #predictions == 1
tree_order = reorder[["user_id", "order_id", "product_id", "product_name"]]
print(tree_order) 

print("############################################################################################## <LOGISTIC REGRESSION> ################################################################")
logmodel = linear_model.LogisticRegression()
logmodel.fit(train_x, train_y)
coef = logmodel.coef_
predictions = logmodel.predict_proba(test_x)
predictions_target = predictions[:,1]
auc = roc_auc_score(test_y, predictions_target)
print("Accuracy Score: ",(round(auc,2))*100, "%")
Test_2 = Test.assign(predictions = predictions_target)
reorder = Test_2.loc[Test_2['predictions'] >= .5] #high probability predictions
regression_order = reorder[["user_id", "order_id", "product_id", "product_name"]]
print(regression_order)

print("############################################################################################## <CLUSTERING> ##########################################################################")
kmeans = KMeans(n_clusters = 2) #generating cluster centers
model = kmeans.fit(train_x)
prediction = kmeans.predict(test_x)
Test_3 = Test.assign(predictions = prediction) #add predictions to test set
reorder = Test_3.loc[Test_3['predictions'] == 1] #predictions == 1
cluster_order = reorder[["user_id", "order_id", "product_id", "product_name"]]
print(cluster_order)