import shutil
import glob
import streamlit as st


def clear_all():
    shutil.rmtree("workspace", ignore_errors=True)
    shutil.rmtree("extracted_images", ignore_errors=True)

    for f in glob.glob("*.pdf"):
        try:
            f.unlink()
        except:
            pass

    st.cache_data.clear()
    st.cache_resource.clear()

