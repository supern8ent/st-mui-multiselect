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
selections = st_mui_multiselect(options, size=5)
st.markdown("You selected %s" % ", ".join(selections))
```

## Development

While developing the component, it can be served from npm. Once it's ready the component should be
built using npm.

The entrypoint for the component's typescript code is the `StMuiMultiselect` class. For more
background check out the following:
- [Streamlit - Components API Reference](https://docs.streamlit.io/library/components/components-api)
- [Streamlit - Create a Component](https://docs.streamlit.io/library/components/create)

### Prerequisites

- [Python 3.9](https://www.python.org)
- [Node.js 16](https://nodejs.org)
- [Poetry](https://python-poetry.org)

### Setup

```
$ poetry install
$ cd st_mui_multiselect/frontend
$ npm install
$ poetry run pre-commit install
$ poetry run pre-commit install -t pre-push
```

### Run dev

You need to run *both* npm dev server for the JS component frontend as well as streamlit
```
$ cd st_mui_multiselect/frontend
$ npm run start
```
```
$ ST_CG_SERVE=1 poetry run streamlit run demo_app.py
```
Setting environment variable `ST_CG_SERVE=1` tells the component to serve from npm.

### Build component

```
$ cd st_mui_multiselect/frontend
$ npm run build
```
To test the built component, run the demo app without setting the environment variable:
```
$ poetry run streamlit run demo_app.py
```

### Publish

```
$ poetry build
$ poetry publish
```
