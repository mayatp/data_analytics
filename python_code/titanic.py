from __future__ import division
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression 
from sklearn.cross_validation import KFold 
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import sys

import pandas 
import matplotlib.pyplot as plt
import numpy as np
import operator
import re




family_id_mapping = {}

titanic = pandas.read_csv("TrainPeturNEW.csv")
titanic_test = pandas.read_csv("TestPeturNEW.csv")
#titanic = pandas.read_csv("TrainP.csv")
#titanic_test = pandas.read_csv("TestP.csv")

predictors = ['Pclass', 'SexID','CalculatedAge','SibSp', 'TicketID','EmbarkedID', 'TitleID']
#predictors = ['Pclass', 'SexID','CalculatedAge','Fare','FamilySize', 'EmbarkedID', 'TitleID']

titanic["TitleID"] = titanic["TitleID"].fillna(titanic["TitleID"].median())

# Combining
#titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]
#titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]
#family_ids = titanic.apply(get_family_id, axis=1)
#family_ids[titanic["FamilySize"] < 3] = -1
#titanic["FamilyId"] = family_ids

#family_ids = titanic_test.apply(get_family_id, axis=1)
#family_ids[titanic_test["FamilySize"] < 3] = -1
#titanic_test["FamilyId"] = family_ids


# Selecting Best Selector
selector = SelectKBest(f_classif, k=7)
selector.fit(titanic[predictors], titanic["Survived"])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(predictors)), weight)
plt.xticks(range(len(predictors)), predictors, rotation="vertical")
plt.show()


# Linear Regression
alg = LinearRegression()
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)
predictions=[]

for train, test in kf:
    train_predictors = (titanic[predictors].iloc[train, :])
    train_target = titanic["Survived"].iloc[train]
    alg.fit(train_predictors, train_target)
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)

predictions = np.concatenate(predictions, axis=0)

predictions[predictions > .5] = 1
predictions[predictions < .5] = 0

accuracy = 0
for i, value in enumerate(predictions):
    if value == titanic["Survived"][i]:
        accuracy = accuracy + 1
    
accuracy = accuracy/len(predictions)
print("Linear Regression accuracy is " + str(accuracy))



# Logistic Regression checking
alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
alg.fit(titanic[predictors], titanic["Survived"])
predictions = alg.predict(titanic_test[predictors])
print("Logistic Regression accuracy is " + str(scores.mean()) )

# Random Forest
"""
highScore = 0
highestrandomNUM = 0
highestn_estimatorsRand = 0
highestmin_samples_split = 1
highestmin_samples_leaf = 1
for randomNUM in range(1,1):
    for n_estimatorsRand in range(50,52):
                for highestmin_samples_splitRand in range(1,2):
                    for highestmin_samples_leafRand in range(1,2):
                        alg = RandomForestClassifier(random_state=randomNUM, n_estimators=n_estimatorsRand, min_samples_split=highestmin_samples_splitRand, min_samples_leaf=highestmin_samples_leafRand)
                        scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
                        if(scores.mean() > highScore) : 
                            highScore = scores.mean()
                            highestrandomNUM = randomNUM
                            highestn_estimatorsRand = n_estimatorsRand
                            highestmin_samples_split= highestmin_samples_splitRand
                            highestmin_samples_leaf = highestmin_samples_leafRand
                            print("Iteration: ",randomNUM, ", ",n_estimatorsRand,",",highestmin_samples_split,",", highestmin_samples_leaf," New highscore found!: ", highScore ,"With random_state:", randomNUM, " and n_estimators: ",n_estimatorsRand, "and min_samples_split",highestmin_samples_split, " and min_samples_leaf: ", highestmin_samples_leaf )
                            # Writing the highest values to file to not lose them from the memory 
                            highest = str(randomNUM) + "Iteration: " + str(randomNUM) + ", " +str(n_estimatorsRand)+","+ str(highestmin_samples_split) +"," + str(highestmin_samples_leaf) +" New highscore found!: " + str(highScore) + "With random_state:" + str(randomNUM) + " and n_estimators: "+ str(n_estimatorsRand) + "and min_samples_split" + str(highestmin_samples_split) + " and min_samples_leaf: "+ str(highestmin_samples_leaf)
                            text_file = open("highestVals.txt", "w")
                            text_file.write("Value %s" % highest)
                            text_file.close()
                        print("Iteration: ",randomNUM, ", ",n_estimatorsRand,",",highestmin_samples_split,",", highestmin_samples_leaf ,", Random Forest accuracy is " + str(scores.mean()) )

print("The highest score were: ", highScore, "  randomNum: ", highestrandomNUM," n_estimators: ",n_estimatorsRand, " min_samples_split: ", highestmin_samples_split, " min_samples_leaf:", highestmin_samples_leaf  )
"""

#random forest algo
alg = RandomForestClassifier(random_state=1, n_estimators=58, min_samples_split=12, min_samples_leaf=3)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print("Random Forest accuracy is " + str(scores.mean()) )




# Ensemble KF
"""
algorithms = [
        [
            GradientBoostingClassifier(random_state=3, n_estimators=200, max_depth=3),
            ['Pclass', 'Sex', 'CalculatedAge','TicketID' ,'Fare' ,'FamilySize', 'Embarked', 'Title']
            ],
        [
            RandomForestClassifier(random_state=1, n_estimators =210, min_samples_split=6, min_samples_leaf=6),
            predictors
            ]
        ]
kf = KFold(titanic.shape[0], n_folds=6, random_state=1)
predictions=[]
for train, test in kf:
    train_target = titanic["Survived"].iloc[train]
    full_test_predictions=[]
    for alg, predictors in algorithms:
        alg.fit(titanic[predictors].iloc[train,:], train_target)
        test_predictions=alg.predict_proba(titanic[predictors].iloc[test,:].astype(float))[:,1]
        full_test_predictions.append(test_predictions)
    test_predictions = (full_test_predictions[0]*3+full_test_predictions[1])/4
    test_predictions[test_predictions <= .5] = 0
    test_predictions[test_predictions > .5] = 1
    predictions.append(test_predictions)
predictions = np.concatenate(predictions, axis=0)
accuracy = 0
for i, value in enumerate(predictions):
    if value == titanic["Survived"][i]:
        accuracy = accuracy + 1
accuracy = accuracy/len(predictions)
print("Ensemble accuracy is " + str(accuracy))
"""
# Ensemble
"""
full_predictions = []
for alg, predictors in algorithms:
    alg.fit(titanic[predictors], titanic["Survived"])
    predictions = alg.predict_proba(titanic_test[predictors].astype(float))[:,1]
    full_predictions.append(predictions)
predictions = (full_predictions[0]*3 + full_predictions[1])/4
predictions[predictions <= .5] = 0
predictions[predictions > .5] = 1
predictions = predictions.astype(int)
"""

#write all data to a new file
"""
writeToNewFile = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Pclass": titanic_test["Pclass"],
        "Sex": titanic_test["Sex"],
        "Age": titanic_test["Age"],
        "FamilySize": titanic_test["FamilySize"],
        "Fare": titanic_test["Fare"],
        "Embarked": titanic_test["Embarked"],
        "Title": titanic_test["Title"],
        "Survived": predictions
    })
writeToNewFile.to_csv("newData.csv", index=True)
"""


# Submission
submission = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": predictions
    })
submission.to_csv("result.csv", index=False)




##filling in missing values in age
"""newFile = pandas.read_csv("newData.csv")

# Selecting Best Selector
selector = SelectKBest(f_classif, k=5)
selector.fit(newFile[predictors], newFile["Age"])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(predictors)), weight)
plt.xticks(range(len(predictors)), predictors, rotation="vertical")
plt.show()

predictors = ['Pclass', 'Sex', 'FamilySize', 'Embarked', 'Title']
"""
"""

kf = KFold(newFile.shape[0], n_folds=3, random_state=1)
predictions=[]
for train, test in kf:
    train_target = newFile["CalculatedAge"].iloc[train]
    full_test_predictions=[]
    for alg, predictors in algorithms:
        alg.fit(newFile[predictors].iloc[train,:], train_target)
        test_predictions=alg.predict_proba(newFile[predictors].iloc[test,:].astype(float))[:,1]
        full_test_predictions.append(test_predictions)
    test_predictions = (full_test_predictions[0]*3+full_test_predictions[1])/4
    test_predictions[test_predictions <= .5] = 0
    test_predictions[test_predictions > .5] = 1
    predictions.append(test_predictions)
predictions = np.concatenate(predictions, axis=0)
accuracy = 0
for i, value in enumerate(predictions):
    if value == newFile["Age"][i]:
        accuracy = accuracy + 1
accuracy = accuracy/len(predictions)
print("Ensemble accuracy is " + str(accuracy))
"""
"""
writeToNewFileAge = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Pclass": titanic_test["Pclass"],
        "Sex": titanic_test["Sex"],
        "CalculatedAge": titanic_test["Age"],
        "FamilySize": titanic_test["FamilySize"],
        "Fare": titanic_test["Fare"],
        "Embarked": titanic_test["Embarked"],
        "Title": titanic_test["Title"],
        "FamilyId": titanic_test["FamilyId"],
        "Survived": predictions
    })
writeToNewFileAge.to_csv("newDataTest.csv", index=True)

writeToNewFileAge = pandas.DataFrame({
        "PassengerId": titanic["PassengerId"],
        "Pclass": titanic["Pclass"],
        "Sex": titanic["Sex"],
        "CalculatedAge": titanic["Age"],
        "FamilySize": titanic["FamilySize"],
        "Fare": titanic["Fare"],
        "Embarked": titanic["Embarked"],
        "Title": titanic["Title"],
        "FamilyId": titanic["FamilyId"]
        #"Survived": predictions
    })
writeToNewFileAge.to_csv("newDataTrain.csv", index=True)
"""