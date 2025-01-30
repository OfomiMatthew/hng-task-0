# HNGx Stage One Task API

This backend API was developed for HNG Stage 0. It features an endpoint that returns the developer's email, the current date and time, and a GitHub repository link. The API is hosted on vercel.  
**Live API Endpoint**: [Live API Endpoint](https://hng-task-0-zeta.vercel.app/api/profiles)

## Features
- Returns the user's registered Slack email.
- Provides the current datetime in ISO 8601 format.
- Includes the GitHub URL of the project's codebase.

## Technologies Used
- **Python** (3.11+)
- **Django** (5.1+)
- **Django REST Framework** (3.15+)
- **django-cors-headers** (for CORS handling)

---

## Setup and Installation

### Prerequisites
- Python 3.11+
- pip

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/OfomiMatthew/hng-task-0.git
   cd hng-task-0

## Api Documentation
- GET api/profiles
- **Description:** returns developer email address, current datetime and github repo link
- **Response format:**
     ```json
     {
    "email": "ofomimatthew7@gmail.com",
    "current_datetime": "2025-01-30T14:03:58Z",
    "github_url": "<https://github.com/OfomiMatthew/hng-task-0>"
      }

### Example usage:
   - curl -X GET https://hng-task-0-zeta.vercel.app/api/profiles


