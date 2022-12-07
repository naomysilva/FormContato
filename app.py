import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


menu = """
<div class="topnav">
  <a  href="#home">Home</a>
  <a href="#news">Novidades</a>
  <a class="active" href="#contact">Contato</a>
  <a href="#about">Sobre</a>
</div>
"""

st.markdown(menu, unsafe_allow_html=True)
st.header(":mailbox: Entre em contato comigo!")

contact_form = """
<form action="https://formsubmit.co/naomy.programmer@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nome" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Mensagem"></textarea>
     <button type="submit">Enviar</button>
</form>
"""




st.markdown(contact_form, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
        
        
local_css("style.css")