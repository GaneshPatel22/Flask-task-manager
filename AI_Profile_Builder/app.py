from flask import Flask, render_template, request, make_response

from utils.retriever import get_context
from utils.gemini import generate_profile

import markdown

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from io import BytesIO


app = Flask(__name__)

latest_profile = ""
latest_name = ""


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/generate", methods=["POST"])
def generate():

    global latest_profile
    global latest_name

    name = request.form["name"]

    retrieved = get_context(name)

    context = retrieved["context"]
    sources = retrieved["sources"]
    image = retrieved["image"]

    try:

        profile = generate_profile(
            name,
            context,
            sources
        )

    except Exception as e:

        profile = f"""

# {name}

## AI Error

{str(e)}

"""

    latest_profile = profile
    latest_name = name

    profile_html = markdown.markdown(
        profile,
        extensions=[
            "tables",
            "fenced_code"
        ]
    )

    return render_template(

        "profile.html",

        name=name,

        profile=profile_html,

        sources=sources,

        image=image

    )


@app.route("/download")
def download_pdf():

    global latest_profile
    global latest_name

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            latest_name,
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    for line in latest_profile.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            story.append(
                Spacer(1, 10)
            )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    response = make_response(pdf)

    response.headers["Content-Type"] = "application/pdf"

    response.headers["Content-Disposition"] = (
        f"attachment; filename={latest_name}.pdf"
    )

    return response


if __name__ == "__main__":

    app.run(
        debug=True
    )