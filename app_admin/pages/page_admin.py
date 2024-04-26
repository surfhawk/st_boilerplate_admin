import streamlit as st

st.title('SubPage Admin')

st.markdown('')
st.markdown('authentication_status: {}'.format(st.session_state.authentication_status))
st.markdown('name: {}'.format(st.session_state.name))
st.markdown('username: {}'.format(st.session_state.username))
