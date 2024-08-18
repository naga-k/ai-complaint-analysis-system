# Full-Stack Application Instructions

This document provides instructions on how to set up, start, and access the full-stack application consisting of a Next.js client and a Flask server.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/kaushik-manivannan/ai-complaint-analysis-system
   cd ai-complaint-analysis-system
   ```

2. Set up environment variables:

   For the client:

   - Navigate to the `client` directory
   - Create a `.env.local` file with the following content:
     ```
     NEXT_PUBLIC_API_URL=http://localhost:4000
     ```

   For the server:

   - Navigate to the `server` directory
   - Create a `.env` file with the following content:
     ```
     POSTGRES_USER=ruby-team
     POSTGRES_PASSWORD=123
     POSTGRES_DB=complaint_system
     POSTGRES_PORT=5432
     POSTGRES_HOST=postgres
     ```

3. Build and start the application:
   - From the project root directory, run:
     ```
     docker compose up --build
     ```
   - This command will build the Docker images for both the client and server, and start the containers.

## Accessing the Application

Once the application is running:

1. Access the Next.js client:

   - Open a web browser and navigate to `http://localhost:3000`
   - You should see the client application running

2. Access the Flask server:
   - The server API is available at `http://localhost:4000`
   - You can test it by navigating to `http://localhost:4000` in your browser or using a tool like curl or Postman

## Development Workflow

- The application is set up with volume mounts, allowing you to make changes to the code and see them reflected immediately without rebuilding the containers.
- If you make changes to the Dockerfile or add new dependencies, you'll need to rebuild the containers:
  ```
  docker compose up --build
  ```

## Stopping the Application

To stop the application:

- If running in the foreground, use `Ctrl+C` or for Mac users `Cmd + C`
- If running in the background, use:
  ```
  docker compose down
  ```

## Troubleshooting

- If you encounter any issues with dependencies or builds, try removing the existing containers and volumes:

  ```
  docker compose down -v
  ```

  Then, rebuild the application:

  ```
  docker compose up --build
  ```

- Check the Docker logs for any error messages:
  ```
  docker compose logs
  ```

## Additional Notes

- For DB connection to a local GUI, just use the DB values in .env file.
- Everytime you install a new python library/package, close the docker container and do a `docker compose up --build` to always get the latest build.
- The client is configured to proxy API requests to the server. Ensure that the `NEXT_PUBLIC_API_URL` in the client's `.env.local` file matches the server's URL.
- For production deployment, remember to update the environment variables and configurations accordingly.
