from flask import render_template, redirect, url_for, session as ses, make_response, request
from Resumeaiogram.app.forms import LoginForm, Download
from Resumeaiogram.app import app
from Resumeaiogram.database.SQLAlchemy_connection import ResumeBot
import base64
from Resumeaiogram.database.SQLAlchemy_connection import session
import pdfkit


@app.route('/generate_pdf', methods=['GET', 'POST'])
def generate_pdf():
    if request.method == 'POST':
        right_tuple = ses['right_tuple']
        user = session.query(ResumeBot).filter_by(id=right_tuple["id"]).first()
        name_surname = user.name_surname
        phone_number = user.phone_number
        email = user.email
        education = user.education
        lang = user.lang
        lang_level = user.lang_level
        country = user.country
        city = user.city
        description = user.description
        profession = user.profession
        soft_skills = user.soft_skills
        tech_skills = user.tech_skills
        projects = user.projects
        how_long = user.how_long
        job_description = user.job_description
        past_work = user.past_work
        image = user.image
        photo_data = ''
        if image is not None:
            photo_data = base64.b64encode(image).decode('utf-8')
        html_content = render_template('download_file.html', profession=profession, name_surname=name_surname,
                                      phone_number=phone_number, email=email, education=education,
                                      tech_skills=tech_skills, soft_skills=soft_skills, projects=projects,
                                      lang=lang, lang_level=lang_level, country=country, city=city,
                                      past_work=past_work, how_long=how_long, job_description=job_description,
                                      description=description, photo_data=photo_data)

        pdf = pdfkit.from_string(html_content, False)
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "attachment; filename=Resume.pdf"
        return response

    else:
        # Обработка GET-запроса
        return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        result = []
        users = session.query(ResumeBot).all()
        for i in users:
            result.append(
                {
                "id": i.id,
                "password" : i.password,
                }
            )
        for data_tuple in result:
            if int(form.user_id.data) == int(data_tuple["id"]):
                if str(data_tuple["password"]) == str(form.password.data):
                    ses['right_tuple'] = data_tuple
                    return redirect(url_for('resume'))
                else:
                    error = 'Невірний логін або пароль'

    return render_template('login_form.html', form=form, error=error)


@app.route("/resume", methods=['GET', 'POST'])
def resume():
    form = Download()
    if 'right_tuple' not in ses:
        return redirect(url_for('login'))

    right_tuple = ses['right_tuple']
    user = session.query(ResumeBot).filter_by(id=right_tuple["id"]).first()
    name_surname = user.name_surname
    phone_number = user.phone_number
    email = user.email
    education = user.education
    lang = user.lang
    lang_level = user.lang_level
    country = user.country
    city = user.city
    description = user.description
    profession = user.profession
    soft_skills = user.soft_skills
    tech_skills = user.tech_skills
    projects = user.projects
    how_long = user.how_long
    job_description = user.job_description
    past_work = user.past_work
    image = user.image
    photo_data = ''
    if image is not None:
            photo_data = base64.b64encode(image).decode('utf-8')
    if form.validate_on_submit():
        ses['right_tuple'] = right_tuple
        return redirect(url_for('generate_pdf'))

    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,
                           email=email, education=education, tech_skills=tech_skills, soft_skills=soft_skills,
                           projects=projects, lang=lang, lang_level=lang_level, country=country, city=city,
                           past_work=past_work, how_long=how_long, job_description=job_description,
                           description=description, photo_data=photo_data, form=form)
