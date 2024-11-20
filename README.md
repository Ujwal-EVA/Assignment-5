ML Project CI/CD Pipeline
This project demonstrates a complete CI/CD pipeline for a machine learning project using a 3-layer Deep Neural Network (DNN) trained on the MNIST dataset. The pipeline is designed to automate training, validation, and deployment while ensuring code quality and reproducibility.

Features
Model Training: A 3-layer DNN with convolutional and fully connected layers.
Validation: Automated checks for:
Model parameter count (< 25,000).
Correct input shape (28x28 images).
Correct output size (10 classes).
Accuracy > 95% on the MNIST test set.
Deployment: Models are saved with a timestamp for tracking and future use.
CI/CD Integration: Includes a GitHub Actions workflow for automation.
Project Structure
bash
Copy code
ml_project/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions Workflow
│
├── data/
│   └── (Downloaded MNIST dataset will be saved here)
│
├── src/
│   ├── train.py            # Model training script
│   ├── validate.py         # Model validation and testing
│   └── deploy.py           # Deployment-related utilities
│
├── requirements.txt        # Required Python packages
└── README.md               # Project Documentation
How to Use
Prerequisites
Python 3.8 or later
pip package manager
Local Setup
Clone the repository:

bash
Copy code
git clone <your-repo-url>
cd ml_project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Train the model:

bash
Copy code
python src/train.py
Validate the model:

bash
Copy code
python src/validate.py
Running the CI/CD Pipeline Locally
Test the GitHub Actions workflow locally (optional):

Use a tool like act to simulate the workflow.
Push your changes to GitHub:

bash
Copy code
git add .
git commit -m "Add initial ML pipeline"
git push origin main
GitHub Actions will automatically run the CI/CD pipeline on every push or pull request.

CI/CD Pipeline
The pipeline automates the following steps:

Install Dependencies: Sets up the Python environment and installs required packages.
Train the Model: Executes src/train.py to train and save the model.
Validate the Model: Runs src/validate.py to ensure the model meets predefined criteria.
Model Details
Architecture:
Layer 1: Convolutional layer with 32 filters (3x3 kernel) and ReLU activation.
Layer 2: MaxPooling layer (2x2).
Layer 3: Fully connected layer with 128 units and ReLU activation.
Output Layer: Dense layer with 10 units (softmax activation).
Dataset: MNIST (28x28 grayscale images of digits 0-9).
Training: 1 epoch, batch size of 32.
Deployment
Models are saved in the models/ directory with a timestamp:
php
Copy code
mnist_model_<YYYYMMDD_HHMMSS>.h5
Deployment logic can be extended in src/deploy.py.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature/my-feature
Commit your changes:
bash
Copy code
git commit -m "Add feature"
Push to the branch:
bash
Copy code
git push origin feature/my-feature
Create a Pull Request.


Acknowledgments
TensorFlow for providing an excellent framework for machine learning.
GitHub Actions for enabling seamless CI/CD integration.
School of AI for teaching us this wonderful stuf!!!
