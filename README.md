# Count Unique - Unique Users Calculator

A Streamlit web application for calculating unique users with saturation modeling.

## Features

- Calculate concurrent users based on RPS and requests per user
- Model unique user accumulation over time with saturation effects
- Interactive visualization of user growth curves
- Hebrew interface with intuitive controls

## Local Development

### Prerequisites
- Python 3.11+
- Docker (optional)

### Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run unique_users_app.py
```

The app will be available at `http://localhost:8501`

### Using Docker

```bash
docker build -t count-unique .
docker run -p 8080:8080 count-unique
```

## Deployment to Google Cloud Run

This project includes automated deployment to Google Cloud Run via GitHub Actions.

### Setup Required Secrets

In your GitHub repository settings, add these secrets:

1. **GCP_PROJECT_ID**: Your Google Cloud Project ID
2. **GCP_SA_KEY**: Service Account JSON key with the following permissions:
   - Cloud Run Admin
   - Storage Admin
   - Container Registry Service Agent

### Creating the Service Account

```bash
# Create service account
gcloud iam service-accounts create count-unique-deployer \
    --description="Service account for deploying count-unique to Cloud Run" \
    --display-name="Count Unique Deployer"

# Grant necessary permissions
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:count-unique-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:count-unique-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:count-unique-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

# Create and download key
gcloud iam service-accounts keys create key.json \
    --iam-account=count-unique-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

Add the contents of `key.json` as the `GCP_SA_KEY` secret in GitHub.

### Deployment

Push to the `main` branch to trigger automatic deployment to Cloud Run.

## Configuration

The application uses the following default parameters:
- RPS: 3000 requests per second
- Requests per user: 10 per second
- Session length: 60 seconds
- Time range: 10 minutes
- Saturation ratio: 0.2

All parameters can be adjusted through the web interface.

## License

MIT License