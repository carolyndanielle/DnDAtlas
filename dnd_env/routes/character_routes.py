from flask import render_template, request, redirect, url_for
from database.models import db, Character

# Route for creating a new character
@app.route('/create', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        name = request.form['name']
        character_class = request.form['class']
        if character_class == 'Warrior':
            strength, dexterity, intelligence = 15, 12, 8
        elif character_class == 'Wizard':
            strength, dexterity, intelligence = 8, 10, 18
        # Add more classes here
        new_character = Character(name=name, character_class=character_class, strength=strength, dexterity=dexterity, intelligence=intelligence)
        db.session.add(new_character)
        db.session.commit()
        return redirect(url_for('view_characters'))
    return render_template('create_character.html')

# Route to view all characters
@app.route('/characters')
def view_characters():
    characters = Character.query.all()
    return render_template('view_characters.html', characters=characters)
