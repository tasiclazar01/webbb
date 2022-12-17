from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Ђорђе Ташић", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def load_lottieurll(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def load_lottieurlll(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.txt")


lottie_coding = load_lottieurl ("https://assets1.lottiefiles.com/packages/lf20_wg1juzlo.json")
lottie_codingg = load_lottieurll ("https://assets2.lottiefiles.com/private_files/lf30_LrduTx.json")
lottie_codinggg = load_lottieurll ("https://assets10.lottiefiles.com/packages/lf20_ipd377dh.json")
img_contract_form = Image.open("images/slika.png")
img_lottie_animation = Image.open("images/slika.png")

img_contract_form2 = Image.open("images/slika2.png")
img_lottie_animation2 = Image.open("images/slika2.png")

img_contract_form3 = Image.open("images/slika2.png")
img_lottie_animation3 = Image.open("images/slika2.png")


st.subheader("Здраво, ја сам Ђорђе :wave:")
st.title("Јуниор електричар из Житорађа")
st.write("Електрика је моја страст. Електроника је моја страст. Уживам у раду са великим и малим струјама.")
st.write("Мој инстаграм > https://www.instagram.com/djordjetasic/ :selfie:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Чиме се све бавим?")
        st.write("##")
        st.write(
            """
            Иако сам јуниор електричар пуно тога већ радим:
            - инсталација струјне мреже у кући
            - поправка свих врста беле технике
            - поправка телевизора, рачунара и лаптопова
            - поправка електронских компоненти на матичним плочама
            - инсталација лед трака по жељи
            """
        )
        st.write("ЈА САМ ВАШЕ СВЕТЛО НА КРАЈУ ТУНЕЛА :flashlight:")
    with right_column:
        st_lottie(lottie_coding, height=300, key = "coding")

with st.container():
    st.write("---")
    st.header("Неки од највећих послова до сад :arrow_down:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Хотел на Златибору")
        st.write(
            """
            Рад у овом хотелу је један од највећих
            задатака које сам имао досад. У питању
            је велики пројекат и драго ми је да сам
            имао учешће у томе. 
            """
        )

with st.container():
    st.write("---")
    st.header("Уметност са лед тракама :arrow_down:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation2)

    with text_column:
        st.subheader("Мало маште и резултат као из бајке")
        st.write(
            """
            У питању је приватна кућа на којој сам дуго радио.
            Посветио сам доста времена, али труд се на крају 
            исплатио као што се и види из приложеног.
            """
        )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("А ко пева зло не мисли! Послушајте химну наше струке :zap:")
        st.write("##")
        audio_file = "muzika/audio.mp3"

        st.audio(audio_file)
    with right_column:
        st_lottie(lottie_codingg, height=300, key="codingg")


with st.container():
    st.write("---")
    st.header("Закажите своју поправку већ сада!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/lazartasic05@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Ваше име" required>
     <input type="email" name="email" placeholder="Ваша имејл адреса" required>
     <textarea name="message" placeholder="Овде оставите Вашу поруку" required></textarea> 
     <button type="submit">Пошаљи</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_codinggg, height=300, key="codinggg")



