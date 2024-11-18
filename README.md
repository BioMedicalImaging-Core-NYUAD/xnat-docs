# Development
## Setup

1. Create a new conda environment:
   ```bash
   conda create -n xnat-docs python=3.10
   conda activate xnat-docs
   ```

2. Install pip package manager:
   ```bash
   conda install pip
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Serving the Documentation

You have two options to view the documentation locally:

### Option 1: Simple Python Server

1. Build the documentation:
   ```bash
   make html
   ```

2. Run a basic HTTP server to view the built documentation:
   
   ```bash
   python -m http.server --directory build/html
   ```

### Option 2: Sphinx Autobuild

Run a local server that automatically rebuilds the documentation when you make changes:

```bash
sphinx-autobuild source build/html
```


