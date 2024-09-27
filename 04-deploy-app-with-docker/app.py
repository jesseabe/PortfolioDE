import streamlit as st

def hello_world():
    return "Fazendo deploy de uma aplicação com Docker"

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()