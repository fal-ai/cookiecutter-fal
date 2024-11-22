# {{ cookiecutter.project_name }}

## Environment variables
Create a `.env` file in the repository root directory and add environment variables as needed. They will be picked automatically in the Makefile.
```
FAL_KEY=
```

## Installing Dependencies and Initializing the Project
To install the required dependencies and initialize the project, run the following command in your terminal:

```bash
make init
```

## Running {{ cookiecutter.project_name }} with an Ephemeral Machine
To run {{ cookiecutter.project_name }} with an ephemeral GPU instance for testing the application, use the following command:

```bash
make run
```

## Deploying {{ cookiecutter.project_name }}
To deploy {{ cookiecutter.project_name }}, execute the following command:

```bash
make deploy
```

## Adding a remote git repository

```bash
git remote add origin <remote-git-url>
git push -u origin main
```
