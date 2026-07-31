import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

def run():
    model = newpipe = joblib.load(open('model.joblib','rb'))
    st.set_page_config(page_title="Sentiment Analysis", page_icon="💬")

    st.title("💬 Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    predicted_sentiment = ""
    if st.button("Predict ✨"):
        with st.spinner("Analyzing sentiment... 🔍"):
            predicted_sentiment = (model.predict(pd.Series(userinput))[0])
        if predicted_sentiment == 1:
            output = 'positive 👍'
        else:
            output = 'negative 👎'
        sentiment = f'Predicted sentiment of "{userinput}" is {output}.'
        if predicted_sentiment == 1:
            st.success(sentiment, icon="✅")
        else:
            st.error(sentiment, icon="🚫")

if __name__ == "__main__":
    run()