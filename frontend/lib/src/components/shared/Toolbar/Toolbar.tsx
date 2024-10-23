/**
 * Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React, { ReactElement } from "react"

import { EmotionIcon } from "@emotion-icons/emotion-icon"
import { useTheme } from "@emotion/react"
import { StyledComponent } from "@emotion/styled"
import { Fullscreen, FullscreenExit } from "@emotion-icons/material-outlined"

import StreamlitMarkdown from "@streamlit/lib/src/components/shared/StreamlitMarkdown"
import Tooltip, {
  Placement,
} from "@streamlit/lib/src/components/shared/Tooltip"
import Button, {
  BaseButtonKind,
} from "@streamlit/lib/src/components/shared/BaseButton"
import Icon from "@streamlit/lib/src/components/shared/Icon"
import { EmotionTheme } from "@streamlit/lib/src/theme"
import { ElementFullscreenContext } from "@streamlit/lib/src/components/shared/ElementFullscreen/ElementFullscreenContext"
import { useRequiredContext } from "@streamlit/lib/src/hooks/useRequiredContext"

import { StyledToolbar, StyledToolbarWrapper } from "./styled-components"

export interface ToolbarActionProps {
  label: string
  icon?: EmotionIcon
  show_label?: boolean
  onClick: () => void
}

export function ToolbarAction({
  label,
  show_label,
  icon,
  onClick,
}: ToolbarActionProps): ReactElement {
  const theme: EmotionTheme = useTheme()

  const displayLabel = show_label ? label : ""
  return (
    <div data-testid="stElementToolbarButton">
      <Tooltip
        content={
          <StreamlitMarkdown
            source={label}
            allowHTML={false}
            style={{ fontSize: theme.fontSizes.sm }}
          />
        }
        placement={Placement.TOP}
        // The default tooltip delay (== how fast the tooltip is triggered) of 200ms
        // is a bit too fast for the toolbar use case. Therefore, we are setting it to 1000ms.
        onMouseEnterDelay={1000}
        inline
      >
        <Button
          onClick={event => {
            if (onClick) {
              onClick()
            }
            event.stopPropagation()
          }}
          kind={BaseButtonKind.ELEMENT_TOOLBAR}
          aria-label={label}
        >
          {icon && (
            <Icon
              content={icon}
              size="md"
              testid="stElementToolbarButtonIcon"
            />
          )}
          {displayLabel && <span>{displayLabel}</span>}
        </Button>
      </Tooltip>
    </div>
  )
}

export interface ToolbarProps {
  onExpand?: () => void
  onCollapse?: () => void
  isFullScreen?: boolean
  locked?: boolean
  target?: StyledComponent<any, any, any>
  disableFullscreenMode?: boolean
}

const Toolbar: React.FC<React.PropsWithChildren<ToolbarProps>> = ({
  onExpand,
  onCollapse,
  isFullScreen,
  locked,
  children,
  target,
  disableFullscreenMode,
}): ReactElement => {
  const {
    expanded: isFullScreenDefault,
    expand,
    collapse,
  } = useRequiredContext(ElementFullscreenContext)

  const finalOnExpand = onExpand || expand
  const finalOnCollapse = onCollapse || collapse
  const finalIsFullScreen = isFullScreen ?? isFullScreenDefault

  return (
    <StyledToolbarWrapper
      className="stElementToolbar"
      data-testid="stElementToolbar"
      locked={locked || finalIsFullScreen}
      target={target}
    >
      <StyledToolbar>
        {children}
        {finalOnExpand && !disableFullscreenMode && !finalIsFullScreen && (
          <ToolbarAction
            label="Fullscreen"
            icon={Fullscreen}
            onClick={() => finalOnExpand()}
          />
        )}
        {finalOnCollapse && !disableFullscreenMode && finalIsFullScreen && (
          <ToolbarAction
            label="Close fullscreen"
            icon={FullscreenExit}
            onClick={() => finalOnCollapse()}
          />
        )}
      </StyledToolbar>
    </StyledToolbarWrapper>
  )
}

export default Toolbar
