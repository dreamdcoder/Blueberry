

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import numpy as np
import pandas as pd
import joblib
import streamlit as st



def prediction(df):
    model = joblib.load("/Blueberry/Model/model.pkl")

    y_val=model.predict(df)
    st.write(f"Estimated Blueberry for given datapoint will be {y_val}.")

