<<<<<<< HEAD
# secure-file-storage
The Secure File Sharing System is a web-based application designed to provide users with a secure and user-friendly platform for managing their personal files online.
## License
MIT License
## Getting Started
The Secure File Sharing System is a web-based application designed to provide users with a secure and user-friendly platform for managing their personal files online. Developed using Python(Django) for the backend, MySQL for data storage, and a responsive frontend built with HTML, CSS, and Bootstrap, the system focuses on key aspects such as data security, user authentication, and efficient file management.
Users can create personal accounts through a simple registration process, enabling them to upload, view, download, and delete their own files within a protected server environment. Each uploaded file is accompanied by metadata—such as filename, file type, and upload timestamp—ensuring traceability and organization.
An important feature of the system is file access control between users. By default, a user can only view and manage their own uploaded files. However, if one user wishes to access a file uploaded by another, they must send a file access request. The original uploader receives this request and can choose to approve or reject it. Only upon approval will the requesting user be granted access to view or download the file. This mechanism adds an extra layer of security and ensures that file sharing remains fully controlled by the file owner.
The application also includes an admin panel that allows administrators to monitor user activity and manage registered accounts, providing necessary oversight in a multi-user environment.
Overall, this project aims to strike a balance between simplicity, user control, and strong security, offering a practical solution for secure file sharing and management in both personal and collaborative settings.
