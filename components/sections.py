"""
Page sections components
"""
from fasthtml.common import Section, Div, H2, H3, H4, P, A, Span, Footer, Img

def QuickOverview():
    """
    Quick overview section with text on left and image collage on right
    """
    return Section(
        Div(
            # Text and image collage section
            Div(
                # Left side - Welcome text
                Div(
                    H2(
                        "Welcome to ",
                        Span("Sandipani VidhyaPeeth", cls="gradient-text"),
                        cls="section-title"
                    ),
                    P(
                        "A premier educational institution dedicated to nurturing young minds and fostering academic excellence in Ponchhari, Madhya Pradesh.",
                        cls="section-description"
                    ),
                    P(
                        "We believe in holistic education that combines rigorous academics with character development, creativity, and practical skills to prepare students for successful careers and meaningful lives.",
                        cls="section-description"
                    ),
                    cls="overview-text"
                ),
                # Right side - Image collage
                Div(
                    Img(src="/static/images/home/ed-robertson-eeSdJfLfx1A-unsplash.jpg", alt="Campus Life", cls="collage-img collage-img-1"),
                    Img(src="/static/images/home/element5-digital-7K_agbqPqYo-unsplash.jpg", alt="Students Learning", cls="collage-img collage-img-2"),
                    Img(src="/static/images/home/feliphe-schiarolli-hes6nUC1MVc-unsplash.jpg", alt="Academic Excellence", cls="collage-img collage-img-3"),
                    cls="overview-collage"
                ),
                cls="overview-content"
            ),
            # Three cards grid below
            Div(
                Div(
                    Img(src="/static/images/home/kimberly-farmer-lUaaKCUANVI-unsplash.jpg", alt="Academic Excellence", cls="overview-card-img"),
                    H3("Academic Excellence"),
                    P("Comprehensive curriculum from Primary to High School with modern teaching methods to prepare students for successful careers"),
                    A("LEARN MORE", href="/academics", cls="overview-card-btn"),
                    cls="overview-card"
                ),
                Div(
                    Img(src="/static/images/home/priscilla-du-preez-ggeZ9oyI-PE-unsplash.jpg", alt="Holistic Development", cls="overview-card-img"),
                    H3("Holistic Development"),
                    P("Sports, arts, culture, and extracurricular activities for well-rounded growth and character building"),
                    A("LEARN MORE", href="/student-life", cls="overview-card-btn"),
                    cls="overview-card"
                ),
                Div(
                    Img(src="/static/images/home/kelli-tungay-2LJ4rqK2qfU-unsplash.jpg", alt="Proven Track Record", cls="overview-card-img"),
                    H3("Proven Track Record"),
                    P("25+ years of excellence in education with outstanding student achievements and successful alumni"),
                    A("LEARN MORE", href="/about", cls="overview-card-btn"),
                    cls="overview-card"
                ),
                cls="overview-grid"
            ),
            cls="container"
        ),
        cls="quick-overview",
        id="overview"
    )


def CTASection():
    """
    Call-to-action section
    """
    return Section(
        Div(
            Div(
                H2("Ready to Join Our Community?"),
                P("Discover how Sandipani VidhyaPeeth can help your child reach their full potential"),
                Div(
                    A("Apply for Admission", href="/admissions", cls="btn btn-primary"),
                    A("Schedule a Visit", href="/contact", cls="btn btn-secondary"),
                    cls="cta-buttons"
                ),
                cls="cta-content"
            ),
            cls="container"
        ),
        cls="cta-section"
    )


def FooterSection():
    """
    Footer section with links
    """
    return Footer(
        Div(
            # Footer content grid
            Div(
                # About section
                Div(
                    Div(
                        Div("🎓", cls="logo-icon"),
                        Span("Sandipani VidhyaPeeth", cls="logo-text"),
                        style="display: flex; align-items: center; gap: 0.75rem; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem;"
                    ),
                    P(
                        "Empowering minds, shaping futures, and building tomorrow's leaders through excellence in education.",
                        cls="footer-description"
                    ),
                    cls="footer-section"
                ),
                # Quick Links
                Div(
                    H4("Quick Links"),
                    Div(
                        A("Home", href="/"),
                        A("About Us", href="/about"),
                        A("Academics", href="/academics"),
                        A("Admissions", href="/admissions"),
                        cls="footer-links"
                    ),
                    cls="footer-section"
                ),
                # Programs
                Div(
                    H4("Programs"),
                    Div(
                        A("Primary School", href="/academics"),
                        A("Middle School", href="/academics"),
                        A("High School", href="/academics"),
                        A("Extracurricular", href="/student-life"),
                        cls="footer-links"
                    ),
                    cls="footer-section"
                ),
                # Connect
                Div(
                    H4("Connect"),
                    Div(
                        A("Contact Us", href="/contact"),
                        A("News & Events", href="/news"),
                        A("Alumni", href="/alumni"),
                        cls="footer-links"
                    ),
                    cls="footer-section"
                ),
                cls="footer-content"
            ),
            # Footer bottom
            Div(
                P(
                    "© ",
                    Span("2025", id="current-year"),
                    " Sandipani VidhyaPeeth. All rights reserved."
                ),
                cls="footer-bottom"
            ),
            cls="container"
        ),
        cls="footer"
    )
