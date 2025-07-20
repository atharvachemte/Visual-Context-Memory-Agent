from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from processor import extract_metadata
from classifier import classify_image
from rl_agent import RLAgent

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

UPLOAD_FOLDER = "input_images"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Keep uploaded metadata in-memory per session
uploaded_metadata = []

# Create new RLAgent WITHOUT loading saved Q-table to start fresh each run
class RLAgentSession(RLAgent):
    def __init__(self):
        self.q_table = {
            "Work-related": 0,
            "Personal/memory": 0,
            "Informational": 0,
            "Advertisement/Junk": 0
        }
agent = RLAgentSession()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            metadata = extract_metadata(filepath)
            metadata["filename"] = filename

            # Classify using RL agent
            category = classify_image(metadata, agent)
            metadata["category"] = category

            # Reward based on category
            reward = {
                "Work-related": 2,
                "Personal/memory": 1,
                "Informational": -1,
                "Advertisement/Junk": -2
            }.get(category, 0)
            metadata["reward"] = reward

            # Update RL agent
            agent.update(category, reward)

            # Add metadata to session list
            uploaded_metadata.append(metadata)

            # Generate charts using current session data
            category_counts = {}
            for data in uploaded_metadata:
                cat = data["category"]
                category_counts[cat] = category_counts.get(cat, 0) + 1

            generate_bar_chart(category_counts)
            generate_reward_chart(agent.q_table)

            return render_template("index.html", metadata=uploaded_metadata)

    # GET request, show empty page with zero charts
    zero_counts = {
        "Work-related": 0,
        "Personal/memory": 0,
        "Informational": 0,
        "Advertisement/Junk": 0
    }
    generate_bar_chart(zero_counts)
    generate_reward_chart(agent.q_table)
    return render_template("index.html", metadata=[])

def generate_bar_chart(category_counts):
    categories = ["Work-related", "Personal/memory", "Informational", "Advertisement/Junk"]
    counts = [category_counts.get(cat, 0) for cat in categories]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, counts, color='skyblue')
    plt.title("Image Count per Category")
    plt.ylabel("Count")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("static/bar_chart.png")
    plt.close()

def generate_reward_chart(q_table):
    categories = ["Work-related", "Personal/memory", "Informational", "Advertisement/Junk"]
    rewards = [q_table.get(cat, 0) for cat in categories]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, rewards, color='mediumseagreen')
    plt.xlabel("Category")
    plt.ylabel("Total Reward")
    plt.title("RL Agent Reward Chart")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("static/reward_chart.png")
    plt.close()

if __name__ == "__main__":
    # Create upload folder if not exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs("static", exist_ok=True)

    app.run(debug=True)
