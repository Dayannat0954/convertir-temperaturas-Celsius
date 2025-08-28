import streamlit as st

st.set_page_config(page_title="Conversor °C ↔ °F", page_icon="🌡️")

st.title("🌡️ Conversor de temperatura")

# Funciones
def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Selector de modo
mode = st.radio("Elige conversión:", ("Celsius → Fahrenheit", "Fahrenheit → Celsius"))

# Entrada de usuario
if mode == "Celsius → Fahrenheit":
    c = st.number_input("Temperatura en °C", value=25.0)
    st.write(f"🌡️ {c:.2f} °C = {c_to_f(c):.2f} °F")
else:
    f = st.number_input("Temperatura en °F", value=77.0)
    st.write(f"🌡️ {f:.2f} °F = {f_to_c(f):.2f} °C")
