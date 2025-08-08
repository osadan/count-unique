FROM python:3.11-slim

# Install uv (fast Python package installer)
RUN pip install uv

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy the app code
COPY unique_users_app.py .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "unique_users_app.py", "--server.address=0.0.0.0", "--server.port=8501"]
