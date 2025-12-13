#!/usr/bin/env python3
"""
Build script to generate static HTML files from FastHTML app
This keeps development (Python) separate from deployment (static HTML)
"""
import re
import shutil
from pathlib import Path
import subprocess
import time
import requests
from urllib.parse import urljoin

# Configuration
BASE_URL = "http://localhost:5001"
DIST_DIR = Path("dist")
PAGES = [
    ("", "index.html"),           # Home page
    ("about", "about.html"),
    ("academics", "academics.html"),
    ("admissions", "admissions.html"),
    ("student-life", "student-life.html"),
    ("contact", "contact.html"),
    ("request-info", "request-info.html"),
    ("plan-visit", "plan-visit.html"),
    ("donate", "donate.html"),
]

def clean_html(content):
    """Remove FastHTML-specific scripts and fix links for static deployment"""

    # Remove FastHTML scripts
    content = re.sub(
        r'<script src="https://cdn\.jsdelivr\.net/npm/htmx\.org@.*?</script>.*?<script src="https://cdn\.jsdelivr\.net/gh/gnat/css-scope-inline@.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove Pico CSS
    content = re.sub(
        r'<link rel="stylesheet" href="https://cdn\.jsdelivr\.net/npm/@picocss/pico@.*?">',
        '',
        content
    )

    # Remove Pico CSS style override
    content = re.sub(
        r'<style>:root \{ --pico-font-size: 100%; \}</style>',
        '',
        content
    )

    # Remove canonical URLs
    content = re.sub(
        r'<link rel="canonical" href=".*?">',
        '',
        content
    )

    # Fix internal links to add .html extension
    content = content.replace('href="/"', 'href="index.html"')

    def add_html_extension(match):
        href = match.group(1)
        if href.startswith('#') or href == '/':
            return f'href="{href}"'
        page = href.lstrip('/')
        if page.startswith('static'):
            # Already relative
            return f'href="{page}"'
        return f'href="{page}.html"'

    content = re.sub(r'href="(/[^"]*)"', add_html_extension, content)

    # Fix absolute paths for static assets to relative
    content = content.replace('href="/static/', 'href="static/')
    content = content.replace('src="/static/', 'src="static/')

    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return content

def check_server():
    """Check if FastHTML server is running"""
    try:
        response = requests.get(BASE_URL, timeout=2)
        return response.status_code == 200
    except:
        return False

def build():
    """Generate static site from FastHTML app"""

    print("🏗️  Building static site from FastHTML app...\n")

    # Check if server is running
    if not check_server():
        print("❌ Error: FastHTML server is not running!")
        print("   Please start the server with: uv run main.py")
        print("   Then run this build script again.")
        return False

    # Clean and create dist directory
    if DIST_DIR.exists():
        print(f"🗑️  Cleaning {DIST_DIR}/ directory...")
        shutil.rmtree(DIST_DIR)

    DIST_DIR.mkdir()
    print(f"✅ Created {DIST_DIR}/ directory\n")

    # Generate HTML pages
    print("📄 Generating HTML pages...")
    for route, filename in PAGES:
        url = urljoin(BASE_URL, route)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                cleaned_html = clean_html(response.text)
                output_file = DIST_DIR / filename
                output_file.write_text(cleaned_html)
                print(f"   ✓ {filename}")
            else:
                print(f"   ✗ {filename} (HTTP {response.status_code})")
        except Exception as e:
            print(f"   ✗ {filename} (Error: {e})")

    # Copy static assets
    print("\n📦 Copying static assets...")
    src_static = Path("static")
    if src_static.exists():
        shutil.copytree(src_static, DIST_DIR / "static")
        print("   ✓ static/")

    print(f"\n✅ Build complete! Static site generated in {DIST_DIR}/")
    print(f"\n📁 Deploy the contents of {DIST_DIR}/ folder to GitHub Pages")
    print(f"   All HTML files and assets are ready for deployment.")

    return True

if __name__ == "__main__":
    build()
