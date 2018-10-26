
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.externals import joblib
data = load_iris()
x = data.data
y = data.target
clf = xgb.XGBClassifier()
clf.fit(x,y)
y_hat = clf.predict_proba([[1,2,3,4]])
joblib.dump(clf,'iris_model.model')

clf1 = joblib.load('iris_model.model')
y_hat = clf1.predict_proba([[1,2,3,4]])
print(y_hat)