import streamlit as st
from ops import db_operations

db_ops = db_operations()

st.title("Futbol Fans Tournament Database")
st.markdown("Welcome, fan! Here you can search through European tournaments from 1872 to now.")
# Initialize connection.
# Uses st.cache to only run once.
#@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})



# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)

def countryQuery():
    queryPlay = '''
    SELECT *
    FROM country;
    '''

countries = db_ops.run_query(countryQuery)
# Print results.
#st.write(f"{row[0]}")
for row in countries:
    st.write(f"{row[0]}")
