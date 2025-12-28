# Simple Adder (Tkinter)

A minimal GUI app that adds two numbers using Python's `tkinter` library.

## 🔧 Features

- Simple GUI with two input fields
- Add two numbers and show the result
- Clear inputs with a button

## ✅ Requirements

- Python 3.8+ (or any Python 3)
- `tkinter` (usually included with Python on Windows/macOS)
  - On Debian/Ubuntu: `sudo apt install python3-tk`

## 🚀 Installation & Running

1. Download or clone this repository to your local machine.
2. Run the app from the command line:

```bash
python "simple adder.py"
```

Or just double-click the file in most graphical environments.

## 🧭 Usage

1. Enter a number in each field.
2. Click **Add Numbers** to calculate the sum (the app currently displays the sum as an integer).
3. Click **Clear** to reset the fields.

## 📝 Notes & Suggestions

- The app reads inputs as floats but currently displays the result with `int(...)`, so decimal parts are dropped; change this if you want full float precision:

```python
# change
result_lable.config(text=f"sum:{int(num1 + num2)}")
# to
result_lable.config(text=f"Sum: {num1 + num2}")
```

- There's a minor variable name typo `result_lable` ("label" is misspelled). It works as-is but you might want to rename it to `result_label`.
- Consider adding input validation and friendly error messages for non-numeric inputs.

## Contributing

Pull requests are welcome. For larger changes, please open an issue first to discuss what you'd like to change.

## License

This project is provided under the MIT License. See `LICENSE` if included.

---

If you want, I can also help create a `LICENSE`, add tests, or prepare a `.gitignore` and a short commit history for pushing to GitHub. 😊
