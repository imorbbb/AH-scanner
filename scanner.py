name: Daily Market Scanner Core

on:
  schedule:
    # Triggers automatically every Monday through Friday at 11:30 AM UTC (7:30 AM EST)
    - cron: '30 11 * * 1-5'
  workflow_dispatch: # Keeps the manual run button active inside the actions dashboard

permissions:
  contents: write # Crucial permission permitting the runner to save changes back to data.js

jobs:
  refresh-data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository code
        uses: actions/checkout@v4

      - name: Set up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      # FIXED STEP: Automatically inject parsing dependencies into the cloud session before executing code
      - name: Install System Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install beautifulsoup4 requests

      - name: Run Market Data Extraction
        run: |
          python scanner.py

      - name: Commit and Push fresh data.js to live site
        run: |
          git config --global user.name "Automated Scanner"
          git config --global user.email "actions@github.com"
          git add data.js
          git commit -m "Automated Morning Data Refresh [Skip CI]" || exit 0
          git push
