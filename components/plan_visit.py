"""
Plan a Visit page components
"""
from fasthtml.common import Section, Div, H1, H2, H3, P, Span, Form, Input, Textarea, Label, Button, Select, Option, I

def PlanVisitHero():
    """
    Hero section for Plan a Visit page
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
                    "Plan Your ",
                    Span("Visit", cls="gradient-text"),
                    cls="hero-title"
                ),
                P("Experience our campus and see what makes Sandipani special", cls="hero-subtitle about-subtitle"),
                cls="hero-content"
            ),
            cls="container"
        ),
        cls="about-hero"
    )

def PlanVisitForm():
    """
    Visit booking form section
    """
    return Section(
        Div(
            # Two column layout
            Div(
                # Left side - Information (Beautiful info cards)
                Div(
                    H2("Schedule Your", cls="form-section-title"),
                    H2("Campus Tour", cls="form-section-title-sub"),
                    P(
                        "Book a personalized tour of our campus and meet with our admissions team to learn more about Sandipani VidhyaPeeth.",
                        cls="form-section-description"
                    ),

                    # Info cards with icons
                    Div(
                        # Card 1 - What to Expect
                        Div(
                            Div(
                                I(cls="fas fa-school icon-large"),
                                cls="info-card-icon-wrapper"
                            ),
                            H3("What to Expect", cls="info-card-title"),
                            Div(
                                Div(
                                    I(cls="fas fa-check-circle"),
                                    P("Guided campus tour (45-60 minutes)"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-check-circle"),
                                    P("Visit classrooms and facilities"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-check-circle"),
                                    P("Meet with admissions counselor"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-check-circle"),
                                    P("Q&A session with faculty (optional)"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-check-circle"),
                                    P("Refreshments provided"),
                                    cls="info-card-item"
                                ),
                                cls="info-card-list"
                            ),
                            cls="info-card"
                        ),

                        # Card 2 - Visiting Hours
                        Div(
                            Div(
                                I(cls="fas fa-clock icon-large"),
                                cls="info-card-icon-wrapper"
                            ),
                            H3("Visiting Hours", cls="info-card-title"),
                            Div(
                                Div(
                                    I(cls="fas fa-calendar-day"),
                                    P("Monday - Friday: 9:00 AM - 3:00 PM"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-calendar-week"),
                                    P("Saturday: 10:00 AM - 1:00 PM"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-door-closed"),
                                    P("Sunday: Closed"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-info-circle"),
                                    P("Please book at least 24 hours in advance"),
                                    cls="info-card-item"
                                ),
                                cls="info-card-list"
                            ),
                            cls="info-card"
                        ),

                        # Card 3 - Location
                        Div(
                            Div(
                                I(cls="fas fa-map-marker-alt icon-large"),
                                cls="info-card-icon-wrapper"
                            ),
                            H3("Location", cls="info-card-title"),
                            Div(
                                Div(
                                    I(cls="fas fa-map-pin"),
                                    P("Sandipani VidhyaPeeth"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-road"),
                                    P("69WM+GP7, Ponchhari"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-city"),
                                    P("Madhya Pradesh 476229"),
                                    cls="info-card-item"
                                ),
                                Div(
                                    I(cls="fas fa-parking"),
                                    P("Free parking available"),
                                    cls="info-card-item"
                                ),
                                cls="info-card-list"
                            ),
                            cls="info-card info-card-highlight"
                        ),

                        cls="info-cards-grid"
                    ),
                    cls="form-left"
                ),

                # Right side - Form
                Div(
                    H3(
                        I(cls="fas fa-calendar-check"),
                        Span(" Book Your Visit", cls="form-title-text"),
                        cls="form-title"
                    ),
                    Form(
                        # Name
                        Div(
                            Label(
                                I(cls="fas fa-user form-icon"),
                                Span(" Full Name *"),
                                For="visitor_name",
                                cls="form-label"
                            ),
                            Input(
                                type="text",
                                id="visitor_name",
                                name="visitor_name",
                                placeholder="Enter your full name",
                                required=True,
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Email
                        Div(
                            Label(
                                I(cls="fas fa-envelope form-icon"),
                                Span(" Email Address *"),
                                For="visitor_email",
                                cls="form-label"
                            ),
                            Input(
                                type="email",
                                id="visitor_email",
                                name="visitor_email",
                                placeholder="your.email@example.com",
                                required=True,
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Phone
                        Div(
                            Label(
                                I(cls="fas fa-phone form-icon"),
                                Span(" Phone Number *"),
                                For="visitor_phone",
                                cls="form-label"
                            ),
                            Input(
                                type="tel",
                                id="visitor_phone",
                                name="visitor_phone",
                                placeholder="+91 XXXXX XXXXX",
                                required=True,
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Preferred Date
                        Div(
                            Label(
                                I(cls="fas fa-calendar-day form-icon"),
                                Span(" Preferred Visit Date *"),
                                For="visit_date",
                                cls="form-label"
                            ),
                            Input(
                                type="date",
                                id="visit_date",
                                name="visit_date",
                                required=True,
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Preferred Time
                        Div(
                            Label(
                                I(cls="fas fa-clock form-icon"),
                                Span(" Preferred Time *"),
                                For="visit_time",
                                cls="form-label"
                            ),
                            Select(
                                Option("Select Time", value="", selected=True),
                                Option("9:00 AM - 10:00 AM", value="9-10"),
                                Option("10:00 AM - 11:00 AM", value="10-11"),
                                Option("11:00 AM - 12:00 PM", value="11-12"),
                                Option("12:00 PM - 1:00 PM", value="12-13"),
                                Option("1:00 PM - 2:00 PM", value="13-14"),
                                Option("2:00 PM - 3:00 PM", value="14-15"),
                                id="visit_time",
                                name="visit_time",
                                required=True,
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Number of Visitors
                        Div(
                            Label(
                                I(cls="fas fa-users form-icon"),
                                Span(" Number of Visitors"),
                                For="num_visitors",
                                cls="form-label"
                            ),
                            Input(
                                type="number",
                                id="num_visitors",
                                name="num_visitors",
                                placeholder="How many people will be visiting?",
                                min="1",
                                max="10",
                                value="1",
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Purpose
                        Div(
                            Label(
                                I(cls="fas fa-compass form-icon"),
                                Span(" Purpose of Visit"),
                                For="purpose",
                                cls="form-label"
                            ),
                            Select(
                                Option("Select Purpose", value="", selected=True),
                                Option("Prospective Parent", value="parent"),
                                Option("Prospective Student", value="student"),
                                Option("Alumni", value="alumni"),
                                Option("General Inquiry", value="inquiry"),
                                Option("Other", value="other"),
                                id="purpose",
                                name="purpose",
                                cls="form-input"
                            ),
                            cls="form-group"
                        ),

                        # Special Requirements
                        Div(
                            Label(
                                I(cls="fas fa-comment-dots form-icon"),
                                Span(" Special Requirements / Notes"),
                                For="special_req",
                                cls="form-label"
                            ),
                            Textarea(
                                id="special_req",
                                name="special_req",
                                placeholder="Accessibility needs, specific areas of interest, etc...",
                                rows="3",
                                cls="form-input form-textarea"
                            ),
                            cls="form-group"
                        ),

                        # Submit Button
                        Button(
                            I(cls="fas fa-check-circle"),
                            Span(" Book Your Visit"),
                            type="submit",
                            cls="btn btn-primary form-submit"
                        ),

                        P(
                            "You will receive a confirmation email within 24 hours.",
                            cls="form-note"
                        ),

                        cls="contact-form",
                        method="POST",
                        action="#"
                    ),
                    cls="form-right"
                ),

                cls="form-content"
            ),
            cls="container"
        ),
        cls="form-section"
    )
