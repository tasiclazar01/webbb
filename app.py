from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title=Ђорђе Ташић", page_icon=":tada:", layout="wide")

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


st.subheader("Zdravo, ja sam Djordje :wave:")
st.title("Junior električar iz Srbije")
st.write("Elektrika je moja strast. Elektronika je moja strast. Uzivam u radu sa malim i velikim strujama.")
st.write("Moj instagram > https://www.instagram.com/djordjetasic/")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Šta ja radim?")
        st.write("##")
        st.write(
            """
            Iako sam junior električar bavim se sa više različitih stvari:
            - instalacija strujne mreže u kući
            - popravka svih vrsta bele tehnike
            - popravka televizora, računara, laptopova
            - popravka elektronskih komponenti na matičnim pločama
            - instalacija led traka po želji
            """
        )
        st.write("Ja sam vaše svetlo na kraju tunela :flashlight:")
    with right_column:
        st_lottie(lottie_coding, height=300, key = "coding")

with st.container():
    st.write("---")
    st.header("Moj najveći projekat u inostranstvu")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Instalacija kod Putina")
        st.write(
            """
            Nema Rusija elektricara kao sto ga ima Srbija.
            Pozvan sam od strane KGB da sprovedem celu unutrašnju instalaciju.
            Šta da kažem, ja sam čovek od poverenja :)
            """
        )

with st.container():
    st.write("---")
    st.header("Moji najveći projekat u Srbiji")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation2)

    with text_column:
        st.subheader("Instalacija kod Destana")
        st.write(
            """
            Destan radi u Nemačku i ne zna kolko pare ima. Celo selo se čudi odokle mu.
            Kuća mu liči na svemirski brod, svi joj se dive. 
            To sam ja s mojih deset prstiju sve odradio.
            """
        )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Pesma za sve kolege električare")
        st.write("##")
        audio_file = "muzika/audio.mp3"

        st.audio(audio_file)
    with right_column:
        st_lottie(lottie_codingg, height=300, key="codingg")


with st.container():
    st.write("---")
    st.header("Kontaktirajte me i zakažite popravku!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/lazartasic05@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Vaše ime" required>
     <input type="email" name="email" placeholder="Vaš imejl" required>
     <textarea name="message" placeholder="Ovde ostavite vašu poruku" required></textarea> 
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_codinggg, height=300, key="codinggg")



