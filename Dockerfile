# Use official Python image
FROM python:3.10

# Set work directory
WORKDIR /portfolio_website_server

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run the Django app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_website_server.wsgi:application"]
