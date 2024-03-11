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
import re

from playwright.sync_api import Page, expect


def test_audio_has_correct_properties(app: Page):
    audio_elements = app.get_by_test_id("stAudio")
    expect(audio_elements).to_have_count(3)

    expect(audio_elements.nth(0)).to_be_visible()
    expect(audio_elements.nth(0)).to_have_attribute("controls", "")
    expect(audio_elements.nth(0)).to_have_attribute("src", re.compile(r".*media.*wav"))


def test_audio_end_time(app: Page):
    audio_elements = app.get_by_test_id("stAudio")
    expect(audio_elements).to_have_count(3)

    expect(audio_elements.nth(1)).to_be_visible()

    audio_element = audio_elements.nth(1)
    audio_element.evaluate("e => e.play()")
    app.wait_for_timeout(5000)
    expect(audio_element).to_have_js_property("paused", True)
    assert int(audio_element.evaluate("e => e.currentTime")) == 13


def test_audio_end_time_loop(app: Page):
    audio_elements = app.get_by_test_id("stAudio")
    expect(audio_elements).to_have_count(3)

    expect(audio_elements.nth(2)).to_be_visible()

    audio_element = audio_elements.nth(2)
    audio_element.evaluate("e => e.play()")
    app.wait_for_timeout(6000)
    expect(audio_element).to_have_js_property("paused", False)
    assert 16 <= audio_element.evaluate("e => e.currentTime") <= 18
