"""
About page hero section component
"""
from fasthtml.common import Section, Div, H1, P, Span

def AboutHero():
    """
    Simple hero section with "About Sandipani" text and subtitle
    """
    return Section(
        # Background
        Div(
            Div(
                style="background-image: url('/static/images/about/about_sanipani_2.jpg')",
                cls="hero-slide active"
            ),
            Div(cls="hero-overlay"),
            cls="hero-background"
        ),
        # Hero content - title and subtitle
        Div(
            Div(
                H1(
                    "About ",
                    Span("Sandipani", cls="gradient-text"),
                    cls="hero-title"
                ),
                P("Excellence in Education Since 1999", cls="hero-subtitle about-subtitle"),
                cls="hero-content"
            ),
            cls="container"
        ),
        cls="about-hero"
    )
