# Student Result Analyzer

A Python-based academic performance analysis tool that processes student marks, calculates averages, ranks students, and generates performance reports.

---

## Features

- Read student marks from CSV files
- Calculate average marks
- Generate student rankings
- Identify top performer
- Identify lowest performer
- Export analysis report to CSV
- Display class statistics

---

## Technologies Used

- Python
- Pandas

---

## Project Structure

```text
student-result-analyzer/
│
├── analyzer.py
├── students.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/student-result-analyzer.git
```

Move into the project folder:

```bash
cd student-result-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python analyzer.py
```

---

## Sample Dataset

```csv
Name,Math,Science,English
Alice,85,90,88
Bob,70,65,75
Charlie,95,92,98
David,60,72,68
Emma,88,85,91
```

---

## Example Output

```text
========== STUDENT RESULT ANALYSIS ==========

Overall Statistics
----------------------------------------
Class Average: 82.13
Highest Average: 95.00
Lowest Average: 66.67

Top Performer
----------------------------------------
Charlie (95.00)

Lowest Performer
----------------------------------------
David (66.67)

Student Rankings
----------------------------------------
Rank  Name      Average
1     Charlie   95.00
2     Emma      88.00
3     Alice     87.67
4     Bob       70.00
5     David     66.67
```

---

## Future Enhancements

- Data visualization using Matplotlib
- PDF report generation
- Streamlit dashboard
- Subject-wise analytics
- Student performance prediction using Machine Learning

---

## License

MIT License
