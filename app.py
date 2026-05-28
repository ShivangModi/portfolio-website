import yaml
from flask import Flask, render_template


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    

app = Flask(__name__)

PROFILE = load_yaml("content/profile.yaml")
SKILLS = load_yaml("content/skills.yaml")
EXPERIENCE = load_yaml("content/experience.yaml")
PROJECTS = load_yaml("content/projects.yaml")
EDUCATION = load_yaml("content/education.yaml")
CERTIFICATES = load_yaml("content/certificates.yaml")

@app.route("/")
def home():

    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
        education=EDUCATION,
        certificates=CERTIFICATES
    )

if __name__ == "__main__":
    app.run(debug=True)