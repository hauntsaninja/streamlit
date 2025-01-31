# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

st.header("Page 5")

if "test_value" not in st.session_state:
    st.session_state.test_value = False


def handle_change():
    st.session_state.test_value = True


st.checkbox("Checkbox 1", on_change=handle_change)
st.checkbox("Checkbox 2")

st.write("test_value: ", st.session_state.test_value)
