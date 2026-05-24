# AGENTIC.md

## 1. Tools Used

- **Claude (claude.ai):** Used as the main assistant throughout the development. I used it to debug errors, understand Flask and SQLAlchemy concepts, deal with problems when using MySQL Workbench for the first time, and to style the page in the final stages so it wouldn't look too plain.

## 2. My Approach

I did not ask Claude to generate the entire project. Instead, I first built the page step by step as if it were a simple blog, with the help of some tutorials. This "skeleton" already included features like login, logout, user registration, storage tables for both users and data, post editing and deletion, and login-based restrictions.
During that process I used Claude a few times to fix errors that came up, though most of them were caused by missing symbols or inconsistent capitalization in variable names.
Where Claude was truly helpful was when adding new features to the page, such as the ability to upload images, better post visualization, and other small details.

## 3. Key Prompts

**Prompt 1 — Flask application context error:**
- What I asked: How to fix the `Working outside of application context` error
- What it generated: Wrapping `db.create_all()` inside `with app.app_context()`
- I used it as-is because I understood that Flask needs an active context to access the database. Claude explained that Flask manages an "application context" that holds information about the current app, and that operations like database access can only happen inside that context. Without `with app.app_context()`, Flask does not know which application the operation belongs to.

**Prompt 2 — Environment variables:**
- What I asked: How to implement environment variables in Flask using python-dotenv
- What it generated: The configuration using `os.getenv()` and the `.env` file
- I modified the result to fit the structure I already had in `config.py`. Originally I had the database credentials and secret key written directly in the code. While reading the project requirements I noticed this was explicitly discouraged, so I turned to Claude for help. The solution was to create a `.env` file that lives only on my computer and is never uploaded to the repository, and to use `os.getenv()` to read those values from the code. I then adapted Claude's solution to work with my existing classes — `config`, `developmentconfig`, and `productionconfig` — without breaking what I already had.

**Prompt 3 — Adoption check system:**
- What I asked: How to implement a system where only one user can mark a post and can also unmark it
- What it generated: The `Adopcion` table, the `adoptar` route, and the template logic
- I reviewed and fixed several errors in the generated code before using it. At first, the code had indentation problems inside the `adoptar` function — the logic that should have been inside the function was placed outside of it, which made no sense. After rewriting it correctly, there was still the `Post` vs `post` issue, where the lowercase version was used instead of the uppercase one in `db.session.get()`, causing it to reference the Blueprint instead of the model. The same happened with the HTTP methods, where `"post"` was written instead of `"POST"`. These were some of the most recurring errors when asking Claude for help, so I ended up always reviewing the generated code twice before applying it.

## 4. Critical Evaluation

**Code evaluated: `login()` function in `views/user.py`**

- What it got right: The general login logic was well structured — using `check_password_hash` to verify the password, managing the session with `session["user_id"]`, and redirecting to the index on successful login.

- What was wrong: The initially generated code had an unnecessary line that created a `User` object before querying the database, which made no sense since that object was immediately overwritten. It also compared `username == None` instead of `user is None` — an important difference because `username` is the text from the form and is never None if the user types something, while `user` is the result of the database query and can be None if the user does not exist.

- How I verified it: I manually tested three cases — logging in with a non-existent user, with an incorrect password, and with correct credentials. I verified that each case returned the correct error message and the appropriate HTTP status code (401 for errors, 302 for successful login).

- Bug found: The generated code used `user` as a variable name for both the Blueprint and the query result, causing an `AttributeError` because Python was referencing the Blueprint instead of the model when trying to run the query. I had to rename the variables to resolve the conflict.

## 5. What I Learned

This project was my first real experience with backend web development. Before starting it I had no experience with Flask, SQLAlchemy, or MySQL on my own — I had worked on university projects that used these technologies, but tasks were always divided among teammates and I rarely had to deal with these parts directly.

These are the most important concepts I learned:

- **Flask and its structure:** I learned how a web framework works — how routes are defined, how Flask receives HTTP requests and returns responses, and how to organize code into Blueprints to separate concerns.

- **Application context:** I did not know that Flask manages an application context and that operations like database access can only happen inside it. This was one of the first errors I had to understand deeply.

- **SQLAlchemy and databases:** I learned to define models as Python classes, create relationships between tables using ForeignKey, and run queries with `filter_by`, `paginate`, and `session.get`. Before this project I had never worked with a database directly from code.

- **MySQL and MySQL Workbench:** I learned to install and configure MySQL Server, create databases, and use Workbench to visualize tables and run queries directly.

- **Environment variables:** I understood why hardcoding credentials in code is a bad practice and how to use `python-dotenv` to manage them securely and avoid larger-scale problems.

- **Git and GitHub:** I already had some knowledge of Git from university projects, but this exercise helped me strengthen my workflow and learn more about what professional project documentation should look like.

- **Testing with pytest:** I learned to write automated tests to verify that routes work correctly, including the use of fixtures to create a test client with an in-memory database.