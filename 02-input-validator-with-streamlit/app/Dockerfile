# Step 1: Choose a base image
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the project files to the container
COPY . /app

# Step 4: Install dependencies
RUN pip install -r requirements.txt

# Step 5: Define the command to run your application
CMD ["streamlit", "run", "main.py"]

