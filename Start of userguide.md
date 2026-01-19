Working with Claude Code
========================

This guide explains how to use Claude Code to accelerate development on the
New App. Claude Code is Anthropic's AI coding assistant that understands
your codebase through the ``CLAUDE.md`` file and integrates with GitHub for
issue tracking.

.. contents:: Table of Contents
   :local:
   :depth: 2

Why Claude Code?
----------------

Claude Code provides several advantages for this project:

- **Context awareness**: Reads ``CLAUDE.md`` to understand project architecture,
  commands, and conventions
- **GitHub integration**: Creates issues, comments on progress, and links commits
  automatically
- **Memory across sessions**: The ``CLAUDE.md`` file serves as persistent memory,
  ensuring consistent behaviour across sessions
- **Code exploration**: Quickly searches and understands large codebases

Setting Up Claude Code
----------------------

Installation
~~~~~~~~~~~~

1. Install Claude Code via npm:

   .. code-block:: bash

      npm install -g @anthropic-ai/claude-code

2. Authenticate with your Anthropic API key:

   .. code-block:: bash

      claude auth

3. Verify installation:

   .. code-block:: bash

      claude --version

Starting a Session
~~~~~~~~~~~~~~~~~~

Navigate to your project directory and start Claude Code:

.. code-block:: bash

   cd new-app
   claude

Claude Code automatically reads the ``CLAUDE.md`` file in the project root,
giving it full context about:

- Project architecture and file structure
- Commands for running, testing, and deploying
- GitHub workflow conventions
- Coding standards and practices

The CLAUDE.md File
------------------

The ``CLAUDE.md`` file is the heart of Claude Code's understanding of your
project. Think of it as a comprehensive onboarding document that you would
give to a new developer.

Structure Overview
~~~~~~~~~~~~~~~~~~

Our ``CLAUDE.md`` includes these key sections:

**Project Overview**
   High-level description of what the application does.

**Commands**
   All the commands needed to run, test, build, and deploy:

   .. code-block:: markdown

      ### Running the Application
      ```bash
      conda activate new-app
      set FLASK_APP=src/app/
      flask run
      ```

**Architecture**
   Detailed explanation of the codebase structure, data flow, and key modules.

**GitHub Workflow**
   Conventions for labels, milestones, issue management, and commit messages.

Updating CLAUDE.md
~~~~~~~~~~~~~~~~~~

Keep ``CLAUDE.md`` updated as the project evolves:

- Add new commands when you introduce build scripts or tools
- Update architecture sections when adding new modules
- Document new conventions as they are established

Example of adding a new section:

.. code-block:: markdown

   ### New Feature: Subject Profiles

   The Subject Discontiuning  module (`src/models/subject_disco.py`)
   provides predictions based on:
   - lasso regression
   - apriori
   - Gives Odds ratios

   Key functions:
   - `summarising_subject_data()`: Main entry point for prediction
   - `apply_lasso_model()`: Applies specific subject discontion 

GitHub Integration
------------------

Claude Code integrates deeply with GitHub for issue tracking and project
management.

Working with Issues
~~~~~~~~~~~~~~~~~~~

**Ask Claude to work on an issue:**

.. code-block:: text

   > Work on issue #2

Claude will:

1. Read the issue details from GitHub
2. Check for proper labels (adding them if missing)
3. Comment on the issue to indicate work has started
4. Make commits that reference the issue number
5. Add a summary comment when complete

**Create a new issue:**

.. code-block:: text

   > Create an issue for adding Excel export to producer reports

Claude will create a properly labelled issue following the project conventions
defined in ``CLAUDE.md``.

Commit Convention
~~~~~~~~~~~~~~~~~

All commits must reference an issue number. Claude enforces this automatically:

.. code-block:: bash

   # Claude generates commits like:
   git commit -m "Add Excel export for reports #2"
   git commit -m "Fix graphs #3"

If Claude doesn't know the issue number, it will ask before committing.

Label System
~~~~~~~~~~~~

Claude understands the project's label taxonomy:

**Type Labels:**
   - ``bug`` - Something isn't working
   - ``enhancement`` - New feature or request
   - ``documentation`` - Documentation improvements
   - ``tech-debt`` - Code quality, refactoring

**Priority Labels:**
   - ``P0-critical`` - Blocks release/pilot
   - ``P1-high`` - Important, not blocking
   - ``P2-medium`` - Should have
   - ``P3-low`` - Nice to have

**Component Labels:**
   - ``database`` - PostgreSQL, schema, queries
   - ``ui-ux`` - Flask templates, web interface
   - ``reports`` - Producer reports, exports
   - ``visualization`` - Maps, charts, data viz

Common Workflows
----------------

Feature Development
~~~~~~~~~~~~~~~~~~~

**Starting a new feature:**

.. code-block:: text

   > I want to add a dark mode toggle to the dashboard

Claude will:

1. Create a task list to track progress
2. Explore the codebase to understand existing patterns
3. Implement the feature following project conventions
4. Run tests and fix any issues
5. Create commits with proper issue references

**Example interaction:**

.. code-block:: text

   You: Add pagination to the compartments list view

   Claude: I'll help add pagination to the compartments list view. Let me first
   explore the current implementation.

   [Claude reads routes.py, templates, and related files]

   I've created a task list:
   1. Add pagination logic to routes.py
   2. Update the template with pagination controls
   3. Add CSS styling for pagination
   4. Test with large datasets

   Starting work on the first task...

Bug Fixing
~~~~~~~~~~

**Fixing a bug:**

.. code-block:: text

   > Fix issue #35 - maps not rendering correctly

Claude will:

1. Read the issue details and any comments
2. Explore the relevant code (mapping modules)
3. Identify the root cause
4. Implement and test the fix
5. Comment on the issue with what was done

Code Review and Refactoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Request a code review:**

.. code-block:: text

   > Review the subject calculation module for potential improvements

Claude will analyse the code and suggest improvements while respecting the
project's convention of avoiding over-engineering.

**Refactor existing code:**

.. code-block:: text

   > Refactor the data_wraggling.py to improve readability

Running Tests
~~~~~~~~~~~~~

**Run the test suite:**

.. code-block:: text

   > Run pytest and fix any failures

Claude knows the testing commands from ``CLAUDE.md``:

.. code-block:: bash

   pytest
   pytest --cov=src
   pytest --cov=src --cov-report=html

Documentation
~~~~~~~~~~~~~

**Update documentation:**

.. code-block:: text

   > Update the documentation for the geospatial matching feature

Claude will:

1. Edit the relevant RST files in ``docs/source/``
2. Build the documentation with ``make.bat html``
3. Ensure both source and built files are ready to commit

Best Practices
--------------

Be Specific
~~~~~~~~~~~

Good:

.. code-block:: text

   > Add error handling to the database connection in database_upload.py
   > when the PostgreSQL server is unreachable

Less helpful:

.. code-block:: text

   > Make the database better

Provide Context
~~~~~~~~~~~~~~~

When working on complex features, provide relevant context:

.. code-block:: text

   > The report should include:
   > - Subject data summary table
   > - Predictions per site/Country
   >

Reference Existing Code
~~~~~~~~~~~~~~~~~~~~~~~

Point Claude to relevant patterns:

.. code-block:: text

   > Create a new route for forecasting, following the same
   > pattern as the subject_disco route in routes.py

Let Claude Explore
~~~~~~~~~~~~~~~~~~

For complex tasks, let Claude explore the codebase first:

.. code-block:: text

   > Before implementing, explore how the mapping module works
   > and summarise the key functions

Task Management
~~~~~~~~~~~~~~~

Claude uses a todo list to track progress on complex tasks. You can see
the current tasks and their status during the session. This helps ensure
nothing is forgotten and gives you visibility into progress.

Troubleshooting
---------------

Claude Doesn't Know a Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If Claude uses the wrong command, the ``CLAUDE.md`` file may need updating.
Add the correct command:

.. code-block:: markdown

   ### New Command
   ```bash
   # Description of what this does
   new-command --with-flags
   ```

Context Getting Too Large
~~~~~~~~~~~~~~~~~~~~~~~~~

For very long sessions, Claude may lose track of earlier context. Start a
fresh session and reference the specific issue or files:

.. code-block:: text

   > Continue work on issue #4. The remaining task is to add unit tests
   > for the Excel export function in src/models/report_export.py

GitHub Authentication Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure the ``gh`` CLI is authenticated:

.. code-block:: bash

   gh auth status
   gh auth login  # if needed

Claude uses the ``gh`` CLI for all GitHub operations.

Database Connection Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

Claude will use the database configuration from ``.env``. Ensure the file
exists and contains valid credentials:

.. code-block:: bash

   DB_HOST=your-host
   DB_PORT=5432
   DB_NAME=new-app
   DB_USER=your-user
   DB_PASSWORD=your-password

Example Session
---------------

Here's a complete example of working with Claude Code:

.. code-block:: text

   $ cd new-app
   $ claude

   You: Work on issue #1 - starting

   Claude: I'll start working on issue #1. Let me first read the issue
   details and explore the relevant parts of the codebase.

   [Claude reads the issue, explores models/, routes.py, templates/]

   I've created a task list:
   1. Create subject_disco_model.py model
   2. Add route in routes.py
   3. Create template for the subject view
   4. Add navigation link in dashboard
   5. Test the feature end-to-end

   Commenting on issue #1: "Starting work on log model of subject disco"

   Starting with task 1...

   [Claude implements the feature, making commits like:]
   "Adding ability to scale numerical values #1"
   "Add route and template for subject disco html #1"

   [After completion:]

   Claude: I've completed all tasks for issue #1. Here's a summary:

   - Created src/models/subject_disco.py with subject calculations
   - Added /subject_disco route in routes.py
   - Created subject_disco.html template with results table
   - Added navigation link in dashboard
   - All tests passing

   Commenting on issue #1 with completion summary and closing the issue.

Further Resources
-----------------

- **CLAUDE.md**: The project's AI assistant configuration file
- **PRODUCT.md**: Product strategy and roadmap
- **GitHub Issues**: Track work at the project's GitHub repository
- `Claude Code Documentation <https://docs.anthropic.com/claude-code>`_:
  Official documentation from Anthropic