# Consuming REST Application

This project is a simple Flask application designed to consume RESTful services from the Quoters API and log the fetched quotes. It demonstrates the integration of Flask with Docker and Kubernetes for development and deployment.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.9+
- pip
- Docker
- Kubernetes (Minikube, Docker Desktop, or any Kubernetes cluster)

## Setup and Local Development

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```
git clone https://github.com/yourusername/ConsumingRest.git
cd ConsumingRest
```

### 2. Run the Virtual Environment
```
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run it locally-
```
flask run
```

### 5. Run Quotes-
```
kubectl run quoters --image=javajon/quoters:1.0.0 --port=8080
kubectl expose pod quoters --name=quoters
kubectl get all -l run=quoters
kubectl port-forward service/quoters 8080:8080
```


### The Flask application will start running on http://localhost:5000. You can access the application and make API calls to fetch quotes.

## Containerization with Docker

Build the Docker image using the following command:
```
docker build -t consumingrest .
```

Run your Docker container locally:
```
docker run -p 5000:5000 consumingrest
```

Now, the application should be accessible at http://localhost:5000.


## Deployment to Kubernetes

Build the Docker image:

```
docker build -t yourusername/consumingrest .
```

Log into Docker Hub:
```
docker login
```

Push the image to your Docker Hub repository:
```
docker push yourusername/consumingrest
```

Create a Kubernetes deployment:
```
kubectl create deployment consumingrest --image=yourusername/consumingrest
```

Expose your deployment
```
kubectl expose deployment consumingrest --type=NodePort --port=5000
```

Get the list of pods and find the pod ID for your deployed application:
```
kubectl get pods
```

Now, make curl commands to the Flask app at localhost:5000:
```
curl http://localhost:5000/fetch-random-quote
curl http://localhost:5000/fetch-quote/1
curl http://localhost:5000/fetch-quote/2
curl http://localhost:5000/fetch-quote/3
```


Check the logs of the pod to verify the connection and see the logs with the quotes:
```
kubectl logs <pod-name>
```

## License

This project is open-source.


