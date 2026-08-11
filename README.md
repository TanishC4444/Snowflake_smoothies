# Snowflake Smoothies

A Streamlit smoothie-order application that uses Snowpark and Snowflake for data-backed application workflows.

## Overview

Snowflake Smoothies demonstrates how a small interactive Streamlit application can connect to Snowflake data and integrate an API-driven fruit search workflow.

## Features

- Streamlit web interface
- Snowflake/Snowpark integration
- Data-backed smoothie workflow
- API-driven fruit search
- Local development configuration

## Prerequisites

- Python 3.10+
- pip
- Snowflake account and connection configuration

## Installation

```bash
git clone https://github.com/TanishC4444/Snowflake_smoothies.git
cd Snowflake_smoothies
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

## Quick Start

```bash
streamlit run streamlit_app.py
```

## Configuration

Store Snowflake credentials in Streamlit secrets, environment variables, or your deployment platform's secret manager. Never commit credentials to the repository.

## Status

Learning project demonstrating Streamlit and Snowflake integration.

## License

No separate license is currently specified in the repository.

## Support

Use GitHub Issues for bugs and questions.
