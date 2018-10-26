
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from sklearn.externals import joblib
app = Flask(__name__)
api = Api(app)

clf_path = 'C:/Users/wangyunyi/Desktop/code/model_api/iris_model.model'

clf = joblib.load(clf_path)

parser = reqparse.RequestParser()
parser.add_argument('query')


class PredictDefault(Resource):
    def get(self):

        args = parser.parse_args()
        user_query = args['query']
        y_hat = clf.predict_proba(user_query)

        output = {'probability': y_hat}

        return output

api.add_resource(PredictDefault, '/')


if __name__ == '__main__':
    app.run(debug=True)