# 🔐 PyQt6 Password Generator

A simple and elegant desktop GUI application for generating secure passwords. Built with **PyQt6**, this tool supports multiple character set options and includes a dark theme for comfortable use.

---

## 🖼️ Features

- ✅ **Password generation** with customizable length (4–40 characters)
- 🔣 Toggle inclusion of:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Symbols
- 🌙 **Dark theme** with consistent and visible UI elements (slider ticks, checkboxes, labels)
- 📋 Copy password to clipboard with a single click
- ⚠️ Input validation (requires at least one character set)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `PyQt6`

### Install dependencies

```bash
pip install PyQt6
```

### Run the app

```bash
python main.py
```

---

## 🗂️ Project Structure

```
.
├── main.py            # Entry point, applies Fusion style and dark palette
├── GUI.py             # Defines the main window and GUI layout
├── logic.py           # Password generation logic
├── palettes.py        # Dark theme palette configuration
└── misc/
    └── pass_gen_logo.png   # (Optional) Icon for the application
```

---

## 🎨 Theming

The application uses the `Fusion` style and a custom dark palette defined in `palettes.py`. All critical UI components (e.g. slider ticks and labels) remain visible and accessible in dark mode.

---

## 📄 License

This project is free to use, modify, and distribute. No specific license is attached by default—feel free to add one if you wish.
