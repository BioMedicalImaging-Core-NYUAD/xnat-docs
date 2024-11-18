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


# Haven't tested these yet VV
## Deployment

### Option 1: Deploy to ReadTheDocs (Recommended)

1. Push your repository to GitHub
2. Go to [ReadTheDocs.org](https://readthedocs.org/)
3. Sign in with your GitHub account
4. Click "Import a Project"
5. Select your repository
6. Click "Build Documentation"

Your documentation will be available at: `https://nyuad-xnat-docs.readthedocs.io/`

### Option 2: Deploy to GitHub Pages

1. Create a new branch named `gh-pages`:
   ```bash
   git checkout --orphan gh-pages
   ```

2. Remove everything except the build directory:
   ```bash
   git rm -rf .
   mv build/html/* .
   rm -rf build
   ```

3. Add, commit, and push:
   ```bash
   git add .
   git commit -m "Initial GitHub Pages deployment"
   git push origin gh-pages
   ```

4. Go to your repository settings on GitHub:
   - Navigate to "Pages"
   - Select the `gh-pages` branch as source
   - Save

Your documentation will be available at: `https://[username].github.io/[repository-name]/`

### Option 3: Deploy to Your Own Server

1. Build the documentation:
   ```bash
   make html
   ```

2. Copy the contents of `build/html` to your web server:
   ```bash
   rsync -av build/html/ user@server:/path/to/webroot/
   ```

## Maintenance

### Updating Documentation

1. Make changes to the RST files in the `source` directory
2. Test locally using sphinx-autobuild
3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update documentation"
   git push origin main
   ```

4. ReadTheDocs will automatically rebuild and deploy your documentation

### Version Control Best Practices

- Create feature branches for significant changes
- Use meaningful commit messages
- Review changes locally before pushing
- Keep dependencies updated


