# WMS Inventory ETL (Python)

## Overview
Python ETL pipeline that extracts WMS inventory data, cleans/transforms it, and loads it into a database for reporting and analytics.

## Data (Example Columns)
WHCode, Client, Item, Qty, Unit, PieceNo, Status, Aisle, Column, Row, EntryDate, CodeDate, Document

## What the Pipeline Does
- **Extract:** Reads inventory files (CSV/Excel) from `/data/raw`
- **Transform:** Cleans data (types, blanks, duplicates, business rules)
- **Load:** Loads standardized output to (Azure SQL / local DB)

## Project Structure
- `src/extract.py` – ingestion
- `src/transform.py` – cleaning & rules
- `src/load.py` – database load
- `src/main.py` – orchestrates pipeline

## How to Run
1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
