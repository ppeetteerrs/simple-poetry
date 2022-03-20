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