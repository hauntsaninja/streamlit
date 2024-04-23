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

"""Handle App logos"""

from __future__ import annotations

from streamlit.elements.image import AtomicImage, WidthBehaviour, image_to_url
from streamlit.proto.ForwardMsg_pb2 import ForwardMsg
from streamlit.runtime.scriptrunner import get_script_run_ctx


def logo(
    image: str | Image.Image | AtomicImage,
    *,  # keyword-only args:
    link: str | None = None,
    collapsed_image: str | None = None,
) -> None:
    """
    Handles the app and sidebar logos
    """
    ctx = get_script_run_ctx()
    if ctx is None:
        return

    fwd_msg = ForwardMsg()
    image_url = image_to_url(image, WidthBehaviour.AUTO, True, "RGB", "auto", "logo")

    fwd_msg.logo.image = image_url
    if link:
        fwd_msg.logo.link = link
    if collapsed_image:
        collapsed_image_url = image_to_url(
            collapsed_image,
            WidthBehaviour.AUTO,
            True,
            "RGB",
            "auto",
            "collapsed-logo",
        )
        fwd_msg.logo.collapsed_image = collapsed_image_url
    ctx.enqueue(fwd_msg)
