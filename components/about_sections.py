"""
About page sections components
"""
from fasthtml.common import Section, Div, H2, H3, H4, P, A, Img, Span

def PrincipalMessageSection():
    """
    Principal message section with image on left and message on right
    """
    return Section(
        Div(
            Div(
                # Principal image on left
                Div(
                    Img(src="/static/images/about/principalimage.png", alt="Principal Ajay Kumar Bansal", cls="principal-img"),
                    cls="principal-left"
                ),

                # Message content on right
                Div(
                    H2("Message from the Principal", cls="principal-heading"),
                    P(
                        "It gives me immense pleasure to welcome you to Sandipani VidhyaPeeth, where we believe in transformative learning that moulds future leaders. Our institution stands as a beacon of excellence in education, combining time-honored traditions with modern pedagogical approaches.",
                        cls="principal-text"
                    ),
                    P(
                        "At Sandipani VidhyaPeeth, we are committed to nurturing not just academic brilliance, but also character, creativity, and critical thinking. Our holistic approach ensures that every student discovers their unique potential and develops the skills necessary to thrive in an ever-changing world.",
                        cls="principal-text"
                    ),
                    P(
                        "Ajay Kumar Bansal",
                        cls="principal-name"
                    ),
                    P(
                        "Principal, Sandipani VidhyaPeeth",
                        cls="principal-title"
                    ),
                    cls="principal-right"
                ),

                cls="principal-content"
            ),
            cls="container"
        ),
        cls="principal-section"
    )

def CommunitySection():
    """
    Community section with image on left and action cards on right
    """
    return Section(
        Div(
            # Section heading
            H2("A Community Where Students Shape Their Journey", cls="community-title"),

            # Content grid
            Div(
                # Left side - Image with hover text
                Div(
                    Div(
                        Img(src="/static/images/about/about_sandipani_1.jpg", alt="Our Community", cls="community-img-default"),
                        cls="community-img-container"
                    ),
                    Div(
                        P(
                            "Sandipani VidhyaPeeth is a premier educational institution dedicated to nurturing young minds through innovative teaching methods and holistic development. We believe in empowering students to shape their own educational journey.",
                            cls="community-description-hover"
                        ),
                        cls="community-img-hover"
                    ),
                    cls="community-left"
                ),

                # Right side - Three action cards with hover effects like home page
                Div(
                    # Visit card (first)
                    Div(
                        Div(
                            Img(src="/static/images/home/school.png", alt="Visit", cls="community-card-icon"),
                            H3("Visit", cls="community-card-title"),
                            cls="community-card-default"
                        ),
                        Div(
                            Img(src="/static/images/home/school.png", alt="Visit", cls="community-card-icon"),
                            H3("Schedule a visit", cls="community-card-title-hover"),
                            A("SCHEDULE", href="/contact", cls="community-card-btn"),
                            cls="community-card-hover"
                        ),
                        cls="community-card"
                    ),
                    # Learn More card (second)
                    Div(
                        Div(
                            Img(src="/static/images/home/learn_more.png", alt="Learn More", cls="community-card-icon"),
                            H3("Learn More", cls="community-card-title"),
                            cls="community-card-default"
                        ),
                        Div(
                            Img(src="/static/images/home/learn_more.png", alt="Learn More", cls="community-card-icon"),
                            H3("We look forward to connect with you!", cls="community-card-title-hover"),
                            A("LEARN MORE", href="/academics", cls="community-card-btn"),
                            cls="community-card-hover"
                        ),
                        cls="community-card"
                    ),
                    # Apply card (third)
                    Div(
                        Div(
                            Img(src="/static/images/home/apply.png", alt="Apply", cls="community-card-icon"),
                            H3("Apply", cls="community-card-title"),
                            cls="community-card-default"
                        ),
                        Div(
                            Img(src="/static/images/home/apply.png", alt="Apply", cls="community-card-icon"),
                            H3("Learn more about application process", cls="community-card-title-hover"),
                            A("APPLY NOW", href="/admissions", cls="community-card-btn"),
                            cls="community-card-hover"
                        ),
                        cls="community-card"
                    ),
                    cls="community-cards"
                ),

                cls="community-content"
            ),
            cls="container"
        ),
        cls="community-section"
    )

def StatisticsSection():
    """
    Statistics section showing key numbers and achievements
    """
    return Section(
        Div(
            # Section label
            P("At a Glance", cls="stats-label"),

            # Section heading
            H2("Sandipani VidhyaPeeth By the Numbers", cls="stats-title"),

            # Section subtitle
            P(
                "We have numbers that push us to give our best and make sure we provide the best educational experience for our students.",
                cls="stats-subtitle"
            ),

            # Statistics grid (3x2)
            Div(
                # Stat 1
                Div(
                    H3("25+", cls="stat-number"),
                    P("Years of Excellence", cls="stat-label"),
                    cls="stat-card"
                ),
                # Stat 2
                Div(
                    H3("50", cls="stat-number"),
                    P("Acres Campus", cls="stat-label"),
                    cls="stat-card"
                ),
                # Stat 3
                Div(
                    H3("15+", cls="stat-number"),
                    P("Sports & Activities", cls="stat-label"),
                    cls="stat-card"
                ),
                # Stat 4
                Div(
                    H3("500+", cls="stat-number"),
                    P("Students", cls="stat-label"),
                    cls="stat-card"
                ),
                # Stat 5
                Div(
                    H3("60+", cls="stat-number"),
                    P("Expert Faculty", cls="stat-label"),
                    cls="stat-card"
                ),
                # Stat 6
                Div(
                    H3("12+", cls="stat-number"),
                    P("Academic Programs", cls="stat-label"),
                    cls="stat-card"
                ),
                cls="stats-grid"
            ),
            cls="container"
        ),
        cls="statistics-section"
    )
