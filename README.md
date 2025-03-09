# Portfolio Dungeon

This is the backend code of my web-app project built with [FastAPI](https://github.com/fastapi/fastapi).

## Installation

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- pip3 (Python package manager)

### Steps to Install
```bash
## 1. Clone the repository:
git clone https://github.com/mrkdeng/portfolio-dungeon-backend
## 2. Navigate into the project directory: 
cd portfolio-dungeon-backend
## 3. Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate
## 4. Install dependencies:
pip install -r requirements.txt
```

## Usage

### Run the Application

To run the application, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
