# Dokonchi_bola 🚀

A FastAPI-based backend application for Dokonchi_bola.

## Overview

Dokonchi_bola is a modern web backend built with FastAPI, providing a RESTful API for managing Dokonchi_bola operations.

## Features

- 🚀 Built with FastAPI
- 📚 Interactive API documentation (Swagger UI)
- ⚡ High-performance async support
- 🔄 RESTful endpoints

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rahmonovisroiljon78-beep/Dokonchi_bola.git
cd Dokonchi_bola
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### GET /
Returns a welcome message indicating the backend is running.

**Response:**
```json
{
  "message": "Dokonchi_bola backend ishlayapti 🚀"
}
```

## Project Structure

```
Dokonchi_bola/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source.

## Support

For issues or questions, please open an issue on GitHub.
