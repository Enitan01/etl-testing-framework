# etl-testing-framework
A lightweight, end‑to‑end ETL testing framework demonstrating ingestion validation, transformation testing, data‑quality checks, and source‑to‑target verification. This framework simulates a real-world data pipeline and demonstrates how to validate each stage using Python and PyTest.

## 📁 Project Structure
etl-testing-framework/
│
├── data/
│   ├── source_data.csv
│   ├── expected_output.csv
│
├── etl/
│   ├── pipeline.py
│   ├── transformations.py
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_transformations.py
│   ├── test_data_quality.py
│   ├── test_source_to_target.py
│
├── utils/
│   ├── validators.py
│
├── requirements.txt
└── README.md

---

## 🎯 Purpose of This Project

This repository demonstrates:

- ETL pipeline orchestration  
- Data transformation logic  
- Data quality validation  
- Source-to-target reconciliation  
- Automated testing using PyTest  
- Reusable validation utilities  
- Clean, maintainable test architecture  

It is ideal for showcasing ETL testing skills in interviews, portfolios, and GitHub profiles.

---

## 🚀 How to Run the Pipeline

```bash
python -c "from etl.pipeline import run_pipeline; import pandas as pd; print(run_pipeline('data/source_data.csv'))"
```
This command loads the source CSV, applies all transformations, and prints the curated output.


## 🧪 How to Run Tests

Install all dependencies

```bash
pip install -r requirements.txt
```

Run the full test suite

```bash 
pytest -v
```

Run a specific test file

```bash
pytest tests/test_transformations.py -v
```

Run a single test inside a file

```bash
pytest tests/test_data_quality.py::test_no_nulls -v
```


