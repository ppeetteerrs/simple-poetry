# Simple Pypackage

**A clean, automated setup for publishing simple Python packages to PyPI and Anaconda.**

![action](https://img.shields.io/github/workflow/status/ppeetteerrs/simple-pypackage/build?logo=githubactions&logoColor=white)
[![pypi](https://img.shields.io/pypi/v/simple-pypackage.svg)](https://pypi.python.org/pypi/simple-pypackage)
[![anaconda](https://img.shields.io/conda/vn/ppeetteerrs/simple-pypackage?logo=anaconda)](https://anaconda.org/ppeetteerrs/simple-pypackage)
![platform](https://img.shields.io/conda/pn/ppeetteerrs/simple-pypackage?label=platform&color=blueviolet)
[![codecov](https://img.shields.io/codecov/c/github/ppeetteerrs/simple-pypackage?label=codecov&logo=codecov)](https://app.codecov.io/gh/ppeetteerrs/simple-pypackage)
[![docs](https://img.shields.io/github/deployments/ppeetteerrs/simple-pypackage/github-pages?label=docs&logo=readthedocs)](https://ppeetteerrs.github.io/simple-pypackage)

# Setup

## Prepare GitHub Repo
1. Create new GitHub repository / fork this repository
2. Setup PyPI and Anaconda Credentials in repository secrets
   - `PYPI_USER`: PyPI username (use `__token__` for API key authentication)
   - `PYPI_PASSWORD`: PyPI password (use token including the `pypi-` prefix for API key authentication)
   - `ANACONDA_API_TOKEN`: Anaconda API token
3. **After first release**: Go to `Settings` and activate your GitHub Pages using the `gh-pages` branch

## Edit Files
- Rename `simple_pypackage` folder to your package name
- Replace all `simple-pypackage`, `simple_pypackage`, `ppeetteerrs` and `Peter Yuen` with your package name, package slug, username and author name in these files:
	- `.devcontainer.json`
	- `mkdocs.yaml`
	- `README.md`
	- `setup.py`
	- `.github/workflows/build.yaml`
	- `conda-recipe/meta.yaml`
	- `{project_name}/__init__.py`
- Change your minimum Python version in `setup.py`, `.github/workflows/build.yaml` and `.github/workflows/upload.yaml`

## GitHub Workflow
- On push / pull request to `main` branch:
	- Try to build PyPI and Conda packages
	- Run `pytest` and `codecov` on all OS types
- On release created:
	- Build and publish package to PyPI and Anaconda (version is automatically inferred from repo tag)
	- Update docs

## Docker Dev Container
- A `.devcontainer.json` with my favourite setup is included <3. Use `VSCode => Reopen in container` to use it if desired.

# Usage

## **Important Gotchas**
- Make sure all product dependencies are available on both `conda-forge` and `pypi`
- Repo version tags must be of the format `vX.Y.Z` with lowercase `v`
- If GitHub Actions are not triggering, check [here](https://www.githubstatus.com/) to make sure it is not because of an outrage.
- Upload to Codecov might fail if you commit your repository too fast after creation / if you have not logged in to Codecov via GitHub. Just re-run the GitHub action in that case.

## Things You Can Do
- **Conda Description**: Write a longer and better description for `conda-recipe/meta.yaml`.
- **Extra Branches**: Separate into `dev` or `feature` branches. You might want to add GitHub Action triggers to push / pull requests to those branches.
- **Tests**: Write tests in `pytest`. Other testing framework would require minor changes.
- **Documentation**: Write some nice documentation in the `docs` directory.
- **Improve setup.py**: You can add `description`, `package_data`, `classifiers` and `keywords` to your `setup.py`.