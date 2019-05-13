from sklearn import tree

#[height, weight , shoe size]

X = [[181,80,44], [177, 70, 43], [160, 60, 38], [154, 54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159, 55,39], [171,75,42],[181,85,43]]

#gender

Y =  ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female','male', 'female', 'male']

tree = tree.DecisionTreeClassifier()
tree = tree.fit(X,Y)

predictionForTree = tree.predict([[167,63,41]])
print("DecisionTree: ", predictionForTree)



