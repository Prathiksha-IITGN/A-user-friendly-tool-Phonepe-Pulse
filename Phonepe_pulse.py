#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import pandas as pd


# In[4]:


path = "C:/Users/SAGARISHA/Downloads/CAP/pulse/data/aggregated/transaction/country/india/state/"
user_state_list = os.listdir(path)


# In[5]:


#Looping through the folder and collection of data 
clm = {'State': [], 'Year': [], 'Quater': [], 'Transacion_type': [], 'Transacion_count': [], 'Transacion_amount': []}
for i in user_state_list:
    p_i = path+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass


# In[6]:


Agg_Trans = pd.DataFrame(clm)


# In[8]:


# This is to direct the path to get the data as states
path = "C:/Users/SAGARISHA/Downloads/CAP/pulse/data/aggregated/user/country/india/state/"
user_state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<---------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'Brand': [],
    'Brand_count': [], 'Brand_percentage': []}
for i in user_state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["usersByDevice"]:
                    
                    brand = z['brand']

                    brand_count = z['count']
                    brand_percentage = z["percentage"]
                    clm['Brand'].append(brand)
                    clm['Brand_count'].append(brand_count)
                    clm['Brand_percentage'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass 
                

user_by_device = pd.DataFrame(clm)


# In[9]:


path = "C:/Users/SAGARISHA/Downloads/CAP/pulse/data/map/transaction/hover/country/india/state/"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<-------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverDataList"]:
                    district = z['name']
                    transaction_count = z['metric'][0]['count']
                    transaction_amount = z['metric'][0]['amount']
                    clm['District'].append(district)
                    clm['Transaction_count'].append(transaction_count)
                    clm['Transaction_amount'].append(transaction_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass   
                

map_transaction = pd.DataFrame(clm)


# In[10]:


path = "C:/Users/SAGARISHA/Downloads/CAP/pulse/data/map/user/hover/country/india/state/"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': [], 'App_opening': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['App_opening'].append(app_opening)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass       
                 

district_registering = pd.DataFrame(clm)
#district_registering.to_csv('district_registering_map.csv')
#district_registering


# In[11]:


import pymysql
import pandas as pd
import sqlalchemy
from sqlalchemy import text

def create_table_and_insert_data(table_name, csv_file_path):
    # MySQL database connection settings
    user = 'root'
    password = 'Prathi@123'
    host = 'localhost'
    port = 3306
    database = 'phonepe_database'
    
    # Create a connection to the MySQL database
    connection = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        user, password, host, port, database))
    
    # Create a table in MySQL
    if table_name == 'Agg_Transaction_Table':
        sql = text('CREATE TABLE Agg_Transaction_Table (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,PRIMARY KEY (MyIndex))')
    elif table_name == 'agg_userbydevice_table':
        sql = text('CREATE TABLE agg_userbydevice_table (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Brand VARCHAR(50),Brand_count BIGINT,Brand_percentage BIGINT,PRIMARY KEY (MyIndex))')
    elif table_name == 'district_map_transaction_table':
        sql = text('CREATE TABLE district_map_transaction_table (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,District VARCHAR(50),Transaction_count BIGINT,Transaction_amount BIGINT,PRIMARY KEY (MyIndex))')
    elif table_name == 'district_map_registering_table':
        sql = text('CREATE TABLE district_map_registering_table (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,District VARCHAR(50),Registered_user BIGINT,App_opening BIGINT,PRIMARY KEY (MyIndex))')
    elif table_name == 'longitude_latitude_state_table':
        sql = text('CREATE TABLE longitude_latitude_state_table (MyIndex INT NOT NULL AUTO_INCREMENT,Code VARCHAR(50),Latitude BIGINT, Longitude BIGINT, State VARCHAR(50),PRIMARY KEY (MyIndex))')
    elif table_name == 'districts_longitude_latitude_table':
        sql = text('CREATE TABLE districts_longitude_latitude_table(MyIndex INT NOT NULL AUTO_INCREMENT,State VARCHAR(50),District VARCHAR(50),Latitude BIGINT, Longitude BIGINT,PRIMARY KEY (MyIndex))')
    else:
        raise ValueError('Invalid table name')
    
    connection.execute(sql)
    
    # Insert data from CSV file into MySQL table
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=connection, if_exists='replace', index=False, chunksize=1000)


# In[14]:


import streamlit as st
import pandas as pd
import plotly.express as px
import sqlalchemy


# In[15]:


#pip install pymysql


# In[19]:


user = 'root'
password = 'Prathi%40123'
host = 'localhost'
port = 3306
database = 'phonepe_database'
connection = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
))


# In[69]:


df = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/Agg_Trans.csv', index_col=0)
state = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/Longitude_Latitude_State_Table.csv')
districts = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/Data_Map_Districts_Longitude_Latitude.csv')
districts_tran = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/district_map_transaction.csv', index_col=0)
app_opening = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/district_registering_map.csv', index_col=0)
user_device = pd.read_csv('C:/Users/SAGARISHA/Downloads/CAP/pulse/user_by_device.csv', index_col=0)


# In[37]:


#Data preparation for geo-visualization
state = state.sort_values(by='state')
state = state.reset_index(drop=True)
df2 = df.groupby(['State']).sum()[['Transacion_count', 'Transacion_amount']]
df2 = df2.reset_index()


# In[38]:


choropleth_data = state.copy()

for column in df2.columns:
    choropleth_data[column] = df2[column]
choropleth_data = choropleth_data.drop(labels='State', axis=1)

df.rename(columns={'State': 'state'}, inplace=True)
sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
state['state'] = pd.Series(data=sta_list)
state_final = pd.merge(df, state, how='outer', on='state')
districts_final = pd.merge(districts_tran, districts,
                           how='outer', on=['State', 'District'])


# In[80]:


#Scatter plot of registered user and app opening
st.balloons()
with st.container():
    st.title(':violet[PhonePe Pulse Data Visualization(2018-2022)📈]')
    st.image('C:/Users/SAGARISHA/Downloads/CAP/pulse/Vizualisation.jpeg')
    st.write(' ')
    st.subheader(
        ':violet[Registered user & App installed -> State and Districtwise:]')
    st.write(' ')
    scatter_year = st.selectbox('Please select the Year',
                                ('2018', '2019', '2020', '2021', '2022'))
    st.write(' ')
    scatter_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=10)
    scatter_year = int(scatter_year)
    scatter_reg_df = app_opening[(app_opening['Year'] == scatter_year) & (
        app_opening['State'] == scatter_state)]
    scatter_register = px.scatter(scatter_reg_df, x="District", y="Registered_user",  color="District",
                                  hover_name="District", hover_data=['Year', 'Quater', 'App_opening'], size_max=60)
    st.plotly_chart(scatter_register)
st.write(' ')


# In[81]:


#Tabs for various analysis:
geo_analysis, Device_analysis, payment_analysis, transac_yearwise = st.tabs(
    ["Geographical analysis", "User device analysis", "Payment Types analysis", "Transacion analysis of States"])


# In[45]:


#geo analysis
with geo_analysis:
    st.subheader(':violet[Transaction analysis->State and Districtwise:]')
    st.write(' ')
    Year = st.radio('Please select the Year',
                    ('2018', '2019', '2020', '2021', '2022'), horizontal=True)
    st.write(' ')
    Quarter = st.radio('Please select the Quarter',
                       ('1', '2', '3', '4'), horizontal=True)
    st.write(' ')
    Year = int(Year)
    Quarter = int(Quarter)
    plot_district = districts_final[(districts_final['Year'] == Year) & (
        districts_final['Quater'] == Quarter)]
    plot_state = state_final[(state_final['Year'] == Year)
                             & (state_final['Quater'] == Quarter)]
    plot_state_total = plot_state.groupby(
        ['state', 'Year', 'Quater', 'Latitude', 'Longitude']).sum()
    plot_state_total = plot_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    plot_state_total['code'] = pd.Series(data=state_code)


# In[47]:


#Geo-visualization of transaction data
fig1 = px.scatter_geo(plot_district,
                          lon=plot_district['Longitude'],
                          lat=plot_district['Latitude'],
                          color=plot_district['Transaction_amount'],
                          size=plot_district['Transaction_count'],
                          hover_name="District",
                          hover_data=["State", 'Transaction_amount', 'Transaction_amount',
                                      'Transaction_count', 'Year', 'Quater'],
                          title='District',
                          size_max=22,)
fig1.update_traces(marker={'color': "#CC0044",
                               'line_width': 1})
fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='state',
                          text=plot_state_total['code'],
                          hover_data=['Transacion_count',
                                      'Transacion_amount', 'Year', 'Quater'],
                          )
fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transacion_amount',
        color_continuous_scale='twilight',
        hover_data=['Transacion_count', 'Transacion_amount']
    )

fig.update_geos(fitbounds="locations", visible=False)
fig.add_trace(fig1.data[0])
fig.add_trace(fig2.data[0])
fig.update_layout(height=1000, width=1000)
st.write(' ')
st.write(' ')
if st.button('Click here to see map clearly'):
    fig.show(renderer="browser")
    st.plotly_chart(fig)


# In[48]:


#Device analysis statewise
with Device_analysis:
    st.subheader(':violet[User Device analysis->Statewise:]')
    tree_map_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=10, key='tree_map_state')
    tree_map_state_year = int(st.radio('Please select the Year',
                                       ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='tree_map_state_year'))
    tree_map_state_quater = int(st.radio('Please select the Quarter',
                                         ('1', '2', '3', '4'), horizontal=True, key='tree_map_state_quater'))
    user_device_treemap = user_device[(user_device['State'] == tree_map_state) & (user_device['Year'] == tree_map_state_year) &
                                      (user_device['Quater'] == tree_map_state_quater)]
    user_device_treemap['Brand_count'] = user_device_treemap['Brand_count'].astype(
        str)


# In[50]:


#Treemap view of user device
user_device_treemap_fig = px.treemap(user_device_treemap, path=['State', 'Brand'], values='Brand_percentage', hover_data=['Year', 'Quater'],
                                         color='Brand_count',
                                         title='User device distribution in ' + tree_map_state +
                                         ' in ' + str(tree_map_state_year)+' at '+str(tree_map_state_quater)+' quater',)
st.plotly_chart(user_device_treemap_fig)


# In[51]:


#Barchart view of user device
bar_user = px.bar(user_device_treemap, x='Brand', y='Brand_count', color='Brand',
                      title='Bar chart analysis', color_continuous_scale='sunset',)
st.plotly_chart(bar_user)


# In[53]:


#Payment type analysis of Transaction data
with payment_analysis:
    st.subheader(':violet[Payment type Analysis -> 2018 - 2022:]')
    # querypa = 'select * from agg_transaction_table'
    # payment_mode = pd.read_sql(querypa, con=connection)
    payment_mode = pd.read_csv('Agg_Trans.csv', index_col=0)
    pie_pay_mode_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                              'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                              'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                              'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                              'uttarakhand', 'west-bengal'), index=10, key='pie_pay_mode_state')
    pie_pay_mode_year = int(st.radio('Please select the Year',
                                     ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='pie_pay_year'))
    pie_pay_mode__quater = int(st.radio('Please select the Quarter',
                                        ('1', '2', '3', '4'), horizontal=True, key='pie_pay_quater'))
    pie_pay_mode_values = st.selectbox(
        'Please select the values to visualize', ('Transacion_count', 'Transacion_amount'))
    pie_payment_mode = payment_mode[(payment_mode['Year'] == pie_pay_mode_year) & (
        payment_mode['Quater'] == pie_pay_mode__quater) & (payment_mode['State'] == pie_pay_mode_state)]


# In[54]:


#pie chart analysis of payment mode
pie_pay_mode = px.pie(pie_payment_mode, values=pie_pay_mode_values,
                         names='Transacion_type', hole=.5, hover_data=['Year'])


# In[56]:


#Bar chart analysis of payment mode
pay_bar = px.bar(pie_payment_mode, x='Transacion_type',
                     y=pie_pay_mode_values, color='Transacion_type')
st.plotly_chart(pay_bar)
st.plotly_chart(pie_pay_mode)


# In[58]:


#Transaction data analysis statewise 
with transac_yearwise:
    st.subheader(':violet[Transaction analysis->Statewise:]')
    transac_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=10, key='transac')
    transac__quater = int(st.radio('Please select the Quarter',
                                   ('1', '2', '3', '4'), horizontal=True, key='trans_quater'))
    transac_type = st.selectbox('Please select the Mode',
                                ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'), key='transactype')
    transac_values = st.selectbox(
        'Please select the values to visualize', ('Transacion_count', 'Transacion_amount'), key='transacvalues')
    payment_mode_yearwise = pd.read_csv('Agg_Trans.csv', index_col=0)

    # querypay_year = 'select * from agg_transaction_table'
    # payment_mode_yearwise = pd.read_sql(querypay_year, con=connection)

    new_df = payment_mode_yearwise.groupby(
        ['State', 'Year', 'Quater', 'Transacion_type']).sum()
    new_df = new_df.reset_index()
    chart = new_df[(new_df['State'] == transac_state) &
                   (new_df['Transacion_type'] == transac_type) & (new_df['Quater'] == transac__quater)]


# In[59]:


year_fig = px.bar(chart, x=['Year'], y=transac_values, color=transac_values, color_continuous_scale='armyrose',
                      title='Transacion analysis '+transac_state + ' regarding to '+transac_type)
st.plotly_chart(year_fig)


# In[79]:


# -------------------------------------------- Sidebar --> for overall india Data comparisons -------------------------------------------------
with st.sidebar:
    # -------------------------- Bar chart ofoverall india transacion data  -----------------------------------------------------------------
    st.image("C:/Users/SAGARISHA/Downloads/CAP/pulse/phonepe_logo.png")
    st.subheader(':violet[Overall India Analysis:]')
    overall_values = st.selectbox(
        'Please select the values to visualize', ('Transacion_count', 'Transacion_amount'), key='values')
    overall = new_df.groupby(['Year']).sum()
    overall.reset_index(inplace=True)

    overall = px.bar(overall, x='Year', y=overall_values, color=overall_values,
                     title='Overall pattern of Transacion all over India', color_continuous_scale='sunset',)
    overall.update_layout(height=350, width=350)
    st.plotly_chart(overall)


# In[63]:


# # -------------------------------------------- Sidebar --> for overall india Data comparisons -------------------------------------------------
# with st.sidebar:
#     # -------------------------- Bar chart ofoverall india transacion data  -----------------------------------------------------------------
#     st.subheader(':violet[Overall India Analysis:]')
#     overall_values = st.selectbox(
#         'Please select the values to visualize', ('Transacion_count', 'Transacion_amount'), key='values')
#     overall = new_df.groupby(['Year']).sum()
#     overall.reset_index(inplace=True)

#     overall = px.bar(overall, x='Year', y=overall_values, color=overall_values,
#                      title='Overall pattern of Transacion all over India', color_continuous_scale='sunset',)
#     overall.update_layout(height=350, width=350)
#     st.plotly_chart(overall)


# In[75]:


# --------------------------Bar chart of overall india registered and app opening --------------------------------------------------------
    # query_reg = 'select * from district_map_registering_table'
    # overall_reg = pd.read_sql(query5, con=connection)
overall_reg = pd.read_csv('district_registering_map.csv')
overall_reg = overall_reg.groupby(['State', 'Year']).sum()
overall_reg.reset_index(inplace=True)

overall_reg = px.bar(overall_reg, x='Year', y=[
                         'Registered_user', 'App_opening'], barmode='group', title='Phonepe installation from 2018 - 2022')
overall_reg.update_layout(height=350, width=350)
st.plotly_chart(overall_reg)


# In[ ]:




