# Enviornment
FROM python:3.12-alpine

# Work Directory
WORKDIR /usr/local/app/PKI_Practice

# Copy content and expose a port
COPY . .
EXPOSE 8000

# Alphine Dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Install PyPi Package
RUN pip install --no-cache-dir PyPkiPractice

# Create the user
RUN useradd app
RUN chown -R app:app /usr/local/app
USER app

# Set the entry point and default command
ENTRYPOINT ["python", "-m", "run-pki-practice"]
CMD ["--default"]