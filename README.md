# 🎓 Student Account Management System (SAMS)

<div align="center">
  <img src="assets/samsrepologo.png" alt="SAMS Logo" width="150" height="150" />
</div>

A lightweight Python application designed to manage student accounts, grades, and academic records through a simple CLI. SAMS uses CSV files for data storage and retrieval — perfect for small-scale educational setups or learning projects.

<div align="center">
  <img src="assets/SAMSbg.png" alt="SAMS UI Preview" width="500" />
</div>

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🚀 Installation](#-installation)
- [⚙️ Usage](#-usage)
- [📋 Menu Options](#-menu-options)
- [📁 File Structure](#-file-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- ➕ **Add Student**: Register students with unique IDs, names, and grades  
- ❌ **Remove Student**: Remove student data using student ID  
- 🔄 **Update Student**: Modify student name or grade  
- 🧮 **Add Grade**: Assign subject-specific grades  
- 📊 **Student Average**: Calculate and display a student’s average score  
- 🔍 **View Student**: View detailed student information  
- 🧾 **View All**: Display all students in the system  
- 📄 **Generate Report**: Compile student grades and averages  
- 💾 **Export Report**: Save reports as CSV  
- 📥 **Load Data**: Load student data from CSV  
- 💾 **Save Data**: Save current session data to CSV  

---

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhiverse01/sams.git
    cd sams
    ```

2. **Install Python (v3.6+)** if you haven’t already.

3. **Dependencies**: No external packages required (uses Python standard library only).

---

## ⚙️ Usage

Run the application using:

```bash
python main.py
```

---

## 📋 Menu Options

| Option # | Operation              | Description |
|----------|------------------------|-------------|
| 1        | Add Student            | Add student ID, name, and grade |
| 2        | Remove Student         | Delete student record via ID |
| 3        | Update Student         | Modify student name or grade |
| 4        | Add Grade              | Add subject-specific grade |
| 5        | Get Student Average    | View average of grades |
| 6        | Get Student Details    | Show student profile |
| 7        | Display All Students   | Show all stored records |
| 8        | Generate Report        | Compile grade report |
| 9        | Export Report          | Save report to CSV |
| 10       | Save Data              | Save current session |
| 11       | Exit                   | Exit the program |

---

## 📁 File Structure

```
sams/
│
├── main.py             # Entry point of the application
├── sams.py             # Core logic of the SAMS system
├── students.csv        # Student data storage
├── report.csv          # Generated report storage
├── assets/
│   ├── samsrepologo.png
│   └── SAMSbg.png
└── README.md           # Project documentation
```

---

## 🤝 Contributing

I welcome all contributions! 🚀  
To contribute:

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).



---
