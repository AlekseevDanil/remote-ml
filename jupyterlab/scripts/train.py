from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)

# train
X = [[ 1,  2,  3],
     [11, 12, 13]]
y = [0, 1]

clf.fit(X, y)

# predict

p1 = clf.predict(X)
print(p1)
p2 = clf.predict([[4, 5, 6], [14, 15, 16]])
print(p2)
