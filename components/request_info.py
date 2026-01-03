"""
Request Info page components
"""
from fasthtml.common import Section, Div, H1, H2, H3, H4, P, Span, Form, Input, Textarea, Label, Button, Select, Option, I

def RequestInfoHero():
    """
    Hero section for Request Info page
    """
    return Section(
        # Background
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
                    "Request ",
                    Span("Information", cls="gradient-text"),
                    cls="hero-title"
                ),
                P("We'd love to share more about Sandipani VidhyaPeeth with you", cls="hero-subtitle about-subtitle"),
                cls="hero-content"
            ),
            cls="container"
        ),
        cls="about-hero"
    )

def RequestInfoForm():
    """
    Request information form section
    """
    return Section(
        Div(
            # Two column layout (1/3 and 2/3)
            Div(
                # Left side (1/3) - What You'll Receive Card
                Div(
                    H3("What You'll Receive", cls="info-card-title-main"),
                    P(
                        "Fill out the form and our admissions team will send you detailed information about:",
                        cls="info-card-description"
                    ),
                    Div(
                        P("✓ School prospectus & academic programs", cls="receive-item"),
                        P("✓ Admission requirements & process", cls="receive-item"),
                        P("✓ Fee structure & payment options", cls="receive-item"),
                        P("✓ Extracurricular activities info", cls="receive-item"),
                        P("✓ Campus facilities & infrastructure", cls="receive-item"),
                        cls="receive-list"
                    ),
                    cls="info-card-main"
                ),

                # Right side (2/3) - Form (No labels, only placeholders)
                Div(
                    Form(
                        # Form fields group
                        Div(
                            # Row 1: Name and Email
                            Div(
                                Input(
                                    type="text",
                                    id="name",
                                    name="name",
                                    placeholder="Full Name *",
                                    required=True,
                                    cls="form-input-pill"
                                ),
                                Input(
                                    type="email",
                                    id="email",
                                    name="email",
                                    placeholder="Email Address *",
                                    required=True,
                                    cls="form-input-pill"
                                ),
                                cls="form-row"
                            ),

                            # Row 2: Phone and Grade
                            Div(
                                Input(
                                    type="tel",
                                    id="phone",
                                    name="phone",
                                    placeholder="Phone Number *",
                                    required=True,
                                    cls="form-input-pill"
                                ),
                                Select(
                                    Option("Student's Current Grade", value="", selected=True),
                                    Option("Nursery", value="nursery"),
                                    Option("LKG", value="lkg"),
                                    Option("UKG", value="ukg"),
                                    Option("Class 1", value="1"),
                                    Option("Class 2", value="2"),
                                    Option("Class 3", value="3"),
                                    Option("Class 4", value="4"),
                                    Option("Class 5", value="5"),
                                    Option("Class 6", value="6"),
                                    Option("Class 7", value="7"),
                                    Option("Class 8", value="8"),
                                    Option("Class 9", value="9"),
                                    Option("Class 10", value="10"),
                                    Option("Class 11", value="11"),
                                    Option("Class 12", value="12"),
                                    id="grade",
                                    name="grade",
                                    cls="form-input-pill"
                                ),
                                cls="form-row"
                            ),

                            # Row 3: Area of Interest
                            Select(
                                Option("Area of Interest", value="", selected=True),
                                Option("Academic Programs", value="academics"),
                                Option("Admission Process", value="admissions"),
                                Option("Fee Structure", value="fees"),
                                Option("Sports & Activities", value="sports"),
                                Option("Facilities", value="facilities"),
                                Option("Other", value="other"),
                                id="interest",
                                name="interest",
                                cls="form-input-pill"
                            ),

                            # Row 4: Textarea
                            Textarea(
                                id="message",
                                name="message",
                                placeholder="Additional Questions or Comments...",
                                rows="3",
                                cls="form-input-pill form-textarea-pill"
                            ),
                            cls="form-fields-group"
                        ),

                        # Submit button - separate to align with bottom
                        Button(
                            "Submit Request",
                            type="submit",
                            cls="btn btn-primary form-submit-pill"
                        ),
                        cls="request-form",
                        method="POST",
                        action="#"
                    ),
                    cls="form-right"
                ),

                cls="request-info-content"
            ),

            # Three contact cards below (full width)
            Div(
                # Visit Us Card
                Div(
                    Div(
                        I(cls="fas fa-map-marker-alt contact-icon"),
                        cls="contact-icon-wrapper"
                    ),
                    H4("Visit Us", cls="contact-card-title"),
                    P("Sandipani VidhyaPeeth", cls="contact-text"),
                    P("69WM+GP7, Ponchhari", cls="contact-text"),
                    P("Madhya Pradesh 476229", cls="contact-text"),
                    cls="contact-card"
                ),

                # Call Us Card
                Div(
                    Div(
                        I(cls="fas fa-phone contact-icon"),
                        cls="contact-icon-wrapper"
                    ),
                    H4("Call Us", cls="contact-card-title"),
                    P("+91 123 456 7890", cls="contact-text"),
                    P("Mon-Fri: 9:00 AM - 5:00 PM", cls="contact-text"),
                    cls="contact-card"
                ),

                # Email Us Card
                Div(
                    Div(
                        I(cls="fas fa-envelope contact-icon"),
                        cls="contact-icon-wrapper"
                    ),
                    H4("Email Us", cls="contact-card-title"),
                    P("info@sandipanividhyapeeth.edu", cls="contact-text"),
                    P("admissions@sandipanividhyapeeth.edu", cls="contact-text"),
                    cls="contact-card"
                ),

                cls="contact-cards-grid-bottom"
            ),

            cls="container"
        ),
        cls="form-section"
    )
