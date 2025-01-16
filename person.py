import streamlit as st
from datetime import datetime

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._created_at = datetime.now().strftime("%d/%m %H:%M")
        self._updated_at = datetime.now().strftime("%d/%m %H:%M")

    @property
    def name(self):
        return self._name
    
    def set_name(self, new_name: str):
        self._name = new_name
        self._updated_at = datetime.now().strftime("%d/%m %H:%M")

    @property
    def age(self):
        return self._age
    
    def set_age(self, new_age: str):
        self._age = new_age
        self._updated_at = datetime.now().strftime("%d/%m %H:%M")

    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    
    def get_data(self):
        return self.name,self.age,self.created_at,self.updated_at

    def place_card(self):
        with st.container(border=True):
            cols = st.columns(4)
            cols[0].markdown(self.name)
            cols[1].markdown(self.age)
            cols[2].markdown(self.created_at)
            cols[3].markdown(self.updated_at)

@st.dialog("Editar pessoa")
def edit_person_dialog(person: Person):
    cols = st.columns(2)
    with cols[0].container(border=True):
        st.markdown(f"Nome: {person.name}")
        st.markdown(f"Idade: {person.age}")
        st.markdown(f"Criado: {person.created_at}")
        st.markdown(f"Update: {person.updated_at}")
    with cols[1]:
        st.text_input("Novo nome", value=person.name, placeholder=person.name, key="new_name")
        st.number_input("Nova Idade", value=person.age, placeholder=person.age, key="new_age", min_value=0, max_value=120)
        if st.button("Confirmar", use_container_width=True):
            person.set_name(st.session_state['new_name'])
            person.set_age(st.session_state['new_age'])
            st.rerun()
    if st.button("Cancelar", use_container_width=True):
        st.rerun()
