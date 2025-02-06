import streamlit as st
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta


options = ["1d", "1wk", "1mo","1m", "2m", "5m", "15m", "30m", "60m"]

data_name = st.text_input("Ara" , value="BTC-USD")

"---"

if data_name != "":

    st.title( data_name + " Grafiği")

    veri = yf.Ticker(data_name)

    enddate = date.today()
    startdate = enddate - relativedelta(months=6)

    


    
    start = st.date_input("Başlangıç tarihi" , value=startdate)

    end = st.date_input("Bitiş tarihi" ,value=enddate) 

    interval = st.pills(
    "Aralık",
    options = options ,
    selection_mode="single",
    default=options[0]    
    )     

    data = veri.history(start = start , end = end,interval = interval)

  

    data_type = st.multiselect(
        "data tipi",
        ["Open", "Close", "Volume", "High","Low"]
        
        )  


    
    st.line_chart(data,y=data_type)

