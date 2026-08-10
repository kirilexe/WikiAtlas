# WikiAtlas • [![Python](https://img.shields.io/badge/Python-3.14-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

A curiousity driven project that maps Wikipedia article relationships as interactive network graphs. Scrapes Wikipedia and visualizes relationships between different links.

> WARNING: This is still WIP and for fun, not a serious project.

## What it does
Crawls Wikipedia starting from any article, follows links through configurable depth levels, and generates an interactive  graph visualization. Shows how Wikipedia articles are connected with each other.

**Example:** Starting from "Animal" -> scrapes related articles -> generates a graph revealing semantic clusters (cells, biology, ecology, etc.) without manual categorization.

## Showcase of a graph generated from the "Animal" article:

### Zoomed out
<img width="1824" height="853" alt="image" src="https://github.com/user-attachments/assets/0ef9c1e0-5d67-4762-9467-0979cf840e86" />

*The entire map of the "Animal" article with depth = 40.*

### Closer showcase
<img width="1431" height="753" alt="image" src="https://github.com/user-attachments/assets/326766cc-fb11-4c45-805b-42dc48ad741c" />

*All of the related articles are shown, the more connections a node has the bigger it gets.*

## Setup

*Download the needed libraries:*
```bash
pip install -r requirements.txt
```

*Start WikiAtlas:*
```bash
python main.py
```
