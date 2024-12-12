# DnD Atlas

DnD Atlas is a web-based tool designed to simplify the character creation and management process for players of Dungeons & Dragons (D&D). This application allows users to create characters by selecting races, classes, and subclasses, with automatic stat updates and inventory management features. The goal of DnD Atlas is to streamline gameplay, making it easier for players and Dungeon Masters to focus on storytelling and strategy.

---

## Features

- **User Accounts**
  - Secure user authentication for personalized character storage.
- **Character Creation**
  - Step-by-step character creation process with race, class, and subclass options.
  - Automatic stat calculations based on level and selected features.
- **Inventory Management**
  - Add, edit, and remove inventory items for each character.
- **Quest Log**
  - Track completed quests and in-game actions.
- **History Page**
  - View a detailed log of all changes made to characters, including level-ups, inventory updates, and quest logs.
- **Responsive Design**
  - Intuitive interface designed for ease of navigation.

---

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Version Control**: GitHub
- **Tools**: Flask-WTF for forms, Flask-Login for authentication, Bootstrap for styling

---

## Installation and Setup

1. Clone this repository:

   - git clone <https://github.com/carolyndanielle/DnDAtlas>
   - cd DnD-Atlas

2. Set up a virtual environment:

    - python -m venv venv
    - source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:

    - pip install -r requirements.txt

4. Create the SQLite database:

    - flask db init
    - flask db migrate -m "Initial migration."
    - flask db upgrade

5. Run the development server:

    - flask run

6. Open your browser and navigate to:

<http://127.0.0.1:5000>

### File Structure

- app/
  - routes.py: Handles application routing and backend logic.
  - models.py: Defines database models for users, characters, and related entities.
  - forms.py: Manages web forms for user input.
- templates/
  - Contains all HTML files for rendering the frontend.
- static/
  - Contains CSS styles, images, and other static assets.
- config.py: Configuration file for Flask and database settings.
- run.py: Entry point for running the application.

### Collaborators
- Team Lead & Back-End Developer: [Carolyn Dickenson](https://github.com/carolyndanielle)
- Front-End Developer: [Patrick Sachleben](https://github.com/Patsax)
- Back-End Developer: [Christopher Bautista (Daniel)](https://github.com/dbautista2)
