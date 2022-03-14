import React from 'react';
export const Marks = ({
  binnedData,
  xScale,
  yScale,
  tooltipFormat,
  innerHeight
}) =>
      binnedData.map(d => (
      <g className='mark'>
        <rect
          x={xScale(d.x0)}
          y={yScale(d.y)}
          width={xScale(d.x1) - xScale(d.x0)}
          height={innerHeight - yScale(d.y)}
         
        >
          <title>{tooltipFormat(d.y)}</title>
        </rect>
      </g>
      ))