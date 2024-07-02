from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from website.settings import BASE_DIR

import pandas
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import pickle

class SaveView(APIView):
    """
    Save Training Data from CSV

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return success message
        """
        url = str(BASE_DIR) + "/../data/diabetes-data.csv"

        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        dataframe = pandas.read_csv(url, names=names)
        array = dataframe.values
        X = array[:,0:8]
        Y = array[:,8]
        test_size = 0.33
        seed = 7
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

        model = LinearRegression()
        model.fit(X_train, Y_train)

        # save the model to disk
        filename = str(BASE_DIR) + "/../results/finalized_model.sav"
        pickle.dump(model, open(filename, 'wb'))
        return Response({"message": "Training data saved"})

class LoadView(APIView):
    """
    Load Training Data from CSV

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return result from loaded model
        """
        url = str(BASE_DIR) + "/../data/diabetes-data.csv"

        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        dataframe = pandas.read_csv(url, names=names)
        array = dataframe.values
        X = array[:,0:8]
        Y = array[:,8]
        test_size = 0.33
        seed = 7
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

        # load the model from disk
        filename = str(BASE_DIR) + "/../results/finalized_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.score(X_test, Y_test)
        return Response({"result": result})