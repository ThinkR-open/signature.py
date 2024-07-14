# Signature.py <img src="signature/assets/signature_hex.png" align="right" alt="Signature.py logo" style="height: 140px;"></a>

## Demo

Try the app at _todo_

## Try locally

1. Clone the repository

2. Install [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx)

3. Install [poetry](https://python-poetry.org/docs/)

4. Navigate to the project directory and install the dependencies

```bash
poetry install
```

5. Activate the virtual environment

```bash
poetry shell
```

6. Run the app

```bash
shiny run --reload signature/app.py
```

## Modify the theme

This app uses Bootstrap `5.3.3`.

To modify the theme, edit the `signature/scss/signature.css` file.

To compile the SCSS to CSS, run:

```bash
sass scss/signature.scss css/signature.css
```
