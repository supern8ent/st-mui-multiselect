import os

import streamlit.components.v1 as components

_SERVED = True if os.environ.get("ST_CG_SERVE", "0") == "1" else False

if _SERVED:
    # Development setup. From frontend run `npm run serve`
    _component_func = components.declare_component(
        "st_mui_multiselect", url="http://localhost:3001"
    )
else:
    # Normal setup. After editing frontend code remember to `npm run build`
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_mui_multiselect", path=build_dir)


def st_mui_multiselect(options, size=4, key=None):
    """Create a new instance of "st_mui_multiselect".

    Parameters
    ----------
    options: Iterable[str]
        The options to display in the multiselect
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    List[str]
        The options that the user has selected
    """
    component_value = _component_func(options=options, size=size, key=key, default=[])

    return component_value
