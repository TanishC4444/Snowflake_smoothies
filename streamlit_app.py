"""Smoothie order demo with an optional Snowflake connection."""
import os
import pandas as pd
import requests
import streamlit as st


def save_order(session, ingredients, customer):
    """Bind user input rather than composing SQL text."""
    return session.sql(
        'insert into smoothies.public.orders(ingredients,name_on_order) values (?, ?)',
        params=[ingredients, customer],
    ).collect()


def main():
    st.title('Customize Your Smoothie')
    demo = os.environ.get('SMOOTHIE_DEMO', '').lower() in {'1', 'true', 'yes'}
    if demo:
        st.info('Local demo with synthetic fruit data. Orders stay in this browser session.')
        fruits = pd.DataFrame({'FRUIT_NAME': ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple', 'Blueberry'], 'SEARCH_ON': ['apple', 'banana', 'strawberry', 'mango', 'pineapple', 'blueberry']})
        session = None
    else:
        try:
            from snowflake.snowpark.functions import col
            session = st.connection('snowflake').session()
            fruits = session.table('smoothies.public.fruit_options').select(col('FRUIT_NAME'), col('SEARCH_ON')).to_pandas()
        except Exception:
            st.error('Configure the Snowflake connection, or set SMOOTHIE_DEMO=1 for a local preview.')
            st.stop()
    name = st.text_input('Name on order', max_chars=100)
    selected = st.multiselect('Choose up to 5 ingredients', fruits['FRUIT_NAME'].tolist(), max_selections=5)
    if selected:
        st.write('Your ingredients: ' + ', '.join(selected))
        if not demo:
            for fruit in selected:
                search = str(fruits.loc[fruits['FRUIT_NAME'] == fruit, 'SEARCH_ON'].iloc[0])
                try:
                    response = requests.get('https://my.smoothiefroot.com/api/fruit/' + requests.utils.quote(search, safe=''), timeout=10)
                    response.raise_for_status()
                    st.subheader(fruit + ' nutrition')
                    st.dataframe(response.json())
                except (requests.RequestException, ValueError):
                    st.warning('Nutrition information is unavailable for ' + fruit + '.')
        if st.button('Submit demo order' if demo else 'Submit order'):
            if not name.strip():
                st.warning('Enter a name for the order.')
            elif demo:
                st.session_state.setdefault('demo_orders', []).append({'name': name.strip(), 'ingredients': selected})
                st.success('Demo order saved locally.')
            else:
                try:
                    save_order(session, ' '.join(selected), name.strip())
                    st.success('Your smoothie is ordered.')
                except Exception:
                    st.error('The order could not be saved. Check your connection and try again.')


if __name__ == '__main__':
    main()
