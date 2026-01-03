// Hero Background Carousel
let currentSlide = 0;
const slides = document.querySelectorAll('.hero-slide');
const totalSlides = slides.length;

function nextSlide() {
    if (slides.length === 0) return;

    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % totalSlides;
    slides[currentSlide].classList.add('active');
}

// Auto-rotate carousel every 5 seconds
if (slides.length > 0) {
    setInterval(nextSlide, 5000);
}

// Navbar scroll behavior
window.addEventListener('scroll', function() {
    const headerWrapper = document.querySelector('.header-wrapper');
    const scrollPosition = window.scrollY;

    // Add scrolled class after scrolling 100px
    if (scrollPosition > 100) {
        headerWrapper.classList.add('scrolled');
    } else {
        headerWrapper.classList.remove('scrolled');
    }
});

// Set current year in footer
document.addEventListener('DOMContentLoaded', function() {
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
});

// Console log for debugging
console.log('FastHTML School Website loaded successfully!');
