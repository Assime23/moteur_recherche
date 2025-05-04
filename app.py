import streamlit as st
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

st.title("Moteur de recherche académique")

ix = open_dir("index")
query_str = st.text_input("Entrez votre requête")

if query_str:
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        for r in results:
            st.write("**Titre** :", r['title'])
