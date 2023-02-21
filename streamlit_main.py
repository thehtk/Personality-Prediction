import numpy as np
import pandas as pd

import warnings
import pickle
import altair as alt
warnings.filterwarnings("ignore")



import streamlit as st
import time
from PIL import Image




def main():
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h1 style="color:white;text-align:center;">Personality Prediction </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    html_temp1 = """
    <h4 style="color:black;">Enter personal details </h4>
    
    """
    st.markdown(html_temp1, unsafe_allow_html=True)
    name = st.text_input('Name')
    gender = st.radio('Gender',['Male','Female'])
    if(gender=='Male'):
        gender_code=1
    else:
        gender_code=0
    
    age = st.number_input('Age ',15,40)
    html_temp4 = """
    <h4 style="color:black;">Instructions </h4>
    <h6 style="color:black;">i). It test is divided in 6 sections. </h6>
    <h6 style="color:black;">ii). To answer the following question select the option.</h4>
    <h6 align="left">&nbsp&nbsp 1=Strongly Disagree &nbsp;&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 2=Disagree &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 3=Netural &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 4=Agree &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 5=Strongly Agree<h6>
    <h4 align="left">Section A<h4>
    </div>
    """
    st.markdown(html_temp4, unsafe_allow_html=True)
   
    a=[0,0,0,0,0]
    a[0] = st.slider('Ques 1. I have excellent ideas', 1, 5, 3)
    a[1] = st.slider('Ques 2. I have a vivid imagination.', 1, 5, 3)
    a[2] = st.slider('Ques 3. I have a rich vocabulary', 1, 5, 3)
    a[3] = st.slider('Ques 4. Spend time reflecting on things.', 1, 5, 3)
    
    html_tempB = """
    <h4 align="left">Section B<h4>
    """
    st.markdown(html_tempB, unsafe_allow_html=True)
    b=[0,0,0,0,0]
    b[0] = st.slider('Ques 5. I am relaxed most of the time', 1, 5, 3)
    b[2] = st.slider('Ques 6. I not worry about things.', 1, 5, 3)
    b[3] = st.slider('Ques 7. I did not get stressed out easily', 1, 5, 3)
    b[4] = st.slider('Ques 8. I not get upset easily..', 1, 5, 3)
    
    html_tempC = """
    <h4 align="left">Section C<h4>
    """
    st.markdown(html_tempC, unsafe_allow_html=True)
    c=[0,0,0,0,0]
    c[0] = st.slider('Ques 9. I am always prepared.', 1, 5, 3)
    c[1] = st.slider('Ques 10. I pay attention to details.', 1, 5, 3)
    c[3] = st.slider('Ques 11. I follow a schedule', 1, 5, 3)
    c[4] = st.slider('Ques 12. I am exacting in my work..', 1, 5, 3)
    
    html_tempD = """
    <h4 align="left">Section D<h4>
    """
    st.markdown(html_tempD, unsafe_allow_html=True)
    d=[0,0,0,0,0]
    d[0] = st.slider('Ques 13. I am interested in people.', 1, 5, 3)
    d[1] = st.slider('Ques 14. I sympathize with others feelings', 1, 5, 3)
    d[3] = st.slider('Ques 15. I did not insult people', 1, 5, 3)
    d[4] = st.slider('Ques 16. I am interested in other people problems', 1, 5, 3)
    
    html_tempE = """
    <h4 align="left">Section E<h4>
    """
    st.markdown(html_tempE, unsafe_allow_html=True)
    e=[0,0,0,0,0]
    e[0] = st.slider('Ques 17. I am the life of the party.', 1, 5, 3)
    e[1] = st.slider('Ques 18. I feel comfortable around people', 1, 5, 3)
    e[2] = st.slider('Ques 19. I start conversations', 1, 5, 3)
    e[3] = st.slider('Ques 20. I do talk a lot.', 1, 5, 3)  
    
    
    ### Other tests
    html_tempF = """
    <h4 align="left">Section F<h4>
    """
    st.markdown(html_tempF, unsafe_allow_html=True)
    pen1 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\pen1.jpg')
    pen2 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\pen2.jpg')
    pen3 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\pen3.jpg')
    pen4 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\pen4.jpg')
    st.image([pen1,pen2,pen3,pen4],width=288)
    pen_intput= st.radio('How you hold pen ',[1,2,3,4])
    
    stand1 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\stand1.jpg')
    stand2 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\stand2.jpg')
    stand3 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\stand3.jpg')
    stand4 = Image.open(r'C:\Users\Hp\OneDrive\Projects\personality\Image\stand4.jpg')
    st.image([stand1,stand2,stand3,stand4],width=150)
    stand_intput= st.radio('How you mostly stand ',[1,2,3,4])
    
    ##Calculating the sum
    ope=0
    neu=0
    con=0
    agr=0
    ext=0
    
    for i in range(0,4):
        ope= ope + a[i]
        neu= neu + b[i]
        con= con +c[i]
        agr= agr+ d[i]
        ext= ext+ e[i]
        
    ##Normalize the data
    ope=(int)((ope-4)*0.4375)+1
    neu=(int)((neu-4)*0.5)+1
    con=(int)((con-4)*0.5)+1
    agr=(int)((agr-4)*0.4375)+1
    ext=(int)((ext-4)*0.4375)+1
    X_ope = data[:,2]
    X_neu = data[:,3]
    X_con = data[:,4]
    X_agr = data[:,5]
    X_ext = data[:,6]
   
    ##Calculating the average
    avg_ope=0
    avg_neu=0
    avg_con=0
    avg_agr=0
    avg_ext=0
    
    for i in range(0,1024):
        avg_ope=avg_ope+X_ope[i]
        avg_neu=avg_neu+X_neu[i]
        avg_con=avg_con+X_con[i]
        avg_agr=avg_agr+X_agr[i]
        avg_ext=avg_ope+X_ext[i]

    avg_ope=avg_ope/1024
    avg_neu=avg_neu/1024
    avg_con=avg_con/1024
    avg_agr=avg_agr/1024
    avg_ext=avg_ext/1024

        
    
        
if __name__=='__main__':
    main()
    
