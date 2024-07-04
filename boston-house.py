import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

st.write("""
# California House Price Prediction App

This app predicts the **California House Price**!
""")
st.write('---')

# Load the California housing dataset
housing = datasets.fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
Y = pd.DataFrame(housing.target, columns=["MedHouseVal"])

st.sidebar.header('Specify Input Parameters')

def user_input_features():
    MedInc = st.sidebar.slider('MedInc', X.MedInc.min(), X.MedInc.max(), X.MedInc.mean())
    HouseAge = st.sidebar.slider('HouseAge', X.HouseAge.min(), X.HouseAge.max(), X.HouseAge.mean())
    AveRooms = st.sidebar.slider('AveRooms', X.AveRooms.min(), X.AveRooms.max(), X.AveRooms.mean())
    AveBedrms = st.sidebar.slider('AveBedrms', X.AveBedrms.min(), X.AveBedrms.max(), X.AveBedrms.mean())
    Population = st.sidebar.slider('Population', X.Population.min(), X.Population.max(), X.Population.mean())
    AveOccup = st.sidebar.slider('AveOccup', X.AveOccup.min(), X.AveOccup.max(), X.AveOccup.mean())
    Latitude = st.sidebar.slider('Latitude', X.Latitude.min(), X.Latitude.max(), X.Latitude.mean())
    Longitude = st.sidebar.slider('Longitude', X.Longitude.min(), X.Longitude.max(), X.Longitude.mean())
    data = {'MedInc': MedInc,
            'HouseAge': HouseAge,
            'AveRooms': AveRooms,
            'AveBedrms': AveBedrms,
            'Population': Population,
            'AveOccup': AveOccup,
            'Latitude': Latitude,
            'Longitude': Longitude}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Model training
model = RandomForestRegressor()
model.fit(X, Y.values.ravel())

# Prediction
prediction = model.predict(df)

st.header('Prediction of Median House Value')
st.write(prediction)
st.write('---')

# SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.header('Feature Importance')
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches='tight')
st.write('---')

plt.title('Feature importance based on SHAP values (Bar)')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(bbox_inches='tight')
