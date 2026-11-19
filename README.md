# Seyes Editor — French Ruled Paper & Penmanship Generator

**Seyes Editor** is a modern, high-precision desktop application for teachers and educators designed to generate authentic French Séyès ruled paper (grands carreaux) and render both official French cursive handwriting and primary manuscript print with **strict mathematical alignment to Séyès interlines**.

**Created by LOUCIF Soufiane**

---

## 🎯 The Core Problem Solved: Mathematical Grid Locking

In standard office word processors (Word, LibreOffice), computer fonts "float" arbitrarily between ruled lines because line heights are defined generically.

In an authentic French school copybook:
* **Base line (0):** All letters strictly rest on the solid blue baseline without floating.
* **1st interline (x-height = 2 mm):** Small lowercase letters without stems (`a, c, e, i, m, n, o, r, s, u, v, w, x, z`).
* **2nd interline (intermediate ascenders = 4 mm):** Intermediate stems (`d, t`).
* **3rd interline (tall ascenders & capitals = 6 mm):** Loops (`b, h, k, l, f`) and **all uppercase letters**.
* **2 interlines below baseline (-4 mm):** Descenders (`g, j, p, q, y, z`).
* **Special case of "f":** Reaches 3 interlines up and 2 interlines down (total 5 interlines).
* **Literacy Script Mode (Andika):** Configured so capital letters and tall ascenders (`b, d, f, h, k, l, t`) reach 2 green lines up, and small letters reach 1 green line up.

**Seyes Editor** calculates exact OpenType font metrics and projects vector glyph paths with sub-millimeter precision.

---

## 🚀 Key Features

### 1. Rich Text & Practice Tools
* **Interactive Practice Dots (Prompted Count):** Highlight any letter (e.g., `m`), click **Practice Dots**, and enter the desired count. Spaced red starting dots (`point d'attaque`) are placed on that exact line across the Séyès squares without altering dates, titles, or other text on the page.
* **Student Tracing Letters:** Click **Tracing Letters** to repeat letters in faint, dotted penmanship ink for students to trace directly with pencils.
* **Word & Letter Color Styling:** Highlight any word or character and apply colors individually (classic ballpoint blue, graphite pencil, correction red, teacher green, or custom picker).
* **Bold, Italic & Underline:** Apply bolding, italicization, and baseline-aligned underlines to selected words or phrases.
* **Clean Formatting Shortcuts:** Modern icon-free copybook formatting buttons for **Date**, **Underlined Title**, **Margin No.**, **Indent (2 sq.)**, and **Clear**.

### 2. Interactive On-Canvas Cropping & Line Drawing
* **On-Canvas Selection Tool:** Click the **Crop Page** button in the canvas toolbar to adjust an interactive crop rectangle with 8 resize handles.
* **Restricted Crop Exports:** Exports to vector PDF, high-resolution PNG, and Windows printing export only the cropped section.
* **Interactive Line Tool:** Click **Draw Line** on the canvas to place custom lines anywhere on the page (with automatic snapping to Séyès baselines and carreaux, custom colors, undo, and clear).

### 3. Modern UI with Light / Dark Mode & 2D Vector Icons
* **Light / Dark Mode Switcher:** Toggle between modern Light studio and sleek Dark studio themes from the main toolbar. The Séyès paper remains authentic white paper for print fidelity.
* **Modern 2D Icons & Chevrons:** Flat 2D vector icons and chevrons across toolbars, menus, and dropdowns.
* **Silent Windows Shortcut:** Launch Seyes Editor cleanly using `Seyes Editor.lnk` with the custom icon and zero console clutter.
* **Bilingual Instant Switching (FR / EN):** Seamlessly switch between French and English from the toolbar dropdown or menu without restarting.

### 4. Authentic Séyès French Ruling Engine
* **Standard Séyès Grid:** 8 mm squares subdivided into 4 interlines of 2 mm each.
* **Authentic School Colors:** Solid vibrant blue baseline, faint green intermediate lines, faint lilac vertical grid lines, and solid red margin.
* **Scale Presets:**
  * `2.0 mm`: Standard French primary/secondary (8 mm squares).
  * `2.5 mm`: Grade 2 / CE1 transition (10 mm squares).
  * `3.0 mm`: Grade 1 / CP early primary (12 mm squares).
  * `4.0 mm`: Kindergarten / Maternelle GS (16 mm squares).
  * Continuous slider from `1.5 mm` to `5.0 mm`.

### 5. Official Handwriting Fonts
* **Cursive Marelle & Marelle 2 (Recommended):** Official French Ministry of Education cursive penmanship font family with OpenType cursive attachment features.
* **Literacy Script — Andika (Recommended):** SIL Andika literacy script for reading, phonics, and elementary English.
* **Marelle Bâton & Marelle Bâton 2:** Elementary school print styles matching Algerian, French, and international primary schoolbooks.

### 6. Export & Direct Printing
* **Vector PDF (A4 or Custom Crop, 300 DPI):** Crisp, resolution-independent vector lines.
* **High-Resolution PNG:** 150 DPI (screen), 300 DPI (print), or 600 DPI (ultra-HD).
* **Direct Windows Print:** Native print dialog (`Ctrl+P`).

---

## 💻 Directory Structure

```
Sayes/
├── assets/
│   ├── icon.png                  # High-resolution application logo
│   ├── icon.ico                  # Multi-resolution Windows icon
│   └── fonts/
│       ├── Marelle-Regular.ttf       # Official French cursive
│       ├── Marelle2-Regular.ttf      # Simplified cursive (Cycle 2)
│       ├── MarelleBaton-Regular.ttf  # Primary print
│       ├── MarelleBaton2-Regular.ttf # Primary print (Cycle 2)
│       └── Andika-Regular.ttf        # Literacy script
├── seyes_engine/
│   ├── __init__.py
│   ├── models.py                 # Data models, StyledSpan, CustomLine, PaperConfig, TypographyConfig
│   ├── grid_renderer.py          # Vector Séyès grid renderer with cropping and custom lines
│   ├── typography_engine.py      # Millimetric glyph positioning, colors, bold, italic, bullets, tracing
│   ├── layout_engine.py          # Rich text parsing, word wrapping, selective dots
│   └── exporter.py               # Vector PDF, PNG, and Windows printing
├── ui/
│   ├── __init__.py
│   ├── main_window.py            # Primary window, menus, light/dark themes, 2D icons
│   ├── editor_panel.py           # Rich text editor, WYSIWYG toolbar, practice dots, tracing
│   ├── canvas_view.py            # High-DPI canvas preview, interactive crop & line drawing tools
│   ├── typography_panel.py       # Font selection, rendering modes, line spacing
│   ├── ruling_panel.py           # Grid scale slider, color pickers, margins
│   ├── templates.py              # Ready-to-use pedagogical templates
│   ├── pedagogical_guide_dialog.py # Teacher's reference guide
│   ├── icons.py                  # Crisp 2D vector icons
│   └── i18n.py                   # Bilingual translation manager (FR / EN)
├── Seyes Editor.lnk              # Windows desktop shortcut
├── main.py                       # Application bootstrap
├── run.bat                       # Windows launcher
└── requirements.txt
```

---

## 🛠️ Installation & Launch

### Prerequisites
* Windows 10 or 11
* Python 3.10+

### Steps
1. Run using the Windows shortcut:
   Double-click `Seyes Editor.lnk` directly in this folder.
2. Or run via batch file:
   Double-click `run.bat`.
3. Or run via PowerShell:
   ```powershell
   python main.py
   ```
