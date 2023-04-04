import streamlit as st

import neattext.functions as nfx
from neattext.functions import clean_text
import neattext as nt
from neattext import TextCleaner
import base64
import pandas as pd

import seaborn
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud

def plot_wordclound(raw_text):
    my_wordcloud = WordCloud(width = 2000, height = 1000, random_state=1, background_color='black', 
                      colormap='viridis', collocations=False).generate(raw_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud, interpolation = "bilinear")
    plt.axis("off")
    st.pyplot(fig)

st.title("Text Cleaning app")

menu = ['Text Cleaning','About']
choice = st.sidebar.selectbox('Menu', menu)
def filedownload(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()  # strings <-> bytes conversions
    st.markdown('Download file:')
    href = f'<a href="data:file/txt;base64,{b64}" download="text.txt">Download Here</a>'
    st.markdown(href, unsafe_allow_html=True)


if choice == 'Text Cleaning':
    st.subheader('Text Cleaning')
    text_file = st.file_uploader('Upload Txt File', type=['txt'] )
    normalize_case = st.sidebar.checkbox('Normalize Case')
    clean_stopwords = st.sidebar.checkbox('Stopwords Cleaning')
    clean_punctuations = st.sidebar.checkbox('Punctuation Cleaning')
    clean_emails = st.sidebar.checkbox('Emails Cleaning')
    clean_special_char = st.sidebar.checkbox('Special Characters Cleaning')
    clean_number = st.sidebar.checkbox('Number Cleaning')
    clean_urls = st.sidebar.checkbox('URLs Cleaning')
    if text_file is not None:
        raw_text = text_file.read().decode('utf-8')
        file_details = {"Filename":text_file.name, "Filesize":text_file.size, "Filetype": text_file.type}
        st.write(file_details)
        col1, col2 = st.columns(2)
        with col1: 
            with st.expander('Original text'):
                
                st.write(raw_text)
        
        with col2:
            with st.expander('Processed text'):
                if normalize_case:
                    raw_text = raw_text.lower()
                if clean_stopwords:
                    raw_text = nfx.remove_stopwords(raw_text)
                if clean_number:
                    raw_text = nfx.remove_numbers(raw_text)
                if clean_emails:
                    raw_text = nfx.remove_emails(raw_text)
                if clean_punctuations:
                    raw_text = nfx.remove_punctuations(raw_text)
                if clean_special_char:
                    raw_text = nfx.remove_special_characters(raw_text)
                if clean_urls:
                    raw_text = nfx.remove_urls(raw_text)
                st.write(raw_text)
                filedownload(raw_text)
        with st.expander('Plot Wordcloud'):
                plot_wordclound(raw_text)


else:
    st.subheader('About')