# Barebones copy of Streamlit's example

### Setup:
```
$ poetry install
$ cd my_component/frontend
$ npm install
```

### Run dev:  
You need to run *both* npm dev server for the JS component frontend as well as streamlit
```
$ cd my_component/frontend
$ npm run start
```
```
$ poetry run streamlit run app.py
```
