import streamlit as st

# Set background image
background_image = '.jpg'
main_background = f'url("{background_image}")'
st.markdown(
    f"""
    <style>
    body {{
        background-image: {main_background};
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Display input image
image1 = st.file_uploader("Upload Image 1", type="jpg")
if image1 is not None:
    st.image(image1, caption="Input Image 1")

# Add machine learning model and prediction code here
# For example:
# model = load_model('your_model.h5')
# prediction = model.predict(process_image(image1))
# image2 = display_image(prediction)

# Assuming 'prediction' is a numpy array, you can convert it to a PIL image object like this:
# prediction_image = Image.fromarray(prediction)

# Now you can display the output image
if prediction_image is not None:
    st.image(prediction_image, caption="Output Image 2")


# Add machine learning model and prediction code here
# For example:
# model = load_model('your_model.h5')
# prediction = model.predict(process_image(image1))
# image2 = display_image(prediction)
