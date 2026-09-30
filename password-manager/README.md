# SyntecxHub Password Manager

A simple command-line password manager developed in Python as part of my SyntecxHub internship tasks.

The application allows users to securely store, search, view, and delete website/app credentials. Password data is stored locally in an encrypted file using Fernet encryption.

## Features

* Set a Master Password on first use
* Verify the Master Password before accessing stored credentials
* Add website/app credentials
* Search and retrieve saved credentials
* View all saved credentials
* Delete saved credentials
* Encrypt stored password data using Fernet
* Store password data locally in an encrypted file

## Technologies Used

* Python
* Cryptography
* Fernet Symmetric Encryption
* JSON
* SHA-256 Hashing
* `getpass` for password input

## Project Structure

```text
Password-Manager/
│
├── password_manager.py
├── README.md
```

### Local Runtime Files

The following files are generated locally when the application runs:

```text
master.key
secret.key
passwords.enc
```

These files are **not included in this GitHub repository** because they may contain sensitive authentication or encrypted credential data.

## Requirements

Python 3.x

Install the required library:

```bash
pip install cryptography
```

## How to Run

Open the project folder:

```bash
cd Password-Manager
```

Install the dependency:

```bash
pip install cryptography
```

Run the program:

```bash
python password_manager.py
```

## How It Works

### 1. Master Password

On the first run, the application asks the user to create a Master Password.

The Master Password is hashed using SHA-256, and the hash is stored locally.

On later runs, the entered password is verified against the stored hash.

### 2. Password Encryption

The application uses the `cryptography` library and Fernet symmetric encryption.

Saved credentials are converted into JSON and encrypted before being stored locally in:

```text
passwords.enc
```

### 3. Add Credentials

Select:

```text
1. Add
```

Then enter:

* Website/App
* Username
* Password

### 4. Search Credentials

Select:

```text
2. Search/Retrieve
```

Enter the website or app name to find the saved credentials.

### 5. View All Credentials

Select:

```text
3. View All
```

This displays all stored credentials.

### 6. Delete Credentials

Select:

```text
4. Delete
```

Enter the website/app name that you want to remove.

### 7. Exit

Select:

```text
5. Exit
```

to close the application.

## Example

```text
Set Master Password (First Time)
New Master Password: ********

[+] Master set

Enter Master Password: ********

1.Add 2.Search/Retrieve 3.View All 4.Delete 5.Exit
Choice: 1

Website/App: github
Username: example@email.com
Password: ********

[+] Added
```

## Security Notes

* The Master Password is not stored as plain text; its SHA-256 hash is stored locally.
* Stored credential data is encrypted using Fernet before being written to disk.
* The encryption key is stored locally in `secret.key`.
* Runtime files containing sensitive information are excluded from the GitHub repository using `.gitignore`.
* Do not upload your personal `master.key`, `secret.key`, or `passwords.enc` files to GitHub.

> **Note:** This project is developed for learning and internship purposes. For real-world password management, use a professionally audited password manager and follow established security practices.

## Internship

This project was developed as part of my **SyntecxHub internship tasks** to practice Python programming, file handling, authentication, hashing, encryption, and basic security concepts.

## Author

**Nasheman Arshad**

BS in Computer Engineering
