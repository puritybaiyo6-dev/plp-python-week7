# Week 7 Assignment: Shopping List Manager

This project demonstrates Python list operations, loops, membership checks, and list reporting.

## Files

- `list_warmup.py` — Demonstrates indexing, adding and removing fruits, and counting items.
- `shopping_list.py` — Provides an interactive shopping list manager with add, remove, show, and done options.
- `list_report.py` — Prints a numbered shopping list, counts item names longer than four characters, and finds the longest name.
- `screenshots/` — Contains screenshots showing the output of all three programs.

## Why check `in` before calling `.remove()`?

Checking whether an item exists before calling `.remove()` prevents a `ValueError` when the item is not in the list. It also lets the program display a helpful message instead of stopping unexpectedly. This makes the shopping list manager safer and more user-friendly.