# ☁️ Cloud Resume Challenge (Terraform + AWS)

This project is my implementation of the **Cloud Resume Challenge**, deployed entirely on AWS and automated with Terraform.

## 🔹 Features
- Resume hosted on **S3** + **CloudFront** (global CDN, HTTPS enforced).
- Serverless **visitor counter API** → API Gateway → Lambda → DynamoDB.
- Automated infrastructure with **Terraform** (modular, reproducible).
- **Budget alarm** to prevent unexpected AWS charges.
- **CORS + IAM least privilege** for secure access.

## 🏗️ Architecture
![diagram](diagrams/architecture.png)

**Flow:**  
User → CloudFront → S3 (resume site)  
    ↓  
API Gateway → Lambda → DynamoDB (visitor count)

## 🚀 How to Deploy
```bash
cd terraform
terraform init
terraform plan
terraform apply

