!pip install --upgrade tensorflow
pip install --upgrade streamlit
import streamlit as st
import tensorflow as tf
import numpy as np from PIL 
import Image,ImageOps
import cv2
import plotly.graph_objects as go from streamlit_option_menu
import option_menu from streamlit_lottie
import st_lottie
import requests
import matplotlib.pyplot as plt

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config( page_title="Hindi Character Recognition", page_icon= "🔎" )
