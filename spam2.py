import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch
import pythoncom

pythoncom.CoInitialize()


def speak(text):
    speakk = Dispatch(("SAPI.SpVoice"))
    speakk.Speak(text)

model = pickle.load(open('C:/Users/Chaitanya/Desktop/ML PBL/Project files/spam.pkl', 'rb'))
cv = pickle.load(open('C:/Users/Chaitanya/Desktop/ML PBL/Project files/vectorizer.pkl', 'rb'))


def main():
    st.title("SMS Spam Detector")
    st.subheader("Check Your Message Here!")
    msg: str = st.text_input("Enter Message:")
    if st.button("Process"):
            print(msg)
            print(type(msg))
            data = [msg]
            print(data)
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("This is Not A Spam SMS")
                speak("This is Not A Spam SMS")
            else:
                st.error("This is A Spam SMS")
                speak("This is A Spam SMS")



main()
