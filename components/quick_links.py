"""
Quick Links section - Call to action cards between hero and overview
"""
from fasthtml.common import Section, Div, H3, P, A, Img

def QuickLinks():
    """
    Quick action cards section with hover effects
    """
    return Section(
        Div(
            # Schedule a visit card
            Div(
                Div(
                    Img(src="/static/images/home/school.png", alt="Schedule", cls="quick-link-icon"),
                    H3("Visit", cls="quick-link-title"),
                    cls="quick-link-default"
                ),
                Div(
                    Img(src="/static/images/home/school.png", alt="Schedule", cls="quick-link-icon"),
                    H3("Schedule a visit", cls="quick-link-title-hover"),
                    A("SCHEDULE", href="/contact", cls="quick-link-btn"),
                    cls="quick-link-hover"
                ),
                cls="quick-link-card"
            ),
            # Learn More card
            Div(
                Div(
                    Img(src="/static/images/home/learn_more.png", alt="Learn More", cls="quick-link-icon"),
                    H3("Learn More", cls="quick-link-title"),
                    cls="quick-link-default"
                ),
                Div(
                    Img(src="/static/images/home/learn_more.png", alt="Learn More", cls="quick-link-icon"),
                    H3("We look forward to connect with you!", cls="quick-link-title-hover"),
                    A("LEARN MORE", href="/academics", cls="quick-link-btn"),
                    cls="quick-link-hover"
                ),
                cls="quick-link-card"
            ),
            # Apply card
            Div(
                Div(
                    Img(src="/static/images/home/apply.png", alt="Apply", cls="quick-link-icon"),
                    H3("Apply", cls="quick-link-title"),
                    cls="quick-link-default"
                ),
                Div(
                    Img(src="/static/images/home/apply.png", alt="Apply", cls="quick-link-icon"),
                    H3("Learn more about application process", cls="quick-link-title-hover"),
                    A("APPLY NOW", href="/admissions", cls="quick-link-btn"),
                    cls="quick-link-hover"
                ),
                cls="quick-link-card"
            ),
            # Giving card
            Div(
                Div(
                    Img(src="/static/images/home/tip-jar.svg", alt="Giving", cls="quick-link-icon"),
                    H3("Giving", cls="quick-link-title"),
                    cls="quick-link-default"
                ),
                Div(
                    Img(src="/static/images/home/tip-jar.svg", alt="Giving", cls="quick-link-icon"),
                    H3("Your contribution makes a difference", cls="quick-link-title-hover"),
                    A("DONATE", href="/contact", cls="quick-link-btn"),
                    cls="quick-link-hover"
                ),
                cls="quick-link-card"
            ),
            cls="quick-links-grid"
        ),
        cls="quick-links-section"
    )
