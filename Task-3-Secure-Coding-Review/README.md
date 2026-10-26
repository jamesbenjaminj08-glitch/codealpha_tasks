Secure Coding Review

CodeAlpha Cybersecurity Internship — Task 3

Project Overview

This project demonstrates a basic security review of a Python application that searches for users in an SQLite database. It identifies a potential SQL injection vulnerability and demonstrates how parameterized queries help prevent it.

Features

Demonstrates a common SQL injection risk in a controlled example.

Uses parameterized SQL queries in the corrected program.

Includes a security review report.

Tests user lookup with sample data stored in an in-memory SQLite database.

Technologies Used

Python

SQLite

Project Files

secure_app.py — corrected Python program.

SECURITY_REVIEW.md — vulnerability analysis, remediation, testing, and recommendations.

README.md — project documentation.

Requirements

Python 3

SQLite support included with Python

How to Run

Open Command Prompt.

Navigate to the project folder.

Run:

python secure_app.py

Enter alice or admin when prompted.

Security Improvement

The corrected program uses a parameterized query:

query = "SELECT username, role FROM users WHERE username = ?"
cursor.execute(query, (username,))

This separates user-supplied data from SQL instructions and helps prevent SQL injection.

Conclusion

This project demonstrates the importance of secure database query construction and documenting security findings during a code review.

Ethical Use

Created for educational cybersecurity training. Review and test only systems you own or are authorised to assess.
