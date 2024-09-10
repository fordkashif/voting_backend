
# Vote App - Flask Backend

This is the Flask backend of the Vote App, which processes the votes sent from the React frontend.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Local Setup](#local-setup)
- [Environment Variables](#environment-variables)
- [Running Locally](#running-locally)
- [Deploying to DigitalOcean](#deploying-to-digitalocean)
- [License](#license)

## Technologies Used
- **Flask** (Python)
- **Flask-CORS**
- **python-dotenv**

## Local Setup

### Prerequisites
Make sure you have the following installed:
- **Python 3.x** and **pip**

### Steps

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yourusername/vote-app-backend.git
   cd vote-app-backend
   \`\`\`

2. **Create a virtual environment** (optional but recommended):
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Create a \`.env\` file** in the root directory to store environment variables:
   \`\`\`bash
   FLASK_SECRET_KEY=supersecretkey
   FLASK_APP_URL=http://127.0.0.1:5000
   \`\`\`

## Environment Variables

| Variable            | Description                              | Example                    |
|---------------------|------------------------------------------|----------------------------|
| \`FLASK_SECRET_KEY\`   | Secret key for Flask app security        | \`supersecretkey\`            |
| \`FLASK_APP_URL\`      | URL where the Flask app is hosted        | \`http://127.0.0.1:5000\`     |

## Running Locally

### Start the Flask Server

1. After installing the dependencies, run:
   \`\`\`bash
   flask run
   \`\`\`

2. The Flask app will be available at \`http://127.0.0.1:5000\`.

## Deploying to DigitalOcean

1. **Push your Flask project to GitHub**.
2. **Deploy using DigitalOcean App Platform**:
   - Create a new app in DigitalOcean.
   - Select **Python** for the backend.
   - Add the environment variables like \`FLASK_SECRET_KEY\` and \`FLASK_APP_URL\`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
