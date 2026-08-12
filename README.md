<div align="center">
<img src="https://images.unsplash.com/photo-1751614813050-f08134933d7c?auto=format&fit=crop&w=1800&h=600&q=82" alt="Fruit selection, nutrition enrichment, smoothie customization, and cloud data storage" width="100%" />
<sub>Real photography by <a href="https://unsplash.com/photos/someone-is-holding-a-refreshing-fruity-smoothie-EMnBbQi0N_o">Esra Afşar on Unsplash</a>.</sub>

# Snowflake Smoothies
### A small Streamlit ordering experience backed by Snowpark, live nutrition data, and Snowflake tables.

![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Snowflake](https://img.shields.io/badge/Data-Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white)
![Python](https://img.shields.io/badge/Python-App-3776AB?style=flat-square&logo=python&logoColor=white)
![Snowpark](https://img.shields.io/badge/Compute-Snowpark-0EA5E9?style=flat-square)

[Experience](#experience) · [Data flow](#data-flow) · [Setup](#run-locally) · [Engineering](#engineering-notes)
</div>

---

## Overview

Snowflake Smoothies is a compact data-application project built with Streamlit. It reads available fruit ingredients from a Snowflake table through Snowpark, lets a customer select up to five items, enriches each selection with a fruit-nutrition API, then writes the submitted name and ingredient string to a Snowflake orders table.

## Experience

- Customer name input and immediate order preview
- Live ingredient options loaded from `smoothies.public.fruit_options`
- Maximum of five selected fruits
- Per-fruit lookup keys from the `SEARCH_ON` column
- Nutrition responses rendered as Streamlit dataframes
- Order confirmation after database insertion

## Data flow

```mermaid
flowchart LR
    A["Snowflake fruit_options"] --> B["Snowpark DataFrame"]
    B --> C["Streamlit multiselect"]
    C --> D["Nutrition API per fruit"]
    D --> E["Nutrition tables"]
    C --> F["Build ingredient string"]
    F --> G["Insert into Snowflake orders"]
    G --> H["Success confirmation"]
```

## Run locally

```bash
git clone https://github.com/TanishC4444/Snowflake_smoothies.git
cd Snowflake_smoothies
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Configure a Streamlit connection named `snowflake` with permission to:

- select `SMOOTHIES.PUBLIC.FRUIT_OPTIONS`;
- insert into `SMOOTHIES.PUBLIC.ORDERS`.

Store credentials in `.streamlit/secrets.toml` locally or the deployment secret manager, never in the repository.

## Expected data contract

```text
fruit_options: FRUIT_NAME, SEARCH_ON
orders:        INGREDIENTS, NAME_ON_ORDER
```

`SEARCH_ON` is used to call `https://my.smoothiefroot.com/api/fruit/<value>` for nutrition enrichment.

## Repository map

```text
Snowflake_smoothies/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Engineering notes

- Snowpark keeps table access native to the Snowflake session.
- The ingredient cap is enforced directly in the UI.
- API and database calls currently lack explicit timeout/error handling.
- The SQL insert is assembled with string interpolation; parameterization/escaping is required before accepting untrusted input.
- The fruit-options dataframe is passed directly to `multiselect`; using a clean list from the `FRUIT_NAME` column would make the contract clearer.
- There is no schema/bootstrap script or automated test.

## Skills demonstrated

Streamlit product development · Snowpark/Snowflake integration · external API enrichment · dataframe interop · database writes · secrets-based connection configuration

## Resume-ready highlight

> Built an interactive Streamlit ordering app that loads ingredient inventory through Snowpark, enriches selections with live nutrition data, enforces product constraints, and persists customized orders to Snowflake.

## License

No license file is currently included.

