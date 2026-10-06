# Week 5 - Security Enhancements in Python

## Project Overview

This project focuses on identifying security vulnerabilities in a Python login application and implementing security improvements.

The project contains an insecure version and a secure version of the application.

## Security Vulnerabilities Identified

The initial application had the following security weaknesses:

1. Plain-text password storage
2. Weak passwords
3. Hard-coded credentials
4. Lack of input validation
5. Password entered visibly in the terminal

## Security Improvements

The secure application includes:

- Password hashing using PBKDF2-HMAC-SHA256
- Random salt generation using Python's secrets module
- Hidden password input using getpass
- Username and password validation
- Secure password comparison using secrets.compare_digest()
- Generic error messages
- Avoidance of plain-text password storage

## Testing

The secure application was tested with:

- Correct password
- Incorrect password
- Empty username
- Empty password

All tests passed successfully.

## Files

- `insecure_app.py` - Original insecure application
- `secure_app.py` - Security-enhanced application
- `security_audit.md` - Security audit and vulnerabilities
- `test_results.txt` - Security testing results
- `README.md` - Project documentation
- `Week5_Security_Report.docx` - Final security report

## Conclusion

The project demonstrates how common security weaknesses can be identified and addressed using secure Python coding practices. The improved application maintains its login functionality while providing stronger password protection, input validation, and safer error handling.
