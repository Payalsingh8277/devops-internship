# Task 3: Terraform Docker Setup 

This project provisions an **NGINX** container using **Terraform** and **Docker**.

## Files Included

- `main.tf` – Terraform configuration
- `.gitignore` – Ignores state and cache files
- `README.md` – You're reading it 

## Requirements

- Terraform v1.12+
- Docker (installed and running)

##  Steps to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/YOUR_USERNAME/task3-terraform-docker.git
cd task3-terraform-docker

# Step 2: Initialize Terraform
terraform init

# Step 3: Show execution plan
terraform plan

# Step 4: Apply configuration
terraform apply

# Step 5: Visit in browser
http://localhost:8080

# Step 6: Destroy when done
terraform destroy
```

## Output

- Docker pulls `nginx:latest`
- Container runs on port `8080`
- Check with: `docker ps`
