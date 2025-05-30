import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import plotly.express as px

st.title("📊Moodel Dashboard")

scope=["https://spreadsheets.google.com/feeds","https://googleapis.com/auth/drive"]

creds= ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client=gspread.authorize(creds)
sheet=client.opoen("Samplesheet").sheet1
data=sheet.get_all_records()
df=pd.DataFrame(data)

st.subheader("📈 Dashboard Overview")
st.dataframe(df)


st.sidebar.header("🔍 Filters")

if 'course_id' in df.columns:
    selected_course =st.sidebar.selectbox("Select Course",['All']+df['Course'].unique().tolist())
    if selected_course != 'All':
        df=df[df['course_id']==selected_course]

if 'last_activity' in df.colums:
    df['last_activity']=pd.to_datatime(df['last_activity'])
    date_range=st.sidebar.date_input("Select date Range",[]) 
    if len(date_range)==2:
        start_date,end_date=date_range
        df=df[(df['last_activity'] >= pd.to_datetime(start_date)) & (df['last_activity'] <= pd.to_datetime(end_date))]
        
st.subheader("📈 Key Metrics")

col1,col2,col3 =st.columns(3)

col1.metric("Total Records", len(df))
if 'completion_percent' in df.columns:
    active_count =(df['completion_percent'] > 0).sum()
    col2.metric("Active Users",active_count) 
    col3.metric("Inactive Users", len(df) - active_count)

#dashboard charts
st.subheader("📊 Charts")

if 'course_id' in df.columns:
    course_counts=df['course_id'].value_count().reset_index()
    course_counts.columns=['course_id','Count']
    fig1 =px.bar(course_counts,x='course_id',y='count',title='Records per course',color='course_id')
    st.plotly_chart(fig1,use_container_width=True)
    
if 'last_activity' in df.columns:
    daily_counts =df.groupby('last_activity').size().rest_index(name='Count')
    fig2=px.line(daily_counts,x='last_activity',y='Count',title='Daily Activity Trean')
    st.plotly_chart(fig2,use_container_width=True)
    
# completion percent chart
if 'completion_percent' in df.colunmns:
    status_count=df['completion_percent'].value_counts().rest_index()
    status_count.columns=['completion_percent','Count']
    fig3=px.pie(status_count,name='Status',values='Count',title='course completion Distribution')
    st.plotly_chart(fig3,use_container_width=True)
    