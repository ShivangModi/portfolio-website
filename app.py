import yaml

from flask import Flask, render_template


app = Flask(__name__)

def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

@app.route("/")
def home():

    profile = load_yaml("content/profile.yaml")
    skills = load_yaml("content/skills.yaml")
    experience = load_yaml("content/experience.yaml")
    projects = load_yaml("content/projects.yaml")
    education = load_yaml("content/education.yaml")

    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        experience=experience,
        projects=projects,
        education=education
    )

if __name__ == "__main__":
    app.run(debug=True)