"""
Hero section component
"""
from fasthtml.common import Section, Div, H1, P, A, Span

def Hero():
    """
    Full-screen hero section with background carousel
    """
    return Section(
        # Background carousel
        Div(
            Div(
                style="background-image: url('/static/images/home/hero-background-1.jpg')",
                cls="hero-slide active"
            ),
            Div(cls="hero-overlay"),
            cls="hero-background"
        ),
        # Hero content
        Div(
            Div(
                H1(
                    "Preparing Students for Successful ",
                    Span("Careers", cls="gradient-text"),
                    cls="hero-title"
                ),
                Div(
                    A("Explore Programs", href="#overview", cls="btn btn-primary"),
                    A("Schedule Visit", href="/contact", cls="btn btn-secondary"),
                    cls="hero-buttons"
                ),
                cls="hero-content"
            ),
            cls="container"
        ),
        cls="hero"
    )
