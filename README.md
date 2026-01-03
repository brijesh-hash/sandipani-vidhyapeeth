# Sandipani VidhyaPeeth Website

Official website for Sandipani VidhyaPeeth school.

## Project Structure

This project uses **FastHTML (Python)** for development and generates **static HTML** for deployment to GitHub Pages.

```
sandipani-vidhyapeeth/
├── main.py              # FastHTML app entry point
├── components/          # Python components (Navbar, Hero, Sections, etc.)
├── static/             # CSS, JS, and images (used in both dev and production)
├── dist/               # Generated static HTML (created by build.py)
├── build.py            # Build script to generate static site
└── reference/          # Design reference images
```

## Development Workflow

### 1. Development (Python/FastHTML)

Work with the FastHTML Python project for development:

```bash
# Install dependencies
uv sync

# Run development server
uv run main.py
```

The site will be available at `http://localhost:5001`

**Make all your changes in:**
- `main.py` - Route definitions
- `components/` - Python components
- `static/` - CSS, JS, images

### 2. Build Static Site

When ready to deploy, generate static HTML files:

```bash
# Make sure dev server is running first!
uv run main.py  # In one terminal

# Then in another terminal, run build script
python3 build.py
```

This will:
- ✅ Generate clean HTML files from your FastHTML app
- ✅ Remove FastHTML-specific scripts (HTMX, etc.)
- ✅ Fix all links to work with static `.html` files
- ✅ Copy static assets (CSS, JS, images)
- ✅ Output everything to `dist/` folder

### 3. Deploy to GitHub Pages

The `dist/` folder contains your complete static website ready for deployment.

**Option A: Manual Deployment**
```bash
# Copy dist/ contents to your friend's repo
cp -r dist/* /path/to/friend/repo/
cd /path/to/friend/repo
git add .
git commit -m "Update website"
git push
```

**Option B: GitHub Pages Branch**
```bash
# Push dist/ folder to gh-pages branch
git subtree push --prefix dist origin gh-pages
```

## Directory Explanation

### Development Files (Not deployed)
- `main.py`, `components/`, `reference/` - Python development files
- `.venv/`, `__pycache__/` - Python virtual environment and cache
- These are in `.gitignore` and won't be deployed

### Production Files (Deployed)
- `dist/` - Contains the complete static website
- `dist/index.html`, `dist/about.html`, etc. - Static HTML pages
- `dist/static/` - CSS, JavaScript, and images

## Important Notes

⚠️ **Never edit files in `dist/` directly!** They are auto-generated.

✅ **Always edit Python files**, then rebuild with `build.py`

🔄 **Workflow Summary:**
1. Edit Python components
2. Test in development server (`uv run main.py`)
3. Run build script (`python3 build.py`)
4. Deploy `dist/` folder to GitHub Pages

## Pages

- **Home** (`/`) - Hero, Quick Links, Overview, Feature Cards, CTA
- **About** (`/about`) - Hero, Principal Message, Community, Statistics
- **Academics** (`/academics`) - Coming soon
- **Admissions** (`/admissions`) - Coming soon
- **Student Life** (`/student-life`) - Coming soon
- **Contact** (`/contact`) - Coming soon

## Technology Stack

- **Development:** FastHTML (Python web framework)
- **Deployment:** Static HTML/CSS/JavaScript
- **Styling:** Custom CSS with responsive design
- **Fonts:** Google Fonts (Inter)
- **Hosting:** GitHub Pages

---

Built with ❤️ for Sandipani VidhyaPeeth
