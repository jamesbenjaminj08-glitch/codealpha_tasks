Secure Coding Review

Internship: CodeAlpha Cybersecurity Internship
Task: Task 3 — Secure Coding Review
Language: Python
Database: SQLite

1. Project Overview

This project demonstrates a basic secure coding review using a Python program that searches for users in an SQLite database. The review identifies an SQL injection risk and demonstrates how to fix it using parameterized queries.

2. Vulnerability Identified

Vulnerability: SQL Injection
Severity: Potentially High, depending on the application and database permissions.

Original insecure approach

The original code inserted user input directly into an SQL query using an f-string.

This can allow specially crafted input to change the meaning of the SQL statement.

Potential impact

Unintended database records could be retrieved.

Database queries could behave unexpectedly.

In applications with broader database permissions, the impact could be more serious.

3. Security Fix Applied

The query was changed to use a parameterized statement:

query = "SELECT username, role FROM users WHERE username = ?"
cursor.execute(query, (username,))

The username is passed separately from the SQL statement. SQLite treats it as data instead of executable SQL syntax.

4. Testing

The corrected program was executed successfully.

Test input: alice

Expected result: The program displays Alice's username and the user role.

Observed result: The program ran successfully and displayed the expected user record.

5. Security Recommendations

Use parameterized queries for database operations.

Validate user input according to application requirements.

Apply least-privilege permissions to database accounts.

Avoid exposing sensitive information in error messages.

Store credentials securely rather than hardcoding them.

Perform regular code reviews and security testing.

6. Conclusion

The review demonstrated how unsafe SQL query construction can introduce SQL injection risks. Replacing direct string interpolation with parameterized queries improves the program's security and provides a useful example of secure coding practice.

7. Ethical Use

This project is intended for educational cybersecurity training. Testing should be limited to applications and systems that the tester owns or is authorised to assess.