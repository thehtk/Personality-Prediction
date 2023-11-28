import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
import altair as alt
warnings.filterwarnings("ignore")

data = pd.read_csv('https://raw.githubusercontent.com/thehtk/Personality-Prediction/main/train_copy%20-%20Copy1.csv')
data = np.array(data)

X = data[:, :-1]
y = data[:, -1]
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)


import streamlit as st
import pickle
import numpy as np
import time
from PIL import Image
import sklearn.preprocessing as pre


def predict_forest(gender_code,age,ope,neu,con, agr,ext):
    input=np.array([[gender_code,age,ope,neu,con, agr,ext]]).astype(np.float64)
    prediction=log_reg.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return prediction

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
    pen1 = Image.open(r'pen1.jpg')
    pen2 = Image.open(r'pen2.jpg')
    pen3 = Image.open(r'pen3.jpg')
    pen4 = Image.open(r'pen4.jpg')
    st.image([pen1,pen2,pen3,pen4],width=288)
    pen_intput= st.radio('How you hold pen ',[1,2,3,4])
    
    stand1 = Image.open(r'stand1.jpg')
    stand2 = Image.open(r'stand2.jpg')
    stand3 = Image.open(r'stand3.jpg')
    stand4 = Image.open(r'stand4.jpg')
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

        
    if st.button("Predict"):
        output=predict_forest(gender_code,age,ope,neu,con, agr,ext)
        
        
        st.success('Your personality types is {}'.format(output))
        if(pen_intput==1):
            st.write("When you take up something, you like to analyze it and make your conclusions so that everything is as per your liking. Overall, you have a unique personality. You can be analytical and emotional as per the situation.")
        
        if(stand_intput==1):
            st.write("You are a defensive person. You trying to comfort yourself, especially in a room full of a crowd.")
        if(stand_intput==2):
            st.write("You are feeling vulnerable and nervous but have to seem not to be confident in public.")
        if(stand_intput==3):
            st.write("You are not concerned with what someone else has to say or do. It show you are self-confidence and pride in one own’s identity.")
        if(stand_intput==4):
            st.write("You are feeling small and lacking confidence. You are displaying submissiveness and lack of power.")
        
        
        "Your scores" 
        source = pd.DataFrame({'Values': [ope,neu,con,agr,ext],'Parameters': ['Openness','Neuroticism','Conscientiousness','Agreeableness','Extraversion']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
        "Openness graph" 
        source = pd.DataFrame({'Values': [ope,avg_ope,1,8],'Parameters': ['Your','average','Minium','maxium']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
        "Neuroticism graph" 
        source = pd.DataFrame({'Values': [ope,avg_neu,1,9],'Parameters': ['Your','average','Minium','maxium']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
        "Conscientiousness graph" 
        source = pd.DataFrame({'Values': [ope,avg_con,1,9],'Parameters': ['Your','average','Minium','maxium']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
        "Agreeableness graph" 
        source = pd.DataFrame({'Values': [ope,avg_agr,1,8],'Parameters': ['Your','average','Minium','maxium']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
        "Extraversion graph" 
        source = pd.DataFrame({'Values': [ope,avg_ext,1,8],'Parameters': ['Your','average','Minium','maxium']})
        bar_chart = alt.Chart(source).mark_bar().encode(y='Values:Q',x='Parameters:O',)
        st.altair_chart(bar_chart, use_container_width=True)
        
if __name__=='__main__':
    main()
    
