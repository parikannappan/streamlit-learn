# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:20:53 2024

@author: ACER
"""

import pandas as pd
import streamlit as st
import os
os.environ['PATH'] = r'C:\Users\ACER\anaconda3\Library\bin;' + os.environ['PATH'] 
st.set_page_config(page_title="Bank Statement Search ", page_icon="bank", layout="wide")
st.title("  :bank: :blue-background[Bank Statement Search App (Citibank/Axis)]")
fl = st.file_uploader(" :pink-background[Upload a file using 'Browse files' ]", type=(["csv"]))
st.button("Rerun")  
if fl is not None:
    @st.cache_data
    def load_data(fl):
        Bankdata = pd.read_csv(fl, header=22)
        return Bankdata
    Bankdata = load_data(fl)
    Bankdata.columns = [col.strip() for col in Bankdata.columns]
    Bankdata = Bankdata.drop('Unnamed: 5', axis=1)
    Bankdata = Bankdata[:-1]
    Bankdata['Withdrawals']= pd.to_numeric(Bankdata['Withdrawals'], errors='coerce') 
    Bankdata['Balance']= pd.to_numeric(Bankdata['Balance'], errors='coerce')
    Bankdata['Deposits']= pd.to_numeric(Bankdata['Deposits'],  errors='coerce')
    Bankdata['Date'] = Bankdata['Date'].str.strip()
    Bankdata['Date'] = pd.to_datetime(Bankdata['Date'], format="%d/%m/%Y", dayfirst=True)  
    top_5_withdrawals = Bankdata.sort_values(by='Withdrawals', ascending=False).head(5)  
    #top_5_withdrawals = top_5_withdrawals.reset_index(drop=True)
    #top_5_wthdropt  = top_5_withdrawals.drop(index=0, axis=0, inplace=False) #drop Totals row
    top_5_deposits = Bankdata.sort_values(by='Deposits', ascending=False).head(5)
    #top_5_deposits = top_5_deposits.reset_index(drop=True)
    #top_5_depdropt  = top_5_deposits.drop(index=0, axis=0, inplace=False)
    
# =============================================================================
#      def style_dataframe(abc):
#        #return dfs2.style.set_table_styles(
#         return abc.style.set_table_styles(
#        [{
#          'selector': 'th',
#          'props': [
#              ('background-color', '#4CAF50'),
#              ('color', 'green'),
#              ('font-family', 'Arial, sans-serif'),
#              ('font-size', '16px')
#          ]
#        }, 
#       {
#          'selector': 'td, th',
#          'props': [
#              ('border', '4px solid #4CAF50')
#          ]
#       }]
#       )
# =============================================================================
    
    def funcslds(description):
        templst = list(description.split(' '))
        
        return templst[7:10]
    top_5_withdrawals['Desc'] = top_5_withdrawals['Description'].apply(funcslds)
    dfw_sl = top_5_withdrawals[['Date','Withdrawals', 'Description']]
    print('dfw_sl', dfw_sl)
    top_5_deposits['Desc'] = top_5_deposits['Description'].apply(funcslds)
    dfd_sl = top_5_deposits[['Date', 'Deposits', 'Description'  ]]
    col1, col2 = st.columns(2)
    with col1: 
       with st.expander(":red-background[Top 5 Withdrawls]"):
            st.dataframe(dfw_sl) 
            #st.line_chart(top_5_wthdropt, x="Date", y="Withdrawals")
    with col2 :
       with st.expander(":green-background[Top 5 Deposits]"):
            st.write(dfd_sl) 
            #st.line_chart(top_5_depdropt, x="Date", y="Deposits")
    
    stinput = st.text_input("Enter keyword to search -")
    #
    if len(stinput) > 0:
       print('stinput-1', stinput)
       #print(np.isnan(stinput))
       dfs1 = Bankdata.loc[Bankdata['Description'].str.contains(stinput, case=False)]
       def functrunc(description):
           templst = list(description.split(' '))
           return templst[7:10]
       dfs1['Desc'] = dfs1['Description'].apply(functrunc) #adding a column for description
       
       dfs1w = dfs1['Withdrawals'].sum()
       dfs1d = dfs1['Deposits'].sum()
       sumdif = dfs1w - dfs1d
       st.write(f':money_with_wings: :red[WITHDRAWALS  -:  {dfs1w}]   :moneybag: :green[DEPOSITS   -:  {dfs1d}  ]')
       st.write(f':abacus: With - Dep = {sumdif}')
       dfs2 = dfs1[['Date','Desc', 'Withdrawals', 'Deposits','Description']]
       dfs2 = dfs2.style.highlight_max(subset=dfs2.columns[2:4])
       dfs3 = dfs2.data
       #dfs2 = dfs2.style.format({'Withdrawals': '{:.2f}', 'Deposits': '{:.2f}'})
       nooftrans = len(dfs1)
       #-------
         
       with st.expander(f' "View {nooftrans} Transactions of keyword" {stinput}'):
          
          #st.dataframe(styled_df) 
          #st.dataframe(dfs2.style.highlight_max(subset=dfs2.columns[2:4].round(2)))
           st.dataframe(dfs3)
           
    else:
        #print('stinput-2 ', stinput)
        dfs1d = 0
        dfs1w = 0
         
    
    #get data using date
    startdate = pd.to_datetime(Bankdata['Date']).min()
    enddate   = pd.to_datetime(Bankdata['Date']).max()
    startfrt  = startdate.strftime('%d/%m/%Y')
    endfrt    = enddate.strftime('%d/%m/%Y')
    st.write(f'View data choosing dates Available date range {startfrt} -- {endfrt}')
    #st.write(f' View data choosing dates -- available data range {} -- {}')
    col3, col4 = st.columns(2)
    with col3:
        date1 = pd.to_datetime(st.date_input('Start date', startdate))
    with col4:
        date2 = pd.to_datetime(st.date_input('End date', enddate))
    df_datr = Bankdata[(Bankdata['Date'] >= date1) & (Bankdata['Date'] <= date2)] 
    noofrows = len(df_datr)
    with st.container():
         with st.expander(f' "View Data with Above date range" which has {noofrows} Transactions'):
              st.dataframe(df_datr)
   
    
      #st.dataframe(Bankdata[['Date','Withdrawals', 'Deposits','Description']])
    #streamlit run c:\users\acer\streamlit-learn\bankrptup.py
  
