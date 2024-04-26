import os
import yaml

import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from st_pages import Page, Section, show_pages, hide_pages, add_page_title


def init_session():
    st.session_state.authentication_status = None
    st.session_state.name = None
    st.session_state.username = None


def load_yaml(fp):
    with open(fp, mode='r') as cfg_f:
        cfg = yaml.safe_load(cfg_f)
        print(cfg)
        return cfg


def wide_page_layout(wide: bool = False):
    ctx = get_script_run_ctx()
    ctx._set_page_config_allowed = True
    st.set_page_config(layout='wide' if wide else 'centered')
    # ctx._set_page_config_allowed = False


def render_require_login():
    init_session()
    wide_page_layout(False)
    show_pages(
        [
            Page("home.py", "Home"),
        ]
    )


def render_authenticated(user: str = '', role: str = ''):
    wide_page_layout(True)
    all_pages_d = {
        'home': Page("home.py", "Home", ),
        'page1': Page("pages/page1.py", "SubPage 1", ),
        'page2': Page("pages/page2.py", "SubPage 2", ),
    }

    if user == 'admin':
        all_pages_d['admin'] = Page("pages/page_admin.py", "Admin Page", )

    show_pages(list(all_pages_d.values()))


init_session()
app_cfg = load_yaml(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app_cfg.yaml'))
