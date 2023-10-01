# Task Manager

Task Manager is a web application built using Django that allows users to efficiently manage their tasks, track priorities, and monitor completion status. This README file provides an overview of the project, instructions for setting up the environment, documentation for API endpoints, and other important details.

## Features

- User Registration and Authentication: Users can create accounts, log in, and log out to access the task management features.
- Task Management: Create, edit, and delete tasks with information such as title, description, due date, priority, and completion status.
- Task Prioritization: Categorize tasks into low, medium, or high priority for better organization.
- Multiple Image Upload: Attach multiple images to tasks for reference or additional information.
- Task Listing: Retrieve a list of tasks, filter by priority or completion status, and search by title.
- API Integration: Expose a RESTful API for accessing and managing tasks programmatically.

## Getting Started

To set up and run the Task Manager project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables: Create a `.env` file and set up necessary settings.
4. Migrate the database: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`

For detailed setup instructions, refer to the [Installation Guide](#installation-guide) section below.

## Installation Guide

1. **Clone the Repository**

   ```bash
   git clone <repository-url>

   git clone <repository-url>
   pip install -r requirements.txt
   SECRET_KEY=28f1dbba4b085971ba2c50d41a57c0e7f02b1fa9708dab7f
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   python manage.py migrate
   python manage.py runserver
   
API Documentation

GET /api/tasks/: Retrieve a list of tasks.
POST /api/tasks/: Create a new task.
GET /api/tasks/<task_id>/: Retrieve details of a specific task.
PUT /api/tasks/<task_id>/: Update a task.
DELETE /api/tasks/<task_id>/: Delete a task.

json
[
  {
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "due_date": "2023-09-30",
    "priority": "high",
    "completed": false
  },
  // More tasks...
]






