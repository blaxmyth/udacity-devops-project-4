#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
dockerpath=blaxmyth/udacity

# Step 2
# Run the Docker Hub container with kubernetes
# kubectl run udacityproject --image=$dockerpath --port=80

kubectl create deployment udacityproject --image=$dockerpath


# kubectl patch nodes minikube --patch '{"spec":{"unschedulable": false}}'

# Step 3:
# List kubernetes pods
kubectl get pods

sleep 5

# Step 4:
# Forward the container port to a host
kubectl port-forward deployment/udacityproject 8080:80

