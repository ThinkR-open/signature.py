# Signature.py <img src="signature/assets/signature_hex.png" align="right" alt="Signature.py logo" style="height: 140px;"></a>

### Demo

Try the app at _todo_

### Try locally

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

### Modify the theme

This app uses Bootstrap `5.3.3`.

To modify the theme, edit the `signature/scss/signature.css` file.

To compile the SCSS to CSS, run:

```bash
sass scss/signature.scss css/signature.css
```

### How the redirection banner works?

The redirection banner is a JavaScript function that redirects the user to the specified URL.

To modify the redirection URL, edit the `index.html` file.

### Mockup

The mockup was created using [Figma](https://www.figma.com/).

Explore the mockup [here](https://www.figma.com/proto/u95KvEqgWLB8arxt7saZcJ/%7Bsignature%7D?node-id=705-5&t=xevegkmzONTrRyR3-8&scaling=contain&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=705%3A5&hide-ui=1)
