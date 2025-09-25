from flask import Flask, render_template, request, abort
from myimages import images

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", images=images[:12])


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


# @app.route("/details")
@app.route("/details/<imgid>")
def details(imgid):
    for image in images:
        if image.get("imgid") == imgid:
            return render_template("item_details.html", image=image)
    abort(404)


@app.route("/browseall")
def browseall():
    return render_template("vendor_gallery.html", images=images)


@app.route("/management")
def management():
    return render_template("vendor_management.html", images=images)


@app.route("/add_to_cart")
def add_to_cart():
    return render_template("checkout.html")


if __name__ == "__main__":
    app.run(debug=True)
