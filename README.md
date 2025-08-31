Bookstore (pretty & fun) 📚✨

> **Tiny, slick, local bookstore manager** — fullscreen Tkinter GUI + SQLite.
> For demos, small shops, or your weekend hacking spree. Zero fluff, max vibes.

![status-badge](https://img.shields.io/badge/status-alpha-orange) ![python](https://img.shields.io/badge/python-3.8%2B-blue) ![license](https://img.shields.io/badge/license-MIT-green)

---

# What’s this? 🤔

This is a minimal **Bookstore GUI** app built with **Tkinter** and **SQLite**.
Add books, sell them, search, remove — everything runs locally in a tiny `books.db`. Perfect for learning, demos, or running on a tiny laptop.

> TL;DR: simple UI, small DB, zero server drama. 🚀

---

# Features ✨

* 🎯 Fullscreen Tkinter GUI for quick operations
* ➕ Add books (name, author, price, ISBN, qty)
* 🛒 Sell books (decrements stock, tracks runtime sales)
* 🔎 Search by title / author
* 🗑️ Remove books / list all books
* 🧾 Small, single-file SQLite DB (`books.db`) — portable and neat

---

# Quick start (local) — 2 minutes ⏱️

```bash
git clone https://github.com/your-username/bookstore-gui.git
cd bookstore-gui
# create & activate venv
python -m venv .venv
# windows:
.venv\Scripts\activate
# linux/mac:
# source .venv/bin/activate

# install (no external deps)
python main.py
```

> Tip: Press `Esc` to toggle fullscreen off if you want. 🎛️

---

# Files you care about 🗂️

* `main.py` — app entrypoint, launches the GUI.
* `database.py` — DB layer: create table, add/sell/remove/search logic.
* `gui.py` — Tkinter UI: forms, buttons, listbox, dialogs.

(keep UI & DB separated — good taste, my friend) 😎

---

# How it works — short & sweet 🔧

1. On start, `database.py` ensures the `books` table exists.
2. `Bookstore` loads DB rows into the GUI list.
3. Add/Sell/Remove actions update DB and refresh the UI.
4. `total_sales` tracked at runtime (you can persist it if you want).

---

# Nice-to-have upgrades (ideas) 💡

* Persist `total_sales` to DB (add `sales` table).
* CSV import/export + scheduled DB backups.
* Input validation & nicer error handling (prevent `ValueError` meltdowns).
* Unit tests for DB functions.
* Small REST API wrapper if you later want remote control.

---

# Troubleshooting & tips 🛠️

* `tkinter` missing on Linux → `sudo apt install python3-tk`.
* If `books.db` not visible: check working directory & permissions.
* Invalid input crashes = make sure price/qty are numbers — GUI expects `float`/`int`.
* Want to stop committing DB? Add `books.db` to `.gitignore`. 🔒

---

# Requirements 📦

```text
Python 3.8+
tkinter (system package on some OSes)
sqlite3 (stdlib)
```

No fancy pip packages required — keep it tiny.

---

# Contributing (if you feel spicy) 🍜

1. Fork → branch `feature/awesome-thing`
2. Keep code & comments in **English**
3. Small commits, tests when possible
4. Open a PR with screenshots/GIFs if you tweak UI

---

# License 📝

MIT — do whatever (but don't steal my coffee). ☕️

---

