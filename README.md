# 📦 Pacify — Object & Contact Manager

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge"/>
</p>

<p align="center">
  A lightweight Python CLI tool to <strong>store, manage, find, edit, and email</strong> your objects/contacts — all from the terminal.
</p>

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📝 **Store Data** | Save object records (Name, ID, Email) persistently in `Data.py` |
| 🔍 **Find by ID** | Search and display any object using its unique ID |
| ✏️ **Edit Details** | Update an object's Name, ID, or Email at any time |
| 📧 **Email All** | Send a bulk email to every object stored in your data |
| 💌 **Email Specific** | Target and email a single object by their ID |
| 🗑️ **Clear Data** | Wipe all stored records with a single command |

---

## 📁 Project Structure

```
📦 Pacify/
├── 📄 main.py           # Entry point — handles all menu logic & operations
├── 📄 Login_page.py     # Handles data input & persistent storage
├── 📄 Data.py           # Acts as a local database (auto-updated at runtime)
└── 📄 Background.py     # Contains ASCII art & branding visuals
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pacify.git
cd pacify
```

### 2. Install Dependencies

```bash
pip install prettytable
```

> All other modules (`smtplib`, `email`, `pprint`) are part of Python's standard library.

---

## ▶️ Usage

```bash
python main.py
```

On first launch, you'll be prompted to enter your objects/contacts. After that, the main menu will appear:

```
+------+------------------------------------------+
| No.  | Options You Have                         |
+------+------------------------------------------+
|  1.  | Remove all data from your device         |
|  2.  | E-mail all objects                       |
|  3.  | E-mail a specific object by ID           |
|  4.  | Edit details of an object                |
|  5.  | Find an object by ID                     |
+------+------------------------------------------+
```

---

## 📧 Email Feature Setup

The email functionality uses **Gmail SMTP**. Before using it:

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Generate an **App Password** under *App Passwords*
4. Use that App Password when prompted by Pacify

> ⚠️ Only **Gmail** accounts are currently supported. More providers coming in a future update.

---

## ⚠️ Important Notes

- 🌐 **Internet is required** for all email features
- 🔄 After adding or clearing data, **restart the program** for changes to take effect
- 🔑 Never share your **App Password** publicly or commit it to version control
- 📂 `Data.py` is your local database — don't manually edit it unless you know what you're doing

---

## 🛠️ Requirements

- Python **3.10+**
- [`prettytable`](https://pypi.org/project/prettytable/) — for table formatting in the terminal
- A **Gmail account** with App Password enabled (for email features)

---

## 🗺️ Roadmap

- [ ] Support for more email providers (Outlook, Yahoo, etc.)
- [ ] Export data to CSV or JSON
- [ ] Search by Name or Email (not just ID)
- [ ] GUI version using Tkinter or PyQt
- [ ] Encrypted data storage

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ by Lakshitpythondevloper

> *"Pacify your data chaos — one object at a time."*
