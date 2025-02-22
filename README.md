# 🔍 Sign-Language-Detector

An application that utilizes the YOLOv model with customized output classes to detect various sign languages.

## 📖 Table of Contents
- [📊 Dataset](#-dataset)
- [⚙️ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🚀 Installation](#-installation)
- [🤝 Contributing](#-contributing)
- [📃 License](#-license)

## 📊 Dataset

This project is trained on a custom dataset of sign language gestures. The dataset was created by capturing and annotating images using [Roboflow](https://roboflow.com/).

The dataset includes six types of customized sign language gestures:
- **Hello**
- **Love**
- **No**
- **Special**
- **Thanks**
- **Yes**

## ⚙️ Features

- Real-time sign language detection using YOLOv
- Web-based interface for easy interaction

## 🛠️ Tech Stack  

This project is built using:

- **YOLOv**
- **OpenCV** 
- **Flask** 
- **Docker** 

## 🚀 Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository  

```bash
git clone https://github.com/PhamAnhTienn/Sign-Language-Detector.git
cd Sign-Language-Detector
```

### 2. Build and Start the Docker Containers
Ensure that [Docker](https://www.docker.com/) is installed, then execute:

```bash
docker-compose up --build
```

### 3. Access the Application
Once the setup is complete, access the web interface to test image or real-time detection:

```bash
http://localhost:8080/live
```

## 🤝 Contributing

This project is open to contributions. Please feel free to submit a PR.

## 📃 License

This project is provided under an MIT license. See the [LICENSE](LICENSE) file for details.