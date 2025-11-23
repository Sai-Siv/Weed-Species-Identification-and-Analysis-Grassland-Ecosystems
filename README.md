# Weed Species Identification and Analysis for Grassland Ecosystems

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)

## 📋 Overview

This project implements a deep learning-based system for automated identification and classification of weed species in grassland ecosystems. The system uses computer vision and neural networks to analyze plant images and predict their species, enabling efficient ecosystem monitoring and management.

**Weed Species Covered:**
- Celosia Argentea L.
- Crowfoot Grass
- Purple Chloris

## 🏗️ Project Structure

```
.
├── dataset/                       # Dataset directory
│   ├── train/                     # Training dataset organized by species
│   └── val/                       # Validation dataset organized by species
├── notebooks/
│   └── main_dl.ipynb              # Jupyter notebook for experiments and analysis
├── scripts/                       # Utility and standalone scripts
│   ├── opencv-test.py             # OpenCV testing and validation
│   ├── Rename.py                  # Batch file renaming utility
│   ├── resize.py                  # Image resizing utility
│   └── train-test-split.py        # Data splitting utility
├── src/                           # Core source code package
│   ├── __init__.py                # Package initialization
│   ├── data.py                    # Data loading and processing functions
│   └── predict.py                 # Model prediction and inference
├── models/                        # Pre-trained models and checkpoints
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip or conda package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sai-Siv/Weed-Species-Identification-and-Analysis-Grassland-Ecosystems.git
   cd Weed-Species-Identification-and-Analysis-Grassland-Ecosystems
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Data Organization

### Dataset Directory Structure

```
dataset/
├── train/
│   ├── CELOSIA_ARGENTEA_L/
│   ├── CROWFOOT_GRASS/
│   └── PURPLE_CHLORIS/
└── val/
    ├── CELOSIA_ARGENTEA_L/
    ├── CROWFOOT_GRASS/
    └── PURPLE_CHLORIS/
```

### Data Preparation

To prepare your dataset, use the provided utilities:

```bash
# Rename images for consistency
python scripts/Rename.py

# Resize images to standard dimensions
python scripts/resize.py

# Split data into training and validation sets
python scripts/train-test-split.py
```

## 📝 Usage

### 1. Data Exploration & Training (Jupyter Notebook)

Start with the main notebook for data exploration and model training:

```bash
jupyter notebook notebooks/main_dl.ipynb
```

### 2. Using the Core Modules

```python
from src import data, predict

# Load data
train_data = data.load_training_data('data/processed/train')

# Make predictions
predictions = predict.classify_image('path/to/image.jpg')
print(predictions)
```

### 3. Running Utilities

```bash
# Test OpenCV functionality
python scripts/opencv-test.py

# Process images
python scripts/resize.py

# Organize data
python scripts/Rename.py
python scripts/train-test-split.py
```

## 🧠 Model

The project uses deep learning models for image classification:

- **Model Architecture**: Convolutional Neural Networks (CNN)
- **Framework**: TensorFlow/PyTorch (as configured)
- **Input**: Plant images (RGB)
- **Output**: Species classification with confidence scores

### Model Files

Trained models are stored in the `models/` directory:
- `model_checkpoint.h5` or `.pth` - Model weights
- `model_config.json` - Model architecture configuration

## 📈 Results

The model achieves high accuracy on the weed species classification task:

| Species | Accuracy |
|---------|----------|
| Celosia Argentea L. | XX% |
| Crowfoot Grass | XX% |
| Purple Chloris | XX% |
| **Overall** | **XX%** |

*Note: Update with your actual results after training*

## 🔧 Development

### Adding New Features

When adding new functionality:

1. Create modules in `src/` for core logic
2. Use `scripts/` for utility scripts
3. Test in `notebooks/main_dl.ipynb`
4. Update documentation

### Running Tests

```bash
# Run unit tests (if available)
python -m pytest tests/
```

## 📚 Dependencies

Core dependencies include:

- **OpenCV** - Image processing
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **TensorFlow/PyTorch** - Deep learning framework
- **Matplotlib/Seaborn** - Data visualization
- **Scikit-learn** - Machine learning utilities

See `requirements.txt` for the complete list.

## 📖 Documentation

- **Notebooks**: See `notebooks/main_dl.ipynb` for detailed experiments and analysis
- **Source Code**: Module docstrings are available in `src/` files
- **Scripts**: Each script in `scripts/` contains inline documentation

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

**Author**: Sai-Siv  
**Repository**: [Weed Species Identification](https://github.com/Sai-Siv/Weed-Species-Identification-and-Analysis-Grassland-Ecosystems)

## 🙏 Acknowledgments

- Grassland ecosystem research community
- OpenCV documentation and community
- Deep learning frameworks (TensorFlow/PyTorch)
- Contributors and collaborators

## 📚 References

- OpenCV Documentation: https://docs.opencv.org/
- TensorFlow/PyTorch Guides: https://tensorflow.org/ / https://pytorch.org/
- Plant Identification Literature: [Add relevant papers/resources]

---

**Last Updated**: November 2025  
**Version**: 1.0.0
