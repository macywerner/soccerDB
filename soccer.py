import streamlit as st
from ops import db_operations

db_ops = db_operations()

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

    return(countries)


# Print results.
#st.write(f"{row[0]}")
st.write(f"{row[countryQuery]}")
