# import os,sys
# from flask import Flask
# from flask_restful import reqparse, abort, Api, Resource
# import pickle
# from sklearn.externals import joblib
# app = Flask(__name__)
# api = Api(app)
# parser = reqparse.RequestParser()
# parser.add_argument('query')
#
# class HelloWorld(Resource):
#     def get(self):
#         # use parser and find the user's query
#         args = parser.parse_args()
#         user_query = args['query']
#
#
#         return user_query
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5000)



import os,sys
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from model_api.score_calculate import score_transform_series

app = Flask(__name__)
api = Api(app)
clf_path = 'C:/Users/wangyunyi/Desktop/code/model_api/iris_model.model'
clf = joblib.load(clf_path)
parser = reqparse.RequestParser()
parser.add_argument('query')

class HelloWorld(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query'].split(',')
        user_query = list(map(float,user_query))

        y_hat = clf.predict_proba(user_query).ravel()[1]

        y_hat = score_transform_series(y_hat)

        y_hat = str(round(y_hat))
        return {'Result':y_hat}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)