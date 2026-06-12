# 🌐 Google Translate App

A simple desktop **language translator** built with Python using `tkinter` for the GUI and `googletrans` for translation. Supports 100+ languages with a clean red-themed interface.

---

## 📁 Project Structure

```
Google_translate/
├── Google_translate.py      # Main application file
└── .vscode/
    ├── settings.json
    ├── launch.json
    └── c_cpp_properties.json
```

---

## ✅ Requirements

- Python 3.7 or higher
- `tkinter` (usually built-in with Python)
- `googletrans==4.0.0-rc1`

---

## 🪟 Setup on Windows

### Step 1 — Install Python

1. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. During installation, **check the box** → ✅ *Add Python to PATH*
3. Verify installation:
   ```cmd
   python --version
   ```

### Step 2 — Install Required Library

Open **Command Prompt** (`Win + R` → type `cmd` → Enter) and run:

```cmd
pip install googletrans==4.0.0-rc1
```

> ⚠️ Make sure to install **exactly this version** (`4.0.0-rc1`). Other versions may not work correctly.

### Step 3 — Extract the Project

Unzip `Google_translate.zip` to any folder, e.g.:
```
C:\Users\YourName\Desktop\Google_translate\
```

### Step 4 — Run the App

Navigate to the project folder and run:

```cmd
cd C:\Users\YourName\Desktop\Google_translate
python Google_translate.py
```

Or simply **double-click** `Google_translate.py` if Python is associated with `.py` files.

---

## 🐧 Setup on Ubuntu (Linux)

### Step 1 — Install Python & pip

Open **Terminal** and run:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

Verify:
```bash
python3 --version
pip3 --version
```

### Step 2 — Install tkinter

`tkinter` is not always pre-installed on Ubuntu. Install it with:

```bash
sudo apt install python3-tk -y
```

### Step 3 — Install Required Library

```bash
pip3 install googletrans==4.0.0-rc1
```

### Step 4 — Extract & Run the App

```bash
unzip 1781254006629_Google_translate.zip
cd Google_translate
python3 Google_translate.py
```

---

## 🚀 How to Use

1. **Type or paste** text in the **Source Text** box.
2. Select the **source language** from the left dropdown (default: English).
3. Select the **destination language** from the right dropdown (default: Hindi).
4. Click the **Translate** button.
5. The translated text will appear in the **Translated Text** box below.

---

## 🐛 Common Issues

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'googletrans'` | Run `pip install googletrans==4.0.0-rc1` |
| `ModuleNotFoundError: No module named 'tkinter'` | Run `sudo apt install python3-tk -y` (Ubuntu only) |
| Translation error or blank output | Check your internet connection; `googletrans` requires internet |
| App doesn't open on double-click (Windows) | Open CMD, navigate to folder, run `python Google_translate.py` |

---

## 📌 Notes

- An **active internet connection** is required for translation to work.
- Supports **100+ languages** (all languages available in Google Translate).
- Built with `tkinter` — no additional GUI framework needed.
