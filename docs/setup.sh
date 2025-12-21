#!/bin/bash
# Setup script for XNAT Documentation

set -e

echo "Setting up XNAT Documentation build environment..."

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python version: $PYTHON_VERSION"

# Check if Python 3.8+
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
    echo "ERROR: Python 3.8 or higher is required. Found: $PYTHON_VERSION"
    echo "Please install a newer Python version and try again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✓ Setup complete!"
echo ""
echo "To build the documentation, run:"
echo "  cd docs"
echo "  source venv/bin/activate"
echo "  make html"
echo ""
echo "For live reload during development, run:"
echo "  sphinx-autobuild source build/html"




