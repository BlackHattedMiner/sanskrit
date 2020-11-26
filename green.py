import streamlit as st
import webbrowser
from PIL import Image
st.title("नमस्कारः!!")
st.header("सिक्किम कि फ़्लोरा और फ़ौना प्रदर्षनावली में आपका हार्दिक स्वागत है!!")
st.markdown("""
<style>
body {
   background-color: #FFFF99;
   color: #00000;
}
</style>
    """, unsafe_allow_html=True)

q = st.selectbox(
    'तो आप किसके बारे में जानना चाहते हैं??',
    ('तिब्बेतस्य लोमशः', 'कक्ताकी', 'पाटलं', 'कोविदारः', 'कृष्णः भल्लूकः', 'हिम्पातस्य तरक्षुः', 'अपुष्पोभ्दिदः')
)
if q == "कृष्णः भल्लूकः":
    st.error("अस्मिन् चित्रे कृष्णः भल्लूकः अस्ति ; जातिः --> उर्सुस थिबेतनुस")
    img = Image.open("bear.JPG")
    st.image(img,width=700)
if q == "तिब्बेतस्य लोमशः":
    st.error("अस्मिन् चित्रे तिब्बेतस्य लोमशः अस्ति ; जातिः --> वी.  फेरीलाटा")
    imga = Image.open("fox.JPG")
    st.image(imga,width=700)
if q == "कक्ताकी":
    st.error("अस्मिन् चित्रे कक्ताकी अस्ति ; जातिः --> नागफणि")
    imgb = Image.open("cactus.JPG")
    st.image(imgb,width=700)
if q == "पाटलं":
    st.error("अस्मिन् चित्रे एकम् पाटलं अस्ति ; जातिः --> रोसा केनिना")
    imgc = Image.open("rose.JPG")
    st.image(imgc,width=700)
if q == "कोविदारः":
    st.error("अस्मिन् चित्रे कोविदारः अस्ति ; जातिः --> और्चिदाकाइ")
    imgd = Image.open("orchid.JPG")
    st.image(imgd,width=700)
if q == "हिम्पातस्य तरक्षुः":
    st.error("अस्मिन् चित्रे हिम्पातस्य तरक्षुः अस्ति ; जातिः --> पी. उनिसिा")
    imge = Image.open("snow.JPG")
    st.image(imge,width=700)
if q == "अपुष्पोभ्दिदः":
    st.error("अस्मिन् चित्रे अपुष्पोभ्दिदः अस्ति ; जातिः --> पोल्पोदिके")
    img = Image.open("fern.JPG")
    st.image(img,width=700)
