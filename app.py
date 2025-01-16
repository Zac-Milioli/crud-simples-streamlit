import streamlit as st
from person import Person, edit_person_dialog

st.set_page_config(page_title="CRUD", page_icon=":material/group:")

if "database" not in st.session_state:
    st.session_state["database"] = []

st.title("CRUD de Pessoas")
if st.button(":material/delete: Limpar database", use_container_width=True):
    st.session_state["database"] = []
    st.toast("Database limpa", icon=":material/check:")

with st.container(border=True):
    st.text_input("Nome", key="name")
    st.number_input("Idade", key="age", min_value=0, max_value=120)
    cols = st.columns(2)
    if st.button(":material/person: Cadastrar pessoa", use_container_width=True):
        if st.session_state.get("name"):
            st.session_state["database"].append(Person(name=st.session_state["name"], age=st.session_state["age"]))
        else:
            st.toast("Cadastro inválido", icon=":material/block:")

st.header(":material/group: Database")
with st.container(border=True):
    cols = st.columns(5)
    cols[0].markdown("Nome")
    cols[1].markdown("Idade")
    cols[2].markdown("Criação")
    cols[3].markdown("Alteração")
    cols[4].markdown("Ações")
    for person in st.session_state["database"]:
        cols = st.columns([4,1])
        with cols[0]:
            person.place_card()
        with cols[1]:
            btn_cols = st.columns(2)
            if btn_cols[0].button(":material/edit:", use_container_width=True, key=f"{person} edit"):
                edit_person_dialog(person)
            if btn_cols[1].button(":material/delete:", use_container_width=True, key=f"{person} delete"):
                st.session_state["database"].remove(person)
                st.rerun()
