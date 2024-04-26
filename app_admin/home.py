import sys
import os
import yaml
import streamlit as st
import streamlit_authenticator as st_auth
from st_pages import Page, Section, show_pages, hide_pages, add_page_title

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from initialize import app_cfg, init_session, render_require_login, render_authenticated

# st.set_page_config(
#     page_title="Streamlit Admin App",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

authenticator = st_auth.Authenticate(
    app_cfg['credentials'],
    app_cfg['cookie']['name'],
    app_cfg['cookie']['key'],
    app_cfg['cookie']['expiry_days'],
    app_cfg['preauthorized']
)


if 'authentication_status' not in st.session_state:
    init_session()


print('st sess_stat: {} / {} / {}'.format(
    st.session_state.authentication_status, st.session_state.name, st.session_state.username))


if st.session_state.authentication_status is not True:
    st.markdown('')
    st.markdown(f"&nbsp; **Streamlit APP Admin** {'&nbsp;' * 8} "
                f"@alpha &nbsp; @beta &nbsp; @gamma &nbsp; @theta")
    name, authentication_status, username = authenticator.login()


if st.session_state.get('authentication_status'):
    authenticator.logout('Logout', 'main', key='uqkey_logout')

print('[M] st sess_stat: {} / {} / {}'.format(
    st.session_state.authentication_status, st.session_state.name, st.session_state.username))

if st.session_state.authentication_status:
    render_authenticated(user=st.session_state.username)

    st.markdown('')
    st.divider()
    st.markdown(f"#### Streamlit APP admin")
    st.markdown('')
    st.markdown('')
    st.markdown('''
    **Member**
    * Alpha
    * Beta
    * Gamma
    * Theta
    ''')
    st.markdown('')

elif st.session_state.authentication_status is False:
    render_require_login()
    st.error('Username/password is incorrect')
elif st.session_state.authentication_status is None:
    render_require_login()
    st.warning('Please enter your username and password')

print('[L] st sess_stat: {} / {} / {}'.format(
    st.session_state.authentication_status, st.session_state.name, st.session_state.username))