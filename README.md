# Simple Poetry

**A clean, automated setup for publishing simple Python packages to PyPI using Poetry and GitHub Actions.**

![action](https://img.shields.io/github/workflow/status/ppeetteerrs/simple-poetry/build?logo=githubactions&logoColor=white)
[![pypi](https://img.shields.io/pypi/v/simple-poetry.svg)](https://pypi.python.org/pypi/simple-poetry)
[![codecov](https://img.shields.io/codecov/c/github/ppeetteerrs/simple-poetry?label=codecov&logo=codecov)](https://app.codecov.io/gh/ppeetteerrs/simple-poetry)
[![docs](https://img.shields.io/github/deployments/ppeetteerrs/simple-poetry/github-pages?label=docs&logo=readthedocs)](https://ppeetteerrs.github.io/simple-poetry)

## Setup

1. Prepare GitHub repo
	- Create new GitHub repository / fork this repository
	- Setup PyPI Credentials in repository secrets
		- `PYPI_TOKEN`: PyPI API token

2. Replace text in files
	- Rename `simple_poetry` folder to `<package_name>`
	- Replace all `simple_poetry` instance in files to `<package_name>`
	- Replace all `simple-poetry` instance in files to `<package-name>`
	- Replace all `3.8` instance in files to `<target-python-version>`
	- Replace `ppeetteerrs` with `<github_user_name`>

3. Enter Package Information
	- `pyproject.toml`: Project description, authors
	- `<package_name>/__init__.py`: Author and email
	- `README.md`: Customize it, change the name and description especially

4. Further Customizations
	- `mkdocs.yaml`: Edit theme and `mkdocstrings` preferences (Can also add sub-pages to API Reference etc.)
	- `.devcontainer.json`: Add preferred extensions / build configurations (e.g. use GPUs)
	- `Dockerfile`: Install necessary formatters / linters / packages for local testing
	- `docs/`: Write your documentation
	- `.github/workflows/push.yaml`: Remove the `tests::Run Tests` step if you need to run tests locally (e.g. if your tests require GPU). Keep the rest to upload Codecov.

5. Publish and Setup GitHub Pages
	- `commit` and `push` your changes
	- Create first release
	- Go to `Settings` and activate your GitHub Pages using the `gh-pages` branch