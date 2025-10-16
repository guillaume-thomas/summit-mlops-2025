# {{cookiecutter.repo_name}}

{{ cookiecutter.project_description }}

Generate with python version {{ cookiecutter.python_version }}.

uv is used to manage the python environment. So please, install uv if you don't have it already:

```bash
pip install uv
```

To install all dependencies, run:

```bash
uv sync --all-groups
```

To run the example hello world application, run:

```bash
uv run hello
```





