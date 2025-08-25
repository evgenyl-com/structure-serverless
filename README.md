# Structure Serverless Example

This project demonstrates a serverless architecture using AWS SAM (Serverless Application Model) to deploy Lambda functions, API Gateway, and supporting resources. It is organized into multiple service folders, each with its own deployment scripts and configuration.

## Project Structure

```
cron/
  daily.py           # Scheduled tasks
  deploy.sh          # Deployment script
  Dockerfile         # Container image for Lambda
  requirements.txt   # Python dependencies
  template.yaml      # AWS SAM template
profile/
  user.py            # User profile Lambda handler
  deploy.sh          # Deployment script
  Dockerfile         # Container image for Lambda
  requirements.txt   # Python dependencies
  template.yaml      # AWS SAM template
shared/
  deploy.sh          # Deployment script for shared resources
  template.yaml      # AWS SAM template for shared resources
```

## Features
- **AWS Lambda** functions packaged as container images
- **API Gateway** with custom domain and Cognito authentication
- **DynamoDB** access policies
- **KMS** decryption permissions
- **Route53** DNS record management
- **CloudWatch Logs** for Lambda monitoring

## Deployment
Each service folder (`cron`, `profile`, `shared`) contains its own `deploy.sh` script and `template.yaml` for independent deployment. You can deploy using AWS SAM CLI:

```sh
cd profile
./deploy.sh
```

## Configuration
- Environment variables and resource references are managed via `template.yaml` files.
- Custom domain, SSL certificate, and DNS settings are configurable via parameters.
- Cognito authentication is enabled for API endpoints.

## Example API Endpoint
The `profile` service exposes a `/user` POST endpoint via API Gateway, secured with Cognito:

```
POST /user
Authorization: IdToken (Cognito)
```

## Prerequisites
- AWS CLI
- AWS SAM CLI
- Docker
- Python 3.8+

## Customization
- Update `requirements.txt` for Python dependencies.
- Modify `template.yaml` to adjust resources, policies, or environment variables.
- Extend Lambda handlers as needed for your business logic.

## License
MIT
