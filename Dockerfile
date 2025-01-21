# Enviornment
FROM python:3.12-alpine

# Work Directory
WORKDIR /usr/local/app/
RUN mkdir -p /usr/local/app/output

# Copy content and expose a port
COPY . .
EXPOSE 5000

# Alpine Dependencies
RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev libffi-dev

# Install PyPi Package
RUN pip install --no-cache-dir .

# Create the user
RUN adduser -D -g '' app
RUN chown -R app:app /usr/local/app
USER app

# Set the entry point and default command
ENTRYPOINT ["run-pki-practice"]
CMD ["--default"]
