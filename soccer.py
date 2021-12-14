import streamlit as st
from ops import db_operations

# Initialize connection.
# Uses st.cache to only run once.
#@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})

db_ops = db_operations()


# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)

rows = db_ops.run_query("SELECT * from country;")

# Print results.
st.write(f"{row[0]}")
