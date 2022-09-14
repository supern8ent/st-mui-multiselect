# Material UI Multiselect component for Streamlit

> Multiselect component for Streamlit using Material UI's tool.

### Installation

```
$ pip install st-mui-multiselect
```

### Usage

```
import streamlit as st
from st_mui_multiselect import st_mui_multiselect

options = ["Mayo", "Lettuce", "Pickles", "Tomatoes", "Onions", "Mushrooms", "Ketchup", "Jalapeños"]
selections = st_mui_multiselect(options, size=select_size)
st.markdown("You selected %s" % ", ".join(selections))
```

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

### Publish

```
$ poetry build
$ poetry publish
```
