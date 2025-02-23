# Online Exam Proctoring System

## Prerequisites

Before setting up this project, ensure you have the following installed:

- **Python**: Version 3.11.4
- **pip**: Version 25.0.1
- **CMake** (may be required for some dependencies)
- **Visual Studio C++ Build Tools** (may be required for compiling certain packages)

## Virtual Environment Setup

To create and activate a virtual environment, use the following commands:

### **For Windows:**

```sh
python -m venv venv
venv\Scripts\activate
```

### **For macOS/Linux:**

```sh
python -m venv venv
source venv/bin/activate
```

## Installing Dependencies

Once the virtual environment is activated, install the required libraries using:

```sh
pip install -r requirements.txt
```

If `pip install` does not work, try:

```sh
pip install --user -r requirements.txt
```

## Running the Server

To start the server, run:

```sh
python server.py
```

Once the server is running, open your web browser and go to:

```
http://localhost:5000
```

## Database Configuration

To configure the database, locate the following file:

```
/backend/db_helper.py
```

Edit the `user` and `password` fields if necessary (the default user may not need to be changed).

### **Creating the Users Table**

Run the following SQL query to create the `sign_up` table for storing user details:

```sql
DROP TABLE IF EXISTS `sign_up`;
CREATE TABLE `sign_up` (
  `email` varchar(45) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Additional Notes

- If you encounter any installation issues, ensure you have **CMake** and **Visual Studio C++ Build Tools** installed.
- Always activate the virtual environment before running the server or installing dependencies.

---

### Happy Coding! 🚀

