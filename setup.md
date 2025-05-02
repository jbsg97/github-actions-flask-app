# Build docker image
docker build -t flask-api .

# Run in port 5000
docker run -p 5000:5000 flask-api