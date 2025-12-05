# School Website Project

A modern, responsive static website for Sandipani VidhyaPeeth.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern Aesthetics**: Beautiful gradients, smooth animations, and premium design
- **Key Sections**:
  - Home with hero section and statistics
  - About Us with mission, vision, and values
  - Academics with program details and facilities
  - Admissions with process steps and important dates
  - Contact with form and contact information

## Technologies Used

- HTML5
- CSS3 (with custom properties and modern features)
- Vanilla JavaScript
- Google Fonts (Inter & Playfair Display)

## Running Locally

### Option 1: Using the provided script
```bash
./start_server.sh
```

### Option 2: Using Python directly
```bash
python3 -m http.server 8000
```

### Option 3: Using Node.js (if installed)
```bash
npx http-server -p 8000
```

Then open your browser and navigate to:
```
http://localhost:8000
```

## File Structure

```
school_project/
├── index.html          # Main HTML file
├── styles.css          # All CSS styles
├── script.js           # JavaScript functionality
├── start_server.sh     # Server startup script
└── README.md           # This file
```

## Customization

### Colors
Edit the CSS variables in `styles.css` under `:root` to change the color scheme:
- `--primary-color`: Main brand color
- `--secondary-color`: Accent color
- `--gradient-primary`: Primary gradient

### Content
Edit `index.html` to update:
- School name and logo
- Section content
- Contact information
- Statistics and achievements

### Images
Replace placeholder images by:
1. Adding your images to the project folder
2. Updating the image sources in `index.html`

## Future Enhancements

When you're ready to deploy:
1. Purchase a domain name
2. Choose a hosting provider (Netlify, Vercel, GitHub Pages, etc.)
3. Upload the files or connect your repository
4. Configure DNS settings

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is created for Sandipani VidhyaPeeth.

---

**Note**: This is a static website. For dynamic features (user authentication, database, etc.), you'll need to integrate a backend service.
