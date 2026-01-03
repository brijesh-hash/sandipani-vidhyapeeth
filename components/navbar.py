"""
Navigation bar component
"""
from fasthtml.common import Nav, Div, A, Ul, Li, Img

def Navbar():
    """
    Main navigation bar component with Park University style
    Top bar with logo and location info + Main nav bar with menu links
    """
    return Div(
        # Top bar with logo and location links
        Div(
            Div(
                # Logo and school name on the left
                A(
                    Img(src="/static/images/logo.png", alt="Sandipani Logo", cls="logo-image"),
                    Div(
                        Div("SANDIPANI", cls="logo-main-text"),
                        Div("VIDHYAPEETH", cls="logo-sub-text"),
                        cls="logo-text-container"
                    ),
                    href="/",
                    cls="logo"
                ),
                # Location links on the right
                Div(
                    A("REQUEST INFO", href="/request-info", cls="top-bar-link"),
                    A("PLAN A VISIT", href="/plan-visit", cls="top-bar-link"),
                    A("DONATE", href="/donate", cls="top-bar-link"),
                    cls="top-bar-links"
                ),
                # Scroll buttons (shown only when scrolled)
                Div(
                    A("APPLY NOW", href="/admissions", cls="scroll-btn"),
                    A("REQUEST INFO", href="/request-info", cls="scroll-btn"),
                    A("PLAN A VISIT", href="/plan-visit", cls="scroll-btn"),
                    A("DONATE", href="/donate", cls="scroll-btn"),
                    cls="scroll-buttons"
                ),
                cls="top-bar-container"
            ),
            cls="top-bar"
        ),
        # Main navigation bar with menu links
        Nav(
            Div(
                Ul(
                    Li(A(Div("🏠", cls="home-icon"), "HOME", href="/", cls="nav-link home-link")),
                    Li(A("ACADEMICS", href="/academics", cls="nav-link")),
                    Li(A("ADMISSION", href="/admissions", cls="nav-link")),
                    Li(A("ALUMNI", href="/alumni", cls="nav-link")),
                    Li(A("LIFE@SANDIPANI", href="/student-life", cls="nav-link")),
                    Li(A("ABOUT SANDIPANI", href="/about", cls="nav-link")),
                    cls="nav-menu"
                ),
                cls="nav-container"
            ),
            cls="navbar"
        ),
        cls="header-wrapper"
    )
