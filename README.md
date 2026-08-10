# WikiAtlas • [![Python](https://img.shields.io/badge/Python-3.14-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

A curiousity driven project that maps Wikipedia article relationships as interactive network graphs. Scrapes Wikipedia and visualizes relationships between different links.

> WARNING: This is still WIP and for fun, not a serious project.

## What it does
Crawls Wikipedia starting from any article, follows links through configurable depth levels, and generates an interactive  graph visualization. Shows how Wikipedia articles are connected with each other.

**Example:** Starting from "Animal" -> scrapes related articles -> generates a graph revealing semantic clusters (cells, biology, ecology, etc.) without manual categorization.

## Showcase of a graph generated from the "Animal" article: (OLD)

### Zoomed out
<img width="1790" height="827" alt="image" src="https://github.com/user-attachments/assets/59d33138-7d89-47e8-865f-1d315592bd08" />

### Closer showcase
<img width="1847" height="849" alt="image" src="https://github.com/user-attachments/assets/c608cf03-82c6-4905-ba06-d00ba0b8ea91" />

## Setup

*Download the needed libraries:*
```bash
pip install -r requirements.txt
```

*Start WikiAtlas:*
```bash
python main.py
```
