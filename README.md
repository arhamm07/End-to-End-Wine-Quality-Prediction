# 🍷 Wine Quality Prediction

An end-to-end machine learning project that predicts wine quality based on various chemical properties. This project includes a Flask-based web interface, a complete ML pipeline, and CI/CD integration.

## 🚀 Features

- **Web Interface**: User-friendly interface to input wine characteristics
- **Machine Learning Model**: Predicts wine quality (0-10 scale)
- **REST API**: Built with Flask for easy integration
- **Containerized**: Ready for Docker deployment
- **CI/CD Pipeline**: Automated testing and deployment
- **Modular Code**: Well-structured Python package

## 🛠️ Tech Stack

- **Backend**: Python 3.10, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Version Control**: Git

## 📦 Dependencies

- Python 3.10+
- Dependencies listed in `requirements.txt`
  ```
  pandas
  scikit-learn
  numpy
  Flask
  python-box
  pyYAML
  tqdm
  joblib
  ```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerization)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/End-to-End-Wine-Quality-Prediction.git
   cd End-to-End-Wine-Qrediction
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Run the Flask development server**
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:8080`

2. **Using Docker**
   ```bash
   docker build -t wine-quality-prediction .
   docker run -p 8080:8080 wine-quality-prediction
   ```

## 🧪 Training the Model

To train the model:
1. Access the training endpoint:
   ```
   http://localhost:8080/train
   ```
   Or run directly:
   ```bash
   python main.py
   ```

## 🌐 API Endpoints

- `GET /` - Home page with input form
- `POST /predict` - Get wine quality prediction
- `GET /train` - Train the model

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/         # CI/CD workflows
├── config/               # Configuration files
├── data/                 # Dataset storage
├── logs/                 # Log files
├── src/                  # Source code
│   └── WineQuality/      # Main package
│       └── pipeline/     # ML pipeline components
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── .gitignore
├── app.py               # Flask application
├── Dockerfile           # Docker configuration
├── main.py              # Training script
├── params.yaml          # Model parameters
├── README.md
├── requirements.txt     # Python dependencies
└── setup.py            # Package setup
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
