from flask import Flask, render_template, request

app = Flask(__name__)


def base_skin_metrics(seed: int = 0):
    return {
        "acne": min(100, 24 + seed),
        "pigmentation": min(100, 34 + seed // 2),
        "dryness": min(100, 40 + seed // 3),
        "score": max(0, min(100, 86 - seed // 2)),
        "future": "High pigmentation risk",
    }


@app.route("/")
def home():
    features = [
        {
            "title": "AI Skin Analysis",
            "text": "Instantly uncover what your skin really needs.",
        },
        {
            "title": "Future Prediction",
            "text": "Preview your skin's journey in 30 days or a year.",
        },
    ]
    return render_template("index.html", features=features)


@app.route("/scan", methods=["GET", "POST"])
def scan():
    result = None
    if request.method == "POST":
        image_name = request.form.get("image_name", "Uploaded Face")
        seed = sum(ord(ch) for ch in image_name) % 13
        result = base_skin_metrics(seed)
        result["image_name"] = image_name
    return render_template("scan.html", result=result)


@app.route("/dashboard")
def dashboard():
    metrics = base_skin_metrics(5)
    issues = [
        {"title": "Pigmentation", "level": "Moderate", "value": metrics["pigmentation"]},
        {"title": "Dryness", "level": "Mild", "value": metrics["dryness"]},
        {"title": "Acne", "level": "Low", "value": metrics["acne"]},
    ]
    recommendations = [
        "AM: Gentle cleanser + Vitamin C + SPF 50",
        "PM: Niacinamide + barrier repair moisturizer",
        "Weekly: Exfoliation once with hydration mask",
    ]
    progress = [
        {"label": "Hydration", "value": 78},
        {"label": "Tone Evenness", "value": 72},
        {"label": "Texture Smoothness", "value": 81},
    ]
    return render_template(
        "dashboard.html",
        metrics=metrics,
        issues=issues,
        recommendations=recommendations,
        progress=progress,
    )


@app.route("/prediction")
def prediction():
    timeline = {
        "now": {"glow": 62, "risk": "Current mild risk"},
        "30": {"glow": 74, "risk": "Manageable pigmentation spikes"},
        "365": {"glow": 82, "risk": "High pigmentation risk"},
    }
    return render_template("prediction.html", timeline=timeline)


@app.route("/passport")
def passport():
    profile = {
        "name": "Ananya Rao",
        "member_id": "BV-AI-3901",
        "plan": "Luxury Intelligence",
        "beauty_score": 88,
    }
    history = [
        {"date": "2026-03-18", "status": "Glow score improved by 5%"},
        {"date": "2026-02-20", "status": "Pigmentation stabilized"},
        {"date": "2026-01-25", "status": "Routine compliance 91%"},
        {"date": "2025-12-12", "status": "Initial AI skin onboarding"},
    ]
    return render_template("passport.html", profile=profile, history=history)


@app.route("/routine")
def routine():
    routine_data = {
        "morning": ["Cream Cleanser", "Vitamin C Serum", "Hydra Gel", "SPF 50 PA++++"],
        "night": ["Foam Cleanser", "Retinol Microdose", "Ceramide Cream", "Lip Recovery"],
    }
    products = [
        {"name": "Lumi-C Bright Serum", "type": "Serum"},
        {"name": "Velvet Cloud Moisturizer", "type": "Moisturizer"},
        {"name": "UV Silk Shield 50", "type": "Sunscreen"},
    ]
    return render_template("routine.html", routine=routine_data, products=products)


@app.route("/makeup")
def makeup():
    palettes = ["Rose Quartz", "Coral Luxe", "Mulberry Satin", "Nude Silk", "Berry Glow"]
    return render_template("makeup.html", palettes=palettes)


@app.route("/admin")
def admin():
    stats = [
        {"label": "Monthly Revenue", "value": "$82,400", "delta": "+18%"},
        {"label": "New Customers", "value": "1,248", "delta": "+11%"},
        {"label": "AI Scans", "value": "5,930", "delta": "+24%"},
    ]
    insights = [
        {"name": "Premium Facials", "value": 82},
        {"name": "AI Consultations", "value": 73},
        {"name": "Makeup Trials", "value": 66},
    ]
    return render_template("admin.html", stats=stats, insights=insights)


if __name__ == "__main__":
    app.run(debug=True)
