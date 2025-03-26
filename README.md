# AI Native Dev Landscape - Export tools

This repo contains the code to export the tools from the AI Native Dev Landscape CSV file into a YAML file.

## Prerequisites
- uses python

## Exporting the tools
- export each tab in the Google Sheet as a CSV file
- naming should be as follows:
  - `AI Native Dev Tool Catalog - Internal - Tools.csv`
  - `AI Native Dev Tool Catalog - Internal - Domains.csv`
  - `AI Native Dev Tool Catalog - Internal - Categories.csv`
- place the CSV files in the `data/csv` folder

## Icons
- run `make yaml` to export to a single YAML file (data/yaml)
- run `make json` to export to a single json file (data/yaml)
- run `make icons` to download the icons (data/repo/data/icons)
- run `make repo` to export to a multi yaml data repo (data/repo)
