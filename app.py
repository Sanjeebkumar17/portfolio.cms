from flask import Flask, render_template, request, redirect,session
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="mysecretkey"

app.config["UPLOAD_FOLDER"] = "static/uploads"

@app.route("/")
def home():
    skills = Skill.query.all()
    projects = Project.query.all()
    abouts = About.query.all()
    blogs = Blog.query.all()
    experiences = Experience.query.all()
    testimonials = Testimonial.query.all()
    services = Service.query.all()

    return render_template(
        "index.html",
        skills=skills,
        projects=projects,
        abouts=abouts,
        blogs=blogs,
        experiences=experiences,
        testimonials=testimonials,
        services=services
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(
            username=username,
            password=password
        ).first()

        if admin:
            session["admin"] = admin.username
            return redirect("/admin")

        return "Invalid Username or Password"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/login")

@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/login")
    skills = Skill.query.all()
    projects = Project.query.all()
    abouts = About.query.all()
    blogs = Blog.query.all()
    experiences = Experience.query.all()
    testimonials = Testimonial.query.all()
    services = Service.query.all()
    contacts = Contact.query.all()

    return render_template(
        "admin.html",
        skills=skills,
        projects=projects,
        abouts=abouts,
        blogs=blogs,
        experiences=experiences,
        testimonials=testimonials,
        services=services,
        contacts = contacts
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

@app.route("/add-blog-form", methods=["POST"])
def add_blog_form():
    title = request.form["title"]
    content = request.form["content"]

    blog = Blog(
        title=title,
        content=content
    )

    db.session.add(blog)
    db.session.commit()

    return redirect("/admin")

@app.route("/add-experience-form", methods=["POST"])
def add_experience_form():

    company = request.form["company"]
    role = request.form["role"]
    description = request.form["description"]

    experience = Experience(
        company=company,
        role=role,
        description=description
    )

    db.session.add(experience)
    db.session.commit()

    return redirect("/admin")

@app.route("/add-testimonial-form", methods=["POST"])
def add_testimonial_form():

    name = request.form["name"]
    feedback = request.form["feedback"]

    testimonial = Testimonial(
        name=name,
        feedback=feedback
    )

    db.session.add(testimonial)
    db.session.commit()

    return redirect("/admin")


@app.route("/add-service-form", methods=["POST"])
def add_service_form():

    title = request.form["title"]
    description = request.form["description"]

    service = Service(
        title=title,
        description=description
    )

    db.session.add(service)
    db.session.commit()

    return redirect("/admin")

    name = request.form["name"]
    feedback = request.form["feedback"]

    testimonial = Testimonial(
        name=name,
        feedback=feedback
    )

    db.session.add(testimonial)
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

@app.route("/delete-blog-ui/<int:id>")
def delete_blog_ui(id):
    blog = Blog.query.get(id)

    if blog:
        db.session.delete(blog)
        db.session.commit()

    return redirect("/admin")

@app.route("/delete-experience-ui/<int:id>")
def delete_experience_ui(id):
    experience = Experience.query.get(id)

    if experience:
        db.session.delete(experience)
        db.session.commit()

    return redirect("/admin")

@app.route('/edit-testimonial/<int:id>')
def edit_testimonial(id):
    testimonial = Testimonial.query.get(id)

    if testimonial:
        return render_template(
            'edit_testimonial.html',
            testimonial=testimonial
        )

    return "Testimonial not found"

@app.route('/edit-service/<int:id>')
def edit_service(id):
    service = Service.query.get(id)

    if service:
        return render_template(
            'edit_service.html',
            service=service
        )

    return "Service not found"

@app.route("/delete-testimonial-ui/<int:id>")
def delete_testimonial_ui(id):
    testimonial = Testimonial.query.get(id)

    if testimonial:
        db.session.delete(testimonial)
        db.session.commit()

    return redirect("/admin")

@app.route("/delete-service-ui/<int:id>")
def delete_service_ui(id):
    service = Service.query.get(id)

    if service:
        db.session.delete(service)
        db.session.commit()

    return redirect("/admin")

@app.route("/delete-contact-ui/<int:id>")
def delete_contact_ui(id):

    contact = Contact.query.get(id)

    if contact:
        db.session.delete(contact)
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

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(2000))

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    contact = Contact(
        name=name,
        email=email,
        message=message
    )

    db.session.add(contact)
    db.session.commit()

    return redirect("/")

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

@app.route('/edit-blog/<int:id>')
def edit_blog(id):
    blog = Blog.query.get(id)

    if blog:
        return render_template('edit_blog.html', blog=blog)

    return "Blog not found"

@app.route('/edit-experience/<int:id>')
def edit_experience(id):
    experience = Experience.query.get(id)

    if experience:
        return render_template('edit_experience.html', experience=experience)

    return "Experience not found"

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

@app.route('/update-blog-form/<int:id>', methods=['POST'])
def update_blog_form(id):
    blog = Blog.query.get(id)

    if blog:
        blog.title = request.form['title']
        blog.content = request.form['content']
        db.session.commit()

    return redirect('/admin')

@app.route('/update-experience-form/<int:id>', methods=['POST'])
def update_experience_form(id):
    experience = Experience.query.get(id)

    if experience:
        experience.company = request.form['company']
        experience.role = request.form['role']
        experience.description = request.form['description']

        db.session.commit()

    return redirect('/admin')
    
@app.route('/update-testimonial-form/<int:id>', methods=['POST'])
def update_testimonial_form(id):
    testimonial = Testimonial.query.get(id)

    if testimonial:
        testimonial.name = request.form['name']
        testimonial.feedback = request.form['feedback']

        db.session.commit()

    return redirect('/admin')

@app.route('/update-service-form/<int:id>', methods=['POST'])
def update_service_form(id):
    service = Service.query.get(id)

    if service:
        service.title = request.form['title']
        service.description = request.form['description']

        db.session.commit()

    return redirect('/admin')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)