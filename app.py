# import os
from io import StringIO

import streamlit as st
import pandas as pd
from prediction import prediction

# uploaded_file = st.file_uploader("Choose a file")

global stat_df
global btn
df =None


# stat_df=pd.read_csv("/Blueberry/Dataset/stat.csv")
stat_df=pd.read_csv("Dataset/stat.csv")
stat_df.set_index('Unnamed: 0',inplace=True)

def get_values(label):
    global stat_df
    min = float(stat_df.loc[label][0])
    max=float(stat_df.loc[label][1])
    return min,max

def populate_data():
     #st.write("""# My first app Hello *world!*""")
     columns = ['clonesize', 'honeybee', 'bumbles', 'andrena', 'osmia',
                'averageofuppertrange', 'averageoflowertrange', 'averagerainingdays',
                'fruitset', 'fruitmass', 'seeds']
     data=[]
     for c in columns:
         min_value, max_value = get_values(c)
         # st.write(f"min:{type(min_value)},max:{type(max_value)},{c},{type(c)}")
         x =  st.slider(c,min_value=min_value,max_value=max_value,value=None)
         data.append(x)
         st.write('Values:', x)
     df=pd.DataFrame(data).T
     df.columns=columns
     st.write(df)
     btn = st.button('Predict', disabled=False, key=11)
     if btn:
         X=(df)
         prediction(X)

if __name__ == '__main__':
     populate_data()






