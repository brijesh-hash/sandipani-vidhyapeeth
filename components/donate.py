"""
Donate page components
"""
from fasthtml.common import Section, Div, H1, H2, H3, P, Span, Form, Input, Label, Button, Img

def DonateHero():
    """
    Hero section for Donate page
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
                    "Support ",
                    Span("Our Mission", cls="gradient-text"),
                    cls="hero-title"
                ),
                P("Your contribution helps us provide quality education to students", cls="hero-subtitle about-subtitle"),
                cls="hero-content"
            ),
            cls="container"
        ),
        cls="about-hero"
    )

def DonateForm():
    """
    Donate form section with QR code and form
    """
    return Section(
        Div(
            # Two column layout (1/2 and 1/2)
            Div(
                # Left side (1/2) - QR Code
                Div(
                    H2("Scan & Donate", cls="donate-qr-title"),
                    P(
                        "Scan the QR code below to make a donation via UPI. After payment, please submit the receipt through the form.",
                        cls="donate-qr-description"
                    ),
                    Div(
                        Img(src="/static/images/donate/qr_code.png", alt="Donation QR Code", cls="qr-code-image"),
                        cls="qr-code-wrapper"
                    ),
                    Div(
                        P("✓ Scan QR code using any UPI app", cls="donate-step"),
                        P("✓ Complete the payment", cls="donate-step"),
                        P("✓ Take a screenshot of payment confirmation", cls="donate-step"),
                        P("✓ Upload the screenshot in the form", cls="donate-step"),
                        cls="donate-steps"
                    ),
                    cls="donate-left"
                ),

                # Right side (1/2) - Form
                Div(
                    H3("Submit Payment Details", cls="donate-form-title"),
                    Form(
                        Input(
                            type="text",
                            id="donor_name",
                            name="donor_name",
                            placeholder="Full Name *",
                            required=True,
                            cls="form-input-pill"
                        ),
                        Input(
                            type="email",
                            id="donor_email",
                            name="donor_email",
                            placeholder="Email Address (Optional)",
                            cls="form-input-pill"
                        ),
                        Input(
                            type="tel",
                            id="donor_phone",
                            name="donor_phone",
                            placeholder="Phone Number *",
                            required=True,
                            cls="form-input-pill"
                        ),
                        Input(
                            type="text",
                            id="donor_address",
                            name="donor_address",
                            placeholder="Address *",
                            required=True,
                            cls="form-input-pill"
                        ),
                        Div(
                            Label("Upload Payment Receipt *", cls="upload-label"),
                            Div(
                                Label(
                                    "Choose File",
                                    For="receipt",
                                    cls="file-upload-btn"
                                ),
                                Span("No file chosen", cls="file-name", id="file-name"),
                                Input(
                                    type="file",
                                    id="receipt",
                                    name="receipt",
                                    accept="image/*",
                                    required=True,
                                    cls="file-input-hidden",
                                    onchange="document.getElementById('file-name').textContent = this.files[0] ? this.files[0].name : 'No file chosen'"
                                ),
                                cls="file-upload-wrapper"
                            ),
                            cls="upload-group"
                        ),
                        Button(
                            "Submit Receipt",
                            type="submit",
                            cls="btn btn-primary form-submit-pill"
                        ),
                        cls="donate-form",
                        method="POST",
                        action="#",
                        enctype="multipart/form-data"
                    ),
                    cls="donate-right"
                ),

                cls="donate-content"
            ),
            cls="container"
        ),
        cls="form-section"
    )
