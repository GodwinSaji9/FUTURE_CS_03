# Secure File Sharing System using AES Encryption

# Project Overview
This project implements a secure file sharing system that allows users to upload and download files safely using AES encryption. Files are encrypted before storage and decrypted only at the time of download, ensuring data confidentiality and protection against unauthorized access.
The project simulates real-world secure data sharing scenarios commonly used in healthcare, legal, and corporate environments, where sensitive information must be protected both at rest and during transfer.
This project was completed as part of a SOC / Cybersecurity Internship Task focusing on secure application development and encryption fundamentals.

# Objectives
•	Build a simple web-based file upload and download system
•	Encrypt all uploaded files using AES-256
•	Prevent plain text file storage on the server
•	Demonstrate basic encryption key handling
•	Document security architecture and design decisions

# Technologies Used
Backend
•	Python
•	Flask – Web framework
Cryptography
•	PyCryptodome
•	AES (Advanced Encryption Standard)
•	CBC mode
•	Secure random key generation
Frontend
•	HTML
•	CSS (basic UI styling)
Tools
•	Git & GitHub
•	Browser (for testing uploads/downloads)


 # Security Features
•	AES-256 Encryption
•	CBC (Cipher Block Chaining) mode
•	Random Initialization Vector (IV) per file
•	PKCS7 padding for block alignment
•	No plain text files stored permanently
•	Encrypted files stored with .enc extension
•	Key is kept in memory only (not written to disk)

# Application Workflow
File Upload
1.	User selects a file via the web interface
2.	File is uploaded to the server
3.	File content is encrypted using AES-256
4.	Encrypted file is saved
5.	Original plaintext file is deleted

File Download
1.	User clicks the download button
2.	Encrypted file is decrypted in memory
3.	Decrypted file is sent to the user
4.	Temporary decrypted file is removed

# Learning Outcomes
•	Implemented AES encryption in a real application
•	Understood encryption modes and IV usage
•	Learned secure file handling practices
•	Gained hands-on experience with Flask
•	Improved documentation and security design skills
