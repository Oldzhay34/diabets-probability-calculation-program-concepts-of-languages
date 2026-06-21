# Diabetes Probability Calculation Program

## Project Overview
This software is a custom-built, Graphical User Interface (GUI) desktop application designed to calculate the probability of a patient having diabetes based on 8 clinical metrics. Instead of relying on high-level machine learning libraries, the program implements the **K-Nearest Neighbors (KNN)** algorithm and **Euclidean Distance** calculations entirely from scratch. 

Developed as part of the CME 3402 Concepts of Programming Languages course, this project also features a polyglot approach, demonstrating the core Euclidean mathematical logic across 10 different programming languages.

## How It Works
The application performs real-time data mining and classification through the following pipeline:
1. **Data Preprocessing:** Reads the `diabetes.csv` dataset and normalizes all 8 feature columns using **Min-Max Scaling** ($N_{new} = (N_{old} - N_{min}) / (N_{max} - N_{min})$) to ensure uniform weight distribution across all dimensions.
2. **Input Validation:** Captures patient data via a Tkinter GUI, strictly validating inputs against the minimum and maximum boundaries of the training dataset.
3. **8-Dimensional Distance Calculation:** Calculates the Euclidean distance between the normalized user input and every normalized record in the dataset within an 8-dimensional space.
4. **Probability Extraction:** Sorts the dataset to find the user-defined $K$-closest neighbors. The final diabetes probability is calculated based on the ratio of diabetic patients within this subset.

## Multi-Language Implementations (Polyglot)
While the main application with the GUI is written in **Python**, the core 2D Euclidean Distance formula required for the algorithm has been implemented and provided in the following 10 programming languages to demonstrate syntax and paradigm versatility:
* `Go` (.go)
* `Rust` (.rs)
* `Ruby` (.rb)
* `COBOL` (.cob)
* `APL` (.apl)
* `Common LISP` (.lsp)
* `Prolog` (.pro)
* `Perl` (.pl)
* `JavaScript` (.js)
* `F#` (.fs)

## How to Run the Main Application
### Prerequisites
* Python 3.x
* Standard `tkinter`, `csv`, and `math` libraries (No `pip install` required).
* The `diabetes.csv` dataset must be placed in the specified directory.

### Execution
1. Clone this repository.
2. Ensure `diabetes.csv` is in the same directory or update the file path in the python script.
3. Run the application:
   ```bash
   diabets.py
