
from core.embedding import encode_image
import os
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"
os.environ["HF_HOME"] = "C:/hf_cache"

import streamlit as st
import zipfile
from pathlib import Path

from core.pdf_extractor import extract_figures_with_captions, create_word_file
from core.search import semantic_search
from utils.file_utils import clear_all


st.set_page_config(
    page_title="VisionPDF",
    page_icon="📄",
    layout="centered"
)

st.title("PDF Image Finder")

uploaded_zip = st.file_uploader("Upload ZIP containing PDFs", type=["zip"])

all_images = []
pdf_results = {}

if uploaded_zip:
    zip_dir = Path("workspace")
    zip_dir.mkdir(exist_ok=True)

    with zipfile.ZipFile(uploaded_zip, "r") as z:
        z.extractall(zip_dir)

    pdf_files = list(zip_dir.rglob("*.pdf"))
    st.success(f"Found {len(pdf_files)} PDFs")

    # -----------------------------
    # Extraction Phase
    # -----------------------------
    for pdf in pdf_files:
        st.subheader(f"Processing: {pdf.name}")

        out_dir, results = extract_figures_with_captions(pdf)

        if results:
            pdf_results[pdf.name] = results

            for r in results:

                # compute embedding ONCE (speed optimization)
                image_vec = encode_image(r["img_path"]).cpu().numpy()

                all_images.append({
                    "path": r["img_path"],
                    "caption": r["caption"],
                    "pdf": pdf.name,
                    "vector": image_vec
                })


    # -----------------------------
    # OPTION 1: Download ALL images per PDF
    # -----------------------------
    if pdf_results:
        st.divider()
        st.subheader("Download All Extracted Images")

        for pdf_name, results in pdf_results.items():

            word_path = Path("workspace") / f"{pdf_name}_all_figures.docx"

            create_word_file(
                results=[{
                    "path": r["img_path"],
                    "caption": r["caption"]
                } for r in results],
                output_path=word_path,
                title=f"All Figures from {pdf_name}"
            )

            with open(word_path, "rb") as f:
                st.download_button(
                    label=f"Download all images from {pdf_name}",
                    data=f,
                    file_name=word_path.name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

    # -----------------------------
    # Semantic Search Section
    # -----------------------------
    if all_images:
        st.divider()
        st.subheader("Searching")

        query = st.text_input("Search diagrams")

        if query:
            results = semantic_search(query, all_images)

            if results:
                for r in results:
                    st.image(
                        r["path"],
                        caption=f"{r['caption']} | Score: {round(r['score'],3)}",
                        use_container_width=True
                    )

                # -----------------------------
                # OPTION 2: Download Search Results
                # -----------------------------
                st.divider()

                search_word_path = Path("workspace") / "search_results.docx"

                create_word_file(
                    results=results,
                    output_path=search_word_path,
                    title=f"Search Results for '{query}'"
                )

                with open(search_word_path, "rb") as f:
                    st.download_button(
                        label="Download Search Results in Word file",
                        data=f,
                        file_name="search_results.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

            else:
                st.warning("No strong matches found.")

st.divider()

if st.button("Clear all data"):
    clear_all()
    st.success("All files and cache cleared.")

