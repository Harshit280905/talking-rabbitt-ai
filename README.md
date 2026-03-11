# Talking Rabbitt – Conversational Analytics MVP

## Overview
Talking Rabbitt is a prototype of a conversational intelligence layer for business analytics. Instead of navigating complex dashboards, users can upload a dataset and ask questions in natural language to instantly receive insights and visualizations.

This MVP demonstrates the "magic moment" where a user replaces manual Excel filtering or dashboard navigation with a simple question and gets an immediate answer.

## Features
- Upload a CSV dataset
- Ask questions about business data in natural language
- Automatic aggregation of insights
- Automated visualization (bar charts)
- Instant answers for quick decision-making

## Example Query
"Which region has the highest revenue?"

The system analyzes the dataset and returns:
- The top-performing region
- A bar chart showing revenue by region

## Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib

## Running the Project Locally
Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Demo Workflow
1. Upload the sample dataset (`sample_sales.csv`).
2. Ask a question such as "Which region has the highest revenue?"
3. The system returns a text insight and a visualization.

## Repository Structure

```
app.py
requirements.txt
sample_sales.csv
README.md
```

## Purpose
This project was built as part of the **Talking Rabbitt AI Product Manager Challenge**, demonstrating how conversational AI can transform business intelligence workflows.

## Vision
Talking Rabbitt aims to become a conversational layer on top of enterprise data, enabling leaders to simply "talk" to their business and instantly understand what is happening across their organization.