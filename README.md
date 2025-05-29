# secure-file-storage
The Secure File Sharing System is a web-based application designed to provide users with a secure and user-friendly platform for managing their personal files online.
## License
MIT License
## Getting Started
Secure File Sharing System

## Project Overview
The Secure File Sharing System is a web-based application designed to provide users with a secure and user-friendly platform for managing their personal files online. Developed using Python (Django) for the backend, MySQL for data storage, and a responsive frontend built with HTML, CSS, and Bootstrap, the system focuses on key aspects such as data security, user authentication, and efficient file management.

This project aims to strike a balance between simplicity, user control, and strong security, offering a practical solution for secure file sharing and management in both personal and collaborative settings. It's ideal for academic, organizational, or personal use where privacy and controlled access are priorities.

## Features
The system offers a range of features for both administrators and regular users:

User Module Features 
  * User Registration and Login: Users can create personal accounts and log in to a dedicated dashboard.
  * Profile Management: View and update personal profile information.
  * Secure File Management:
    * Upload: Securely upload files to a protected server environment.
    * View & Download: View and download their own files.
    * Delete: Delete their own files within the protected environment.
    * Files are accompanied by metadata (filename, file type, upload timestamp) for traceability and organization.
  * Controlled File Sharing: By default, users can only view and manage their own uploaded files. 
    * Users can send file access requests to view files uploaded by others.
    * Access is granted only upon approval from the original uploader, ensuring full control.
  * Feedback Mechanism: Users can submit feedback, suggestions, or report issues to contribute to continuous improvement.

Admin Module Features 
  * User Management: View and manage all registered users, including usernames, email addresses, and account status. This allows monitoring user activity, handling misuse, or deactivating accounts.
  * File Oversight: Access and manage all uploaded files within the system, including viewing file metadata and deleting inappropriate or harmful files to maintain platform integrity.
  * Feedback Management: View, respond to, and take necessary actions based on user feedback to improve system performance and user experience.

## Advantages of the Proposed System 
The system overcomes the drawbacks of manual systems by offering:

* Reduced manual work, saving time and effort.
* Elimination of wrong entries, providing accurate reports.
* Reduced paperwork and extra costs.
* Avoidance of data redundancy and inconsistency.
* Enhanced data security.
* Faster information retrieval.
* User-friendliness and flexibility.

# Technologies Used

* Backend
  * Framework : Django (Version 5) 
  * Language : Python 
  * Database : MariaDB / MySQL (Version 10.6 MariaDB) 
  * Database Tool : HeidiSQL 

* Frontend
  * Markup Language : HTML (Version HTML5) 
  * Styling : CSS (Version CSS3) 
  * Scripting : JavaScript 
  * Framework : Bootstrap 

* Development Environment
  * IDE/Editor : PyCharm 

* System Requirements
  * Operating System : Windows 
  * Processor : Intel i5 (10th or 11th Gen) and above 
  * System Type : 64-bit Operating System, x64 based processor 
  * RAM : 8GB 
  * Hard Disk : 512 SSD 

## Installation & Setup Instructions

To run this project locally, you will need to:

1. Clone the repository : ***git clone [https://github.com/sidharthrmenon/FileVault-Encrypted-Storage.git]***
2. Navigate to the project directory : ***cd FileVault-Encrypted-Storage***
3. Set up a Python virtual environment (recommended).
4. Install dependencies : Use a ***requirements.txt*** file (you'll need to create this if you haven't) to install Django, MySQL client, etc.\

   Example: ***pip install -r requirements.txt***

5. Configure Database : Set up your MySQL/MariaDB database and update your Django ***settings.py*** with the database credentials.
6. Apply migrations : ***python manage.py makemigrations*** followed by ***python manage.py migrate***
7. Create a superuser : ***python manage.py createsuperuser*** (for admin access)
8. Run the development server : ***python manage.py runserver***

## Future Enhancements
The documentation mentions a section for future enhancements. While the specific details are not provided in the extracted content, this section should be updated to include any planned improvements or new features for the system. This could include:
  * Implementing custom encryption algorithms for file protection.
  * Integrating advanced search and filtering options for files.
  * Adding version control for uploaded files.
  * Implementing notification systems for access requests/approvals.

## Screenshots
