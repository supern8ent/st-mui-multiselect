# Material UI Multiselect component for Streamlit

## Development

### Setup

```
$ poetry install
$ cd st_mui_multiselect/frontend
$ npm install
```

### Run dev

You need to run *both* npm dev server for the JS component frontend as well as streamlit
```
$ cd st_mui_multiselect/frontend
$ npm run start
```
```
$ poetry run streamlit run app.py
```

### Tooling

Install pre-commit hooks:
```
$ poetry run pre-commit install
$ poetry run pre-commit install -t pre-push
```
