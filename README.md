# 🏥 Hospital Management System - Backend

A complete Django-based hospital management backend system with REST API.

## ✨ Features

### Core Modules
- ✅ **Patient Management** - Register and manage patient records
- ✅ **Doctor Management** - Manage doctors with specializations
- ✅ **Appointment System** - Schedule and track appointments
- ✅ **Medical Records** - Complete patient medical history
- ✅ **Prescriptions** - Manage medications and dosages
- ✅ **Lab Tests** - Order and track lab tests
- ✅ **Billing & Invoices** - Generate bills and track payments

### Dashboard Features
- 📊 Real-time statistics and analytics
- 📈 Interactive charts (appointments, doctors by specialization)
- 📋 Recent appointments table
- 🔍 Search and filter functionality
- 👤 User authentication and profiles

### REST API
- 🔌 Complete RESTful API
- 📖 API documentation included
- 🔍 Search and filter endpoints
- 📊 Analytics endpoints

## 🚀 Quick Start

### 1. Clone and Setup
```bash
cd hospital_system
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Superuser
```bash
python manage.py createsuperuser
```

### 4. Populate Sample Data (Optional)
```bash
python manage.py populate_data
```

### 5. Run Server
```bash
python manage.py runserver
```

### 6. Access the System

- **Dashboard**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Docs**: http://127.0.0.1:8000/api-docs/

## 📚 API Endpoints

### Patients
- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create patient
- `GET /api/patients/{id}/` - Get patient details
- `GET /api/patients/search/?q={query}` - Search patients

### Doctors
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/available/` - Available doctors only
- `GET /api/doctors/by_specialization/?specialization={spec}` - Filter by specialization

### Appointments
- `GET /api/appointments/` - List all appointments
- `GET /api/appointments/today/` - Today's appointments
- `GET /api/appointments/upcoming/` - Upcoming appointments
- `GET /api/appointments/by_date_range/?start_date={date}&end_date={date}` - Filter by date

### Medical Records
- `GET /api/medical/records/` - All medical records
- `GET /api/medical/records/by_patient/?patient_id={id}` - Patient records

### More Endpoints
See `/api-docs/` for complete documentation

## 🛠 Tech Stack

- **Backend**: Django 5.2
- **API**: Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django Auth + Session
- **Charts**: Chart.js

## 📁 Project Structure
```
hospital_system/
├── patients/           # Patient management
├── doctors/            # Doctor management
├── appointments/       # Appointment scheduling
├── medical_records/    # Medical records, prescriptions, lab tests, invoices
├── accounts/           # User authentication
├── dashboard/          # Main dashboard and views
├── hospital_system/    # Project settings
├── manage.py
├── requirements.txt
└── README.md
```

## 🔐 Security Features

- ✅ User authentication required
- ✅ CORS configuration for frontend
- ✅ CSRF protection
- ✅ Environment variables for sensitive data
- ✅ Production-ready security settings

## 📊 Database Models

### Patient
- Full name, DOB, gender
- Contact information
- Medical ID
- Address

### Doctor
- Full name, specialization
- Contact information
- Availability status

### Appointment
- Patient & Doctor references
- Date, time, status
- Notes

### Medical Record
- Patient diagnosis
- Symptoms, treatment
- Doctor notes

### Prescription
- Medication details
- Dosage, frequency
- Instructions

### Lab Test
- Test name, type
- Status tracking
- Results

### Invoice
- Amount, payment status
- Due dates
- Payment tracking

## 🌐 Frontend Integration

Your frontend can connect to this backend using the REST API endpoints.

Example (JavaScript):
```javascript
// Get all patients
fetch('http://127.0.0.1:8000/api/patients/')
  .then(response => response.json())
  .then(data => console.log(data));

// Search patients
fetch('http://127.0.0.1:8000/api/patients/search/?q=John')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 📝 License

This project is built for educational purposes.

## 👨‍💻 Author

Hospital Management System Backend