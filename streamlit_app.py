import streamlit as st
import base64

# Set the page title and icon
st.set_page_config(
    page_title="My Machine Learning App",
    page_icon="🔎"
)

# Load the background image
with open("hdbd (1).png", "rb") as file:
    bg_img = file.read()

# Set the background image
st.markdown(
  f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{base64.b64encode(bg_img).decode()}");
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-size: cover;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title and description to the app
st.title("My Machine Learning App")
st.subheader("This app uses machine learning to classify images")

# Add a file uploader to upload an image
file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image was uploaded
if file is not None:
    # Load and preprocess the image
    img = load_and_prep(file)

    # Display the uploaded image
    fig, ax = plt.subplots()
    ax.imshow(img.numpy().astype('uint8'))
    ax.axis(False)
    st.pyplot(fig)

    # Make a prediction on the image
    pred_prob = model.predict(tf.expand_dims(img, axis=0))

    # Display the top n predictions
    n = st.slider('n', min_value=1, max_value=5, value=3, step=1)
    class_name, confidense = get_n_predictions(pred_prob, n)

    if st.button("Predict"):
        st.header(f"Top {n} Prediction for given image")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=confidense[::-1],
            y=class_name[::-1],
            orientation='h'))
        fig.update_layout(height=500, width=900,
                          xaxis_title='Probability', yaxis_title=f'Top {n} Class Name')
        st.plotly_chart(fig, use_container_width=True)

        st.success(f"The image is classified as \t  \'{class_name[0]}\' \t with {confidense[0] * 100:.1f} % probability")
