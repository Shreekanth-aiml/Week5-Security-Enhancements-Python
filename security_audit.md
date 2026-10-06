# Week 5 Security Audit

## Application

Python User Login Application

---

## Vulnerability 1: Plain-Text Password Storage

The original application stores usernames and passwords directly inside the Python source code.

Example:

```python
users = {
    "admin": "admin123",
    "student": "password123"
}
```
