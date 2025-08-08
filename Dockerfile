FROM python:3.11-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev
RUN pip install uv
WORKDIR /app
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY streamlit_app.py .
COPY pages ./pages
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]
