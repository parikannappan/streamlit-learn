# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 01:27:19 2024

@author: ACER
"""

import pandas as pd
import streamlit as st 
st.set_page_config(page_title="Bank data", page_icon="bank", layout="wide")
st.title("  :bank: Personal Bank data")

Bankdata = pd.read_csv('SavingsStmt140624.csv', header=22)
#print(Bankdata.columns)
#Bankdata[['Description','type','method']] = Bankdata['   Description   '].str.split(' ', expand=True)
#print(Bankdata.head(2))
stinput = st.text_input("enter keyword to search")
dfs1 = Bankdata.loc[Bankdata['   Description   '].str.contains(stinput)]
#print(dfs1['   Description   '])
st.write(dfs1)