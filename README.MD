# 📊 Week 1 Lab — Student Grade Data Processing

A Python data-processing project built for the **AWS Student Builder Group — AASTU, Cohort 1**.

This project demonstrates how to load, clean, and analyze student grade data using Python and NumPy. It uses reusable Python modules for data processing and a Jupyter notebook to demonstrate the complete workflow.

##  Features

-  Load student grade data from a CSV file.
-  Clean dirty data using reusable Python functions:
  - Convert invalid grade values into missing values.
  - Fill missing subject scores using the subject average.
  - Remove records that cannot be repaired.
  - Remove duplicate student records.
-  Analyze cleaned data using NumPy:
  - Calculate class averages for each subject.
  - Identify the top student by overall average.
  - Calculate the pass rate using a specified threshold.
- Demonstrate the complete data-processing pipeline in a Jupyter notebook.

##  Project Structure

```text
week1-python-basics/
├── data/
│   └── students.csv       # Raw dataset with deliberate dirty data
├── data_loader.py         # Data loading and cleaning functions
├── analyzer.py            # NumPy analysis functions
├── lab.ipynb              # Jupyter notebook with the full pipeline
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Requirements

- Python 3.12
- pip
- Jupyter Notebook
- NumPy

## Getting Started

### 1. Clone the repository

```bash
git clone [week1-demo](https://github.com/semehal/week1-demo)
cd week1-deliverable
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## ▶️ Usage

### Option 1: Run the Jupyter Notebook

Start Jupyter Notebook:

```powershell
jupyter notebook lab.ipynb
```

Run the notebook cells in order to see the complete workflow, from loading the raw dataset to analyzing the cleaned data.

### Option 2: Run the Python Modules

Run the data loader:

```powershell
python data_loader.py
```

Run the analyzer:

```powershell
python analyzer.py
```

**Note:** Running these modules directly assumes they contain executable code for demonstrating their functions. The notebook is the main demonstration of the complete pipeline.

## 🗃️ Dataset and Data Cleaning

The file `data/students.csv` contains 10 rows of student grade data, including deliberately introduced data-quality problems.

| Data issue | Example | Cleaning approach |
|---|---|---|
| Missing value | Empty Physics score for Liya | Fill using the Physics average |
| Invalid value | `N/A` in Kebede's Physics score | Convert to a missing value |
| Duplicate record | Abebe's record appears twice | Keep only one copy |

After cleaning, the dataset contains **9 unique student records**, assuming the invalid and missing values are successfully handled by the cleaning pipeline.

## 🔍 How It Works

The project follows a simple data-processing pipeline:

1. **Load the data:** `load_data` reads the CSV file and converts grade values into numeric values. Values that cannot be converted become `None`.
2. **Fill missing values:** `fill_missing` replaces missing subject scores with the mean of the available scores for that subject.
3. **Remove unrepaired records:** `remove_bad_records` removes records that still contain missing values.
4. **Remove duplicates:** `remove_duplicates` keeps the first occurrence of each duplicate record.
5. **Analyze the data:** `analyzer.get_scores` converts the cleaned grades into a two-dimensional NumPy array, with students as rows and subjects as columns.
6. **Generate insights:** The analysis functions calculate subject averages, identify the top student, and determine the pass rate.

## 🧮 NumPy Concepts Practiced

This project provides hands-on practice with several important NumPy concepts:

- Creating and working with arrays.
- Converting data into numerical arrays.
- Calculating means and maximum values.
- Using `axis=0` to calculate averages across students for each subject.
- Using `axis=1` to calculate averages across subjects for each student.
- Applying Boolean conditions to calculate pass rates.
- Using `argmax()` to identify the index of the highest value.

## ⚠️ Limitations

- The dataset is small and manually created, so its results are for demonstration purposes.
- Filling missing grades with the subject mean assumes that the average is a reasonable estimate.
- The `subject_averages` function returns a NumPy array without subject labels.
- The project has limited input validation and does not include automated tests yet.
- Results depend on the dataset and the cleaning rules implemented.

## 📚 What I Learned

Through this project, I practiced:

- Working with CSV files in Python.
- Writing reusable functions and organizing code into modules.
- Handling missing, invalid, and duplicate data.
- Using NumPy for numerical analysis.
- Understanding array dimensions and axis-based calculations.
- Creating and managing Python virtual environments.
- Using Jupyter Notebook to demonstrate and document a data-processing workflow.
- Applying Git and GitHub to manage and share a project.

## 🎯 Project Goal

The goal of this lab is to build a foundation in Python data processing and numerical analysis as part of the **AWS Student Builder Group learning journey**.

---

**Built with 🐍 Python, 🔢 NumPy, and 📓 Jupyter Notebook.**
