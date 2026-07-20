# my-econ-app

[![CI](https://github.com/mayutori/my-econ-app/actions/workflows/ci.yml/badge.svg)](https://github.com/mayutori/my-econ-app/actions)

A CLI tool to automatically fetch key economic indicators (USD/JPY, Nikkei 225, S&P 500) and generate normalized PDF report plots.

## Overview
This software fetches historical financial data via Yahoo Finance, calculates key economic metrics, and outputs a normalized time-series chart in PDF format.

## Usage

Run the following command to fetch data and generate a PDF report:

```bash
uv run econ-report