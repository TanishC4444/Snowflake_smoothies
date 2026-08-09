# Snowflake Smoothies

A Streamlit smoothie-order application that connects to Snowflake through Snowpark.

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`
- A Snowflake account and connection configuration

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Configuration

Keep Snowflake credentials in environment variables, a local secrets file, or your deployment platform's secret manager—never in the repository.

## Project scope

This is a learning project demonstrating a small Streamlit interface backed by Snowflake data and API-driven fruit search.
