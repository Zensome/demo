# Demo app

Simple full stack app which takes user input data and encrypts with downloadable file.

**Backend (Python/FastAPI)**

- Accepts and validates user data
- Encrypts data using AES encryption
- Generates .txt file

**Frontend (React)**

- Form with name, email, and password fields
- Client-side validation
- File download

## Deployment

- GitHub Actions
- Google Cloud Run

## API

- `POST /api/account` - Submit account data
- `GET /api/download/{filename}` - Download encrypted file

## Live Demo

- Frontend: https://frontend-service-iwduz3ezya-uc.a.run.app
- Backend: https://backend-service-iwduz3ezya-uc.a.run.app
