"""
Sandipani VidhyaPeeth - FastHTML Website
Main application file
"""
from fasthtml.common import *
from components import Navbar, Hero, QuickLinks, QuickOverview, CTASection, FooterSection
from components.about_hero import AboutHero
from components.about_sections import PrincipalMessageSection, CommunitySection, StatisticsSection
from components.request_info import RequestInfoHero, RequestInfoForm
from components.plan_visit import PlanVisitHero, PlanVisitForm
from components.donate import DonateHero, DonateForm

# Create FastHTML app with static files and external resources
app, rt = fast_app(
    hdrs=(
        # Favicon
        Link(rel="icon", type="image/png", href="/static/images/logo.png"),
        # Google Fonts
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"
        ),
        # Font Awesome Icons
        Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
        ),
        # Custom CSS
        Link(rel="stylesheet", href="/static/css/styles.css", type="text/css"),
        # Custom JavaScript
        Script(src="/static/js/script.js"),
    )
)


# Routes
@rt("/")
def get():
    """Home page"""
    return (
        Title("Sandipani VidhyaPeeth - Home"),
        Navbar(),
        Hero(),
        QuickLinks(),
        QuickOverview(),
        CTASection(),
        FooterSection()
    )


@rt("/academics")
def get():
    """Academics page"""
    return (
        Title("Academics - Sandipani VidhyaPeeth"),
        Navbar(),
        Div(
            H1("Academics Page - Coming Soon", style="text-align: center; padding: 200px 0;")
        ),
        FooterSection()
    )


@rt("/admissions")
def get():
    """Admissions page"""
    return (
        Title("Admissions - Sandipani VidhyaPeeth"),
        Navbar(),
        Div(
            H1("Admissions Page - Coming Soon", style="text-align: center; padding: 200px 0;")
        ),
        FooterSection()
    )


@rt("/student-life")
def get():
    """Student Life page"""
    return (
        Title("Student Life - Sandipani VidhyaPeeth"),
        Navbar(),
        Div(
            H1("Student Life Page - Coming Soon", style="text-align: center; padding: 200px 0;")
        ),
        FooterSection()
    )


@rt("/about")
def get():
    """About Us page"""
    return (
        Title("About Us - Sandipani VidhyaPeeth"),
        Navbar(),
        AboutHero(),
        PrincipalMessageSection(),
        CommunitySection(),
        StatisticsSection(),
        FooterSection()
    )


@rt("/contact")
def get():
    """Contact page"""
    return (
        Title("Contact - Sandipani VidhyaPeeth"),
        Navbar(),
        Div(
            H1("Contact Page - Coming Soon", style="text-align: center; padding: 200px 0;")
        ),
        FooterSection()
    )


@rt("/request-info")
def get():
    """Request Information page"""
    return (
        Title("Request Information - Sandipani VidhyaPeeth"),
        Navbar(),
        RequestInfoHero(),
        RequestInfoForm(),
        FooterSection()
    )


@rt("/plan-visit")
def get():
    """Plan a Visit page"""
    return (
        Title("Plan a Visit - Sandipani VidhyaPeeth"),
        Navbar(),
        PlanVisitHero(),
        PlanVisitForm(),
        FooterSection()
    )


@rt("/donate")
def get():
    """Donate page"""
    return (
        Title("Donate - Sandipani VidhyaPeeth"),
        Navbar(),
        DonateHero(),
        DonateForm(),
        FooterSection()
    )


# Run the server
if __name__ == "__main__":
    serve()
