
from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    profile = None
    error = None

    if request.method == "POST":

        # Receive form data
        name = request.form.get("name", "").strip()
        bio = request.form.get("bio", "").strip()
        image_url = request.form.get("image_url", "").strip()
        job = request.form.get("job", "").strip()
        location = request.form.get("location", "").strip()

        # Check required fields
        if not name or not bio:
            error = "Please enter your name and bio."

        else:
            # Validate image URL if provided
            if image_url:
                parsed_url = urlparse(image_url)

                if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
                    error = "Please enter a valid image URL."

            # Create profile data
            if not error:
                profile = {
                    "name": name,
                    "bio": bio,
                    "image_url": image_url,
                    "job": job,
                    "location": location
                }

    return render_template(
        "index.html",
        profile=profile,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
