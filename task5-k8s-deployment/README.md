# Task 5 - Kubernetes Deployment

## Objective
Deploy an NGINX application on Kubernetes using Minikube, expose it via NodePort, scale replicas, and verify in browser.

---

## Steps Performed

### 1. Create Deployment
```bash
kubectl create deployment my-app --image=nginx:latest
```

### 2. Expose Deployment as NodePort Service
```bash
kubectl expose deployment my-app --type=NodePort --port=80
```

### 3. Check Services
```bash
kubectl get svc
```

### 4. Access Application via Minikube
```bash
minikube service my-app
```

### 5. Scale Deployment
```bash
kubectl scale deployment my-app --replicas=3
```

### 6. Verify Deployment Details
```bash
kubectl describe deployment my-app
```

---

## Proof of Work (Screenshots)
- **pods.png** → Output of `kubectl get pods`
- **services.png** → Output of `kubectl get svc`
- **deployment-describe.png** → Output of `kubectl describe deployment my-app`
- **browser.png** → Application running in browser
