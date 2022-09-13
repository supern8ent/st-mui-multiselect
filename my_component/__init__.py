import os
import streamlit.components.v1 as components

_SERVED = True if os.environ.get("ST_CG_SERVE", "0") == "1" else False

if _SERVED:
    # Development setup. From frontend run `npm run serve`
    _component_func = components.declare_component("my_component", url="http://localhost:3001")
else:
    # Normal setup. After editing frontend code remember to `npm run build`
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def my_component(options, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(options=options, key=key, default=[])

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# # Add some test code to play with the component while it's in development.
# # During development, we can run this just as we would any other Streamlit
# # app: `$ streamlit run my_component/__init__.py`
# if _SERVED:
#     import streamlit as st
#
#     st.subheader("Component with constant args")
#
#     # Create an instance of our component with a constant `name` arg, and
#     # print its output value.
#     num_clicks = my_component("World")
#     st.markdown("You've clicked %s times!" % int(num_clicks))
#
#     st.markdown("---")
#     st.subheader("Component with variable args")
#
#     # Create a second instance of our component whose `name` arg will vary
#     # based on a text_input widget.
#     #
#     # We use the special "key" argument to assign a fixed identity to this
#     # component instance. By default, when a component's arguments change,
#     # it is considered a new instance and will be re-mounted on the frontend
#     # and lose its current state. In this case, we want to vary the component's
#     # "name" argument without having it get recreated.
#     name_input = st.text_input("Enter a name", value="Streamlit")
#     num_clicks = my_component(name_input, key="foo")
#     st.markdown("You've clicked %s times!" % int(num_clicks))
