# Project Development Guide

## Directory Structure Overview

Your project has been reorganized into a professional Python project structure:

```
Weed-Species-Identification-and-Analysis-Grassland-Ecosystems/
├── data/                          # Data management
│   ├── raw/                       # Original, untouched raw data
│   │   └── .gitkeep               # Placeholder for dataset.zip
│   └── processed/                 # Extracted and processed data
│       └── .gitkeep               # Placeholder for train/ and val/ directories
├── notebooks/
│   └── main_dl.ipynb              # Jupyter notebook for experiments and analysis
├── scripts/                       # Utility and standalone scripts
│   ├── opencv-test.py             # OpenCV functionality testing
│   ├── Rename.py                  # Batch image renaming utility
│   ├── resize.py                  # Image resizing and preprocessing
│   └── train-test-split.py        # Dataset splitting utility
├── src/                           # Core source code package
│   ├── __init__.py                # Makes src/ a Python package
│   ├── data.py                    # Data loading and processing functions
│   └── predict.py                 # Model prediction and inference logic
├── models/                        # Pre-trained model checkpoints
├── .gitignore                     # Git configuration for version control
├── README.md                      # Main project documentation
└── requirements.txt               # Python dependencies
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Working with Each Directory

### `data/` Directory

**Purpose**: Centralized data management

- **raw/**: Store original datasets here without modification
  - Recommended: Keep `dataset.zip` here
  - Never modify files in this directory

- **processed/**: Contains cleaned and extracted data
  - Organize extracted images by species
  - Create subdirectories: `train/` and `val/`
  - Structure:
    ```
    processed/
    ├── train/
    │   ├── CELOSIA_ARGENTEA_L/
    │   ├── CROWFOOT_GRASS/
    │   └── PURPLE_CHLORIS/
    └── val/
        ├── CELOSIA_ARGENTEA_L/
        ├── CROWFOOT_GRASS/
        └── PURPLE_CHLORIS/
    ```

### `scripts/` Directory

**Purpose**: Utility scripts for data preprocessing and testing

Available scripts:

1. **Rename.py** - Batch rename image files
   ```bash
   python scripts/Rename.py
   ```

2. **resize.py** - Resize images to standard dimensions
   ```bash
   python scripts/resize.py
   ```

3. **train-test-split.py** - Split data into training and validation sets
   ```bash
   python scripts/train-test-split.py
   ```

4. **opencv-test.py** - Test OpenCV functionality and image processing
   ```bash
   python scripts/opencv-test.py
   ```

### `src/` Directory

**Purpose**: Core application code and modules

The `src/` directory is configured as a Python package (with `__init__.py`).

**Modules**:

1. **data.py** - Data handling functions
   ```python
   from src.data import load_training_data, preprocess_images
   ```

2. **predict.py** - Model prediction and inference
   ```python
   from src.predict import classify_image, get_predictions
   ```

### `notebooks/` Directory

**Purpose**: Jupyter notebooks for experimentation and analysis

- **main_dl.ipynb**: Main notebook for deep learning experiments
  ```bash
  jupyter notebook notebooks/main_dl.ipynb
  ```

### `models/` Directory

**Purpose**: Store trained model files

Organize models by:
- Model architecture
- Training date
- Version number

Example: `models/cnn_model_v1.h5`

## Running the Project

### Option 1: Using Jupyter Notebook (Recommended for Experiments)

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows

# Start Jupyter
jupyter notebook

# Open notebooks/main_dl.ipynb
```

### Option 2: Using Scripts

```bash
# Process images
python scripts/resize.py
python scripts/Rename.py

# Split data
python scripts/train-test-split.py

# Test OpenCV
python scripts/opencv-test.py
```

### Option 3: Using Core Modules

```python
# In your Python script or notebook
from src import data, predict

# Load data
training_data = data.load_training_data('data/processed/train')

# Make predictions
results = predict.classify_image('path/to/image.jpg')
print(results)
```

## Development Workflow

### Adding New Features

1. **For core logic**:
   - Create new functions in `src/`
   - Update `src/__init__.py` to export them

2. **For utilities**:
   - Add scripts to `scripts/`
   - Include proper documentation

3. **For experimentation**:
   - Use `notebooks/main_dl.ipynb`
   - Document your findings

### Best Practices

1. **Keep data organized**:
   - Never modify files in `data/raw/`
   - Use `data/processed/` for all modifications

2. **Use relative imports**:
   ```python
   from src import data, predict
   ```

3. **Document your code**:
   - Add docstrings to functions
   - Include comments for complex logic

4. **Version control**:
   - Use `.gitignore` to exclude large files
   - Commit code regularly
   - Don't commit data files or models

## Common Tasks

### Task 1: Prepare Dataset

```bash
# 1. Extract raw dataset
# Place dataset.zip in data/raw/

# 2. Rename images (if needed)
python scripts/Rename.py

# 3. Resize images
python scripts/resize.py

# 4. Split into train/val
python scripts/train-test-split.py

# Result: Organized data in data/processed/
```

### Task 2: Train Model

```bash
# Open Jupyter and run main_dl.ipynb
jupyter notebook notebooks/main_dl.ipynb

# Or use your own Python script
python train.py  # (create if needed)
```

### Task 3: Make Predictions

```python
from src import predict

# Load image and predict
result = predict.classify_image('path/to/image.jpg')
print(f"Species: {result['species']}")
print(f"Confidence: {result['confidence']}")
```

## Dependencies

Key libraries (see `requirements.txt` for complete list):

- **opencv-python**: Image processing
- **numpy/pandas**: Data manipulation
- **tensorflow/torch**: Deep learning
- **matplotlib/seaborn**: Visualization
- **scikit-learn**: Machine learning utilities
- **jupyter**: Interactive notebooks

To install or update dependencies:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### Issue: Import errors when using `src` modules

**Solution**: Ensure you're running Python from the project root directory.

```bash
cd Weed-Species-Identification-and-Analysis-Grassland-Ecosystems
python your_script.py
```

### Issue: Virtual environment not activating

**Solution**: Use the full path to activate:

```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Issue: Jupyter kernel not finding `src` modules

**Solution**: Restart the kernel after installing packages or ensure the virtual environment is properly activated.

## Next Steps

1. ✅ Review the new project structure
2. ✅ Create virtual environment
3. ✅ Install dependencies
4. ✅ Organize raw data in `data/raw/`
5. ✅ Run preprocessing scripts
6. ✅ Start with `notebooks/main_dl.ipynb`
7. ✅ Train your model
8. ✅ Make predictions using `src/predict.py`

## References

- [Python Packaging Guide](https://packaging.python.org/)
- [Real Python Project Structure](https://realpython.com/navigating-the-python-ecosystem/)
- [TensorFlow Documentation](https://tensorflow.org/)
- [OpenCV Documentation](https://docs.opencv.org/)

---

**Project Version**: 1.0.0  
**Last Updated**: November 2025
