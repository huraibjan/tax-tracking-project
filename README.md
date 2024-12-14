# Tax Tracking System

## Overview
The Tax Tracking System is a web-based application designed to help users manage tax records efficiently. It allows users to add, view, edit, and delete records, as well as calculate taxes based on total amounts and specified tax rates. Built with HTML, TailwindCSS, and JavaScript, this project interacts with a backend API for data storage and retrieval.

---

## Features
- **Add Tax Records:** Create new records with fields for company name, amount, payment date, status, and due date.
- **View Records:** Display tax records in a table with filtering options by due date.
- **Edit/Delete Records:** Update or remove records with ease.
- **Calculate Tax:** Compute tax dues automatically based on user-defined tax rates.
- **Dynamic Filtering:** Filter records by specific due dates or view all records at once.

---

## Project Workflow

### 1. Adding Records
Users can add new tax records by completing a form with the following details:
- **Company Name**
- **Amount**
- **Payment Date**
- **Status** (Paid/Unpaid)
- **Due Date** (Dropdown menu)

### 2. Viewing Records
Tax records are displayed in a responsive table that:
- Displays details like company name, amount, payment date, status, and due date.
- Provides filtering by specific due dates or an "All Records" option.
- Shows a message when no records are available.

### 3. Editing Records
Clicking the edit icon opens a modal where users can:
- Update record details, including the company name, amount, payment date, status, and due date.
- Save changes directly from the modal.

### 4. Deleting Records
Users can delete records by clicking the delete icon, triggering a confirmation modal.

### 5. Tax Calculation
Users can:
- Specify a tax rate.
- Automatically compute tax dues based on the total amount of all records.
- View the calculated tax dues in the summary section.

---

## Installation and Setup

### Prerequisites
- **Node.js** (Optional: If the backend server needs to be run locally).
- A backend API available at `http://127.0.0.1:5000/records`.
- A modern web browser (e.g., Chrome, Edge).

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/huraibjan/tax-tracking-project.git
   cd tax-tracking-project
   ```

2. **Ensure Backend API is Running**
   The application interacts with the backend API hosted at `http://127.0.0.1:5000/records`. Make sure the backend server is operational.

3. **Open the Project**
   Open the `index.html` file in any modern web browser.

4. **Start Using the Application**
   - Add, view, edit, or delete tax records.
   - Calculate taxes based on the total amounts and input tax rates.

---

## Folder Structure
```
project-directory/
├── index.html        # Main HTML file
├── README.md         # Project documentation
├── styles/           # Optional folder for custom CSS
├── scripts/          # Optional folder for custom JS
└── assets/           # Optional folder for images and other assets
```

---

## API Endpoints
Ensure the following API endpoints are functional for the project:

### 1. **Get All Records**
- **Endpoint:** `GET /records`
- **Description:** Fetches all tax records.
- **Response Example:**
  ```json
  [
    {
      "id": 1,
      "company": "Example Co",
      "amount": 1000,
      "payment_date": "2023-09-15",
      "status": "paid",
      "due_date": "2023-10-15"
    }
  ]
  ```

### 2. **Add a Record**
- **Endpoint:** `POST /records`
- **Description:** Adds a new tax record.
- **Request Body Example:**
  ```json
  {
    "company": "Example Co",
    "amount": 1000,
    "payment_date": "2023-09-15",
    "status": "paid",
    "due_date": "2023-10-15"
  }
  ```

### 3. **Update a Record**
- **Endpoint:** `PUT /records/{id}`
- **Description:** Updates an existing tax record.
- **Request Body Example:**
  ```json
  {
    "company": "Updated Co",
    "amount": 2000,
    "payment_date": "2023-09-16",
    "status": "unpaid",
    "due_date": "2023-11-15"
  }
  ```

### 4. **Delete a Record**
- **Endpoint:** `DELETE /records/{id}`
- **Description:** Deletes a tax record by its ID.

---

## Technologies Used

### Frontend:
- **HTML**
- **TailwindCSS**
- **JavaScript**

### Backend (API):
- **Framework:** Flask (or similar frameworks if applicable).
- **Database:** MySQL or SQLite (Optional).

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a clear description of your changes.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
Special thanks to all contributors and resources that supported the development of this project!

