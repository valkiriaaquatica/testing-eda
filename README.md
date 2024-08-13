# EDA LoadBalancer Operator TESTING PUSPOSES NO PRODUCTION

This repository contains an operator developed for testing purposes. It is designed to manage the exposure of EDA (Event-Driven Ansible) services running in environments like K3s, mminikube, or kind, where pods are typically assigned `ClusterIP` addresses by default.

## Problem Statement

When running EDA on environments such as K3s, minikube, or kind, the pods are often assigned `ClusterIP` addresses. This limits the accesibility to the cluster itself, making it hard to expose these services to other machines on the network. Without proper exposure (e.g., through `port-forward` or `LoadBalancer` services), external systems cannot easily interact with these pods.

# The Image where is the Operator config
     ```bash
     docker pull fermendy/my-eda-worker-operatos:latest
     ```

## Solution

This operator automatically manages the exposure of specific EDA pods thanks to the ARP of MetalLB. The operator monitors the namespace `eda` (or the one indicated in the deployment file) and automatically changes the service type from `ClusterIP` to `LoadBalancer` for any newly created pod that matches the naming pattern `activation-job-*`. The operator ensures that these services are accessible on port 80 from other machines on the network. Additionally, when the associated pod or rulebook is deleted, the corresponding service is automatically removed.

### Key Features

- **Automatic Service Update:** Converts services of EDA pods named `activation-job-*` from `ClusterIP` to `LoadBalancer`.
- **Port Configuration:** The exposed port is automatically set to 80 for external access.
- **Auto Cleanup:** The service is deleted automatically when the corresponding pod is removed.

## Use Case

This operator is particularly useful when running EDA in a K3s cluster and needing to receive webhooks or interact with services from other machines on the network. It simplifies the network configuration by automatically exposing services as `LoadBalancer` without requiring manual intervention.

## Deployment

To deploy the operator in your cluster:

1. **Download the Deployment YAML:**
   - The deployment file is named `eda-lb-deployment.yml`.

2. **Apply the Deployment:**
   - Use the following command to deploy the operator:
     ```bash
     kubectl apply -f eda-lb-deployment.yml
     ```