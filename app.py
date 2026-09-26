from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/uploads"

@app.route("/")
def home():
    skills = Skill.query.all()
    projects = Project.query.all()

    return render_template(
        "index.html",
        skills=skills,
        projects=projects
    )

@app.route("/admin")
def admin():
    skills = Skill.query.all()
    projects = Project.query.all()
    abouts = About.query.all()

    return render_template(
        "admin.html",
        skills=skills,
        projects=projects,
        abouts=abouts
    )

@app.route("/add-skill-form", methods=["POST"])
def add_skill_form():
    skill_name = request.form["name"]

    skill = Skill(name=skill_name)
    db.session.add(skill)
    db.session.commit()

    return redirect("/admin")    

@app.route("/add-project-form", methods=["POST"])
def add_project_form():
    title = request.form["title"]
    description = request.form["description"]

    image = request.files["image"]

    filename = ""

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    project = Project(
        title=title,
        description=description,
        image=filename
    )

    db.session.add(project)
    db.session.commit()

    return redirect("/admin")

@app.route("/add-about-form", methods=["POST"])
def add_about_form():
    content = request.form["content"]

    about = About(content=content)

    db.session.add(about)
    db.session.commit()

    return redirect("/admin")

@app.route("/delete-skill-ui/<int:id>")
def delete_skill_ui(id):
    skill = Skill.query.get(id)

    if skill:
        db.session.delete(skill)
        db.session.commit()

    return redirect("/admin")


@app.route("/delete-project-ui/<int:id>")
def delete_project_ui(id):
    project = Project.query.get(id)

    if project:
        db.session.delete(project)
        db.session.commit()

    return redirect("/admin")
    if skill:
        db.session.delete(skill)
        db.session.commit()

    return redirect("/admin")

@app.route("/delete-about-ui/<int:id>")
def delete_about_ui(id):
    about = About.query.get(id)

    if about:
        db.session.delete(about)
        db.session.commit()

    return redirect("/admin")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db" 

db = SQLAlchemy(app)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    image = db.Column(db.String(200))

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(2000))

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200))
    role = db.Column(db.String(200))
    description = db.Column(db.String(1000))

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    feedback = db.Column(db.String(1000))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(1000))

@app.route("/projects")
def get_projects():
    projects = Project.query.all()

    result = []

    for project in projects:
        result.append({
            "id": project.id,
            "title": project.title,
            "description": project.description
        })
    return result 

@app.route("/about")
def get_about():
    abouts = About.query.all()

    result = []

    for about in abouts:
        result.append({
            "id": about.id,
            "content": about.content
        })

    return result

@app.route("/skills")
def get_skills():
    skills = Skill.query.all() 
    result = []
    for skill in skills:
        result.append({
            "id": skill.id,
            "name": skill.name
        })

    return result

@app.route("/add-skill", methods=["POST"])
def add_skill():
    data = request.get_json()

    skill = Skill(name=data["name"])
    db.session.add(skill)
    db.session.commit()

    return {"message": "skill added successfully"}


@app.route("/add-project", methods=["POST"])
def add_project():
    data = request.get_json()

    project = Project(
        title=data["title"],
        description=data["description"]
    )

    db.session.add(project)
    db.session.commit()

    return {"message": "project added successfully"}
    
@app.route('/delete-skill/<int:id>', methods=['DELETE'])
def delete_skill(id):
    skill = Skill.query.get(id)

    if skill is None:
        return {"message": "Skill not found"}, 404

    db.session.delete(skill)
    db.session.commit()

    return {"message": "Skill deleted successfully"}

@app.route("/delete-project/<int:id>", methods=["DELETE"])
def delete_project(id):
    project = Project.query.get(id)

    if not project:
        return {"message": "Project not found"}, 404

    db.session.delete(project)
    db.session.commit()

    return {"message": "Project deleted successfully"}    

@app.route("/update-project/<int:id>", methods=["PUT"])
def update_project(id):
    project = Project.query.get(id)

    if not project:
        return {"message": "Project not found"}, 404

    data = request.get_json()

    project.title = data["title"]
    project.description = data["description"]

    db.session.commit()

    return {"message": "Project updated successfully"}

@app.route('/update-skill/<int:id>', methods=['PUT'])
def update_skill(id):
    skill = Skill.query.get(id)

    if skill is None:
        return {"message": "Skill not found"}, 404

    data = request.get_json()
    skill.name = data["name"]

    db.session.commit()

    return {"message": "Skill updated successfully"}


@app.route('/edit-skill/<int:id>')
def edit_skill(id):
    skill = Skill.query.get(id)

    if skill:
        return render_template('edit_skill.html', skill=skill)

    return "Skill not found"


@app.route('/update-skill-form/<int:id>', methods=['POST'])
def update_skill_form(id):
    skill = Skill.query.get(id)

    if skill:
        skill.name = request.form['name']
        db.session.commit()

    return redirect('/admin')

@app.route('/edit-about/<int:id>')
def edit_about(id):
    about = About.query.get(id)

    if about:
        return render_template('edit_about.html', about=about)

    return "About not found"

@app.route('/edit-project/<int:id>')
def edit_project(id):
    project = Project.query.get(id)

    if project:
        return render_template('edit_project.html', project=project)

    return "Project not found"

@app.route('/update-about-form/<int:id>', methods=['POST'])
def update_about_form(id):
    about = About.query.get(id)

    if about:
        about.content = request.form['content']
        db.session.commit()

    return redirect('/admin')

@app.route('/update-project-form/<int:id>', methods=['POST'])
def update_project_form(id):
    project = Project.query.get(id)

    if project:
        project.title = request.form['title']
        project.description = request.form['description']
        db.session.commit()

    return redirect('/admin')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)