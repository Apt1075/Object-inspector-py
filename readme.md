# 🔍 Python Object Inspector

A simple Python script that inspects user-provided objects and displays useful details like type, size, mutability, and value.

## 🚀 Features
- Convert string input to Python objects safely using `ast.literal_eval`.
- Identify if an object is **mutable** (list, dict, set, bytearray).
- Display attributes such as value, type, size, Memory, and mutability.

---

## 🛠️ Requirements
- Python 3.7+

No external libraries are required.

---

## ▶️ Usage

Run the script:

```bash
python object_inspector.py
```

It will ask for an input:

```
Welcome to object inspector
Please enter the object you want to inspect: [1, 2, 3]
```

✅ Example Output:
```
Object Inspection:
----------------------------------------
Value    : [1, 2, 3]
Type     : <class 'list'>
Size     : 88
Memory   : 1505141171584
Mutable  : Yes
----------------------------------------
```

Another Example:
```
Please enter the object you want to inspect: 42
```
Output:
```
Object Inspection:
----------------------------------------
Value  : 42
Type   : <class 'int'>
Size   : 28
Mutable: No
----------------------------------------
```

---

## 📄 License
This project is licensed under the MIT License.
