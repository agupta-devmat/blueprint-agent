# blueprint-agent

A FastAPI application powered by pydantic-ai that implements an AI-powered roulette game agent. The agent uses OpenAI's GPT-4o model to interact with users and determine if their roulette number bets are winners.

## Features

- AI-powered roulette game using pydantic-ai
- RESTful API built with FastAPI
- OpenAI GPT-4o integration
- AWS App Runner deployment ready
- Docker containerization support

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- OpenAI API key
- AWS CLI (for deployment)
- Docker (for containerization)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd blueprint-agent
```

2. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install dependencies:
```bash
uv sync
```

4. Set up environment variables:
```bash
# office.com/apps -> AWS (Dev) -> Access Keys
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SESSION_TOKEN=""
```

## Running the Application

Start the development server:
```bash
# Development with auto-reload
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Or use the Makefile command
make run
```

The API will be available at:
- **Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Development Commands

The project includes a Makefile with useful commands:

```bash
# Install dependencies
make install

# Install development dependencies
make install-dev

# Run development server with auto-reload
make run

# Run production server
make run-prod

# Add a new package
make add PACKAGE=package-name

# Add a development package
make add-dev PACKAGE=package-name

# Build Docker image
make build

# Create ECR repository
make create-ecr

# Login to ECR
make ecr-login

# Build and push to ECR
make push

# Deploy to AWS
make deploy-to-aws
```

## AWS Deployment

This project is configured for deployment on AWS App Runner using SAM (Serverless Application Model).

### Configuration

The deployment is configured with:
- **Service Name**: blueagent
- **Region**: eu-central-1
- **Instance**: 1 vCPU, 2048 MB memory
- **Port**: 80 (containerized)
- **Auto-scaling**: 1-1 instances, max 100 concurrent requests

### Deploy to AWS

1. Configure AWS CLI with your credentials
2. Update the Makefile variables if needed:
   - `ACCOUNT_ID`: Your AWS account ID
   - `REGION`: Your preferred AWS region
   - `SUBNET_ID`: Your VPC subnet ID

3. Deploy:
```bash
make create-ecr
make push
make deploy-to-aws
```

## Project Structure

```
blueprint-agent/
├── src/
│   ├── main.py              # FastAPI application with pydantic-ai agent
│   └── __pycache__/         # Python cache files
├── aws-sam/                 # AWS SAM related files
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
├── template.yaml           # SAM template for AWS deployment
├── Makefile                # Development and deployment commands
├── Dockerfile              # Docker configuration
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## API Usage

The application exposes a pydantic-ai agent as an API. You can interact with the roulette agent by sending requests to the API endpoints.

### Example Usage

The roulette agent allows users to:
1. Provide a roulette number (0-36)
2. The agent uses the `roulette_wheel` tool to generate a random winning number
3. Returns whether the user's number is a winner or loser

## Dependencies

Key dependencies include:
- **FastAPI**: Web framework
- **pydantic-ai**: AI agent framework
- **OpenAI**: AI model provider
- **uvicorn**: ASGI server
- **boto3**: AWS SDK
- **anthropic**: Alternative AI provider
- **cohere**: Alternative AI provider

See `pyproject.toml` for the complete list of dependencies.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if applicable)
5. Submit a pull request

## License

[Add your license information here]
