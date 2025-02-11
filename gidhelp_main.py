
# importing utilities and packages
from gidhelp import Gidhelp_75
from time import sleep 

import streamlit as st



# Model working
model = Gidhelp_75()                                                # creating model instance

# some preworking
st.cache_data.clear()
st.cache_resource.clear()
st.set_page_config("Gidhelp (Github Description Helper)", page_icon="📝")


# page layout
st.title("Gidhelp")
st.markdown("###### :orange[Gi]thub :orange[D]escription :orange[Help]er")


st.text("You can use this tool for writing your Github profile description, it may be helpful for you, for more details slide left top-bar")



details = """#### About the Model
- Gidhelp is a tool that helps us to write our Github profile description.
- It is based on next word predictor technique.
- It has several versions i.e., *Gidhelp_75*, *Gidhelp_500*, etc
- Currently there are available only one model *Gidhelp_75*
- More models will comming soon.
"""

#  Sidebar  
st.sidebar.title("Menu")
st.sidebar.divider()
words_limit = st.sidebar.slider(
    "Set suggestion word limit",
    min_value=1,
    max_value=10,
    step = 1,
    value=5
)
st.sidebar.markdown(details)
st.sidebar.write("You can check my social media accounts: ")
st.sidebar.write("[Website](https://a4archit.github.io/my-portfolio)")
st.sidebar.write("[Kaggle](https://www.kaggle.com/architty108)")
st.sidebar.write("[Github](https://www.github.com/a4archit)")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/archit-tyagi-191323296)")








# declaring functions
def clear_text():
    st.session_state.user_input_text = ""
    
def update_input_label():
    st.session_state.user_input_text = complete_text

# taking user input
user = st.text_area(
    "", 
    key="user_input_text",
    placeholder="Write something...",
    help="Write something about your Github profile."
)


# adding buttons
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.button("Clear", on_click=clear_text, use_container_width=True)

with col2:
    st.button("Update input label", on_click=update_input_label, use_container_width=True)

with col3:
    st.button("Help me now!", use_container_width=True)

st.divider()

space_for_output = st.empty()


predicted_text, complete_text, words_list = model.predict(user, prediction_words_length=words_limit)     # prediction from user text
# updating output text
if user != "":
    output_chars = ""
    for word_index, word in enumerate(words_list):
        for index, char in enumerate(word):
            if index == 0 and word_index != 0:
                output_chars += f" {char}"
            else:
                output_chars += f"{char}"

            space_for_output.markdown(f'<p style="font-size: 1.2em;background-color: #edebeb; padding: 30px; box-sizing:border-box; border-radius: 10px;"><b style="color: #000;">{user.capitalize().strip()}</b> <i style="color: #807d7d">{output_chars}</i> </p>', unsafe_allow_html=True)
            if word_index == 0 and index == 0:
                sleep(0.5)
            sleep(0.05)



