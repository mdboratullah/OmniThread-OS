echo "Building OmniThread OS Enterprise Docker Image..."
docker build -t omnithread-os:latest .

echo "Running OmniThread OS Enterprise Container on Port 8080..."
docker run -d -p 8080:8080 --name omnithread_instance omnithread-os:latest

echo "Deployment Successful! Access your dashboard at http://localhost:8080"
