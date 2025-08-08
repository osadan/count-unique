# Stage 1: Install dependencies using uv
FROM python:3.11-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev
RUN pip install uv
WORKDIR /app
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Stage 2: Final slim image
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY unique_users_app.py .
EXPOSE 8080
ENV PORT=8080
CMD streamlit run unique_users_app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false
