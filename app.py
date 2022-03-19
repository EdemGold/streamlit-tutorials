#import dependancies
import numpy as np
import streamlit as st

#create dataset
dataframe = np.random.randn(10,20)

#run dataframe
st.dataframe(dataframe)