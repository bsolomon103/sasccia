import React from 'react';
import {useRef, useEffect} from 'react';
import {AxisBottom} from './AxisBottom';
import {AxisLeft} from './AxisLeft';
import {Marks} from './Marks';
import {Dropdown} from './Dropdown';

import {csv, scaleLinear,scaleTime,max,timeFormat,extent,histogram,timeMonths,sum,brushX,select,event} from 'd3';


const attributes = [
    {value:'requests', label:'Requests'},
    {value:'assessments', label:'Assessments'},
    {value:'opened', label:'Opened Services'},
    {value:'closed',label:'Closed Services'},
    {value:'deaths', label:'Number Of Deaths'}
    ]

export const DateHistogram =({data,xValue,xAxisLabel, histogramValue, setHistogramValue}) => {
    const width = 1100;
    const height = 200;
    const margin = { top: 5, right: 30, bottom: 30, left: 90 };
    const xAxisLabelOffset = 50;
    const yAxisLabelOffset = 25;
    
    
    
    const yValue = d => d['count'];
    const yAxisLabel = 'Raw Count';
    
    const innerHeight = height - margin.top - margin.bottom - 50;
    const innerWidth = width - margin.left - margin.right;
    const xAxisTickFormat = timeFormat("%d/%m/%y");


  const xScale = scaleTime()
    .domain(extent(data,xValue))
    .range([0, innerWidth])
  	.nice();
  
 
  
  const [start, stop] = xScale.domain();
 
  
  const binnedData = histogram()
  .value(xValue)
  .domain(xScale.domain())
  .thresholds(timeMonths(start, stop))
  (data).map(array => ({y: sum(array, yValue),
                       x0:array.x0,
                       x1:array.x1}));
  
 
  
	const yScale = scaleLinear()
  	.domain([0, max(binnedData, d => d.y)])
  	.range([innerHeight,0]);


  
  return (
      <>
        <div className='dropdown'>
        <label for='y-select'>Filter By</label>
            <Dropdown
                options={attributes}
                id="y-select"
                selectedValue={histogramValue}
                onSelectedValueChange={setHistogramValue}
            />
        </div>
        <svg width={width} height={height}>
        <g transform={`translate(${margin.left},${margin.top+10})`}>
          
            <AxisBottom
              xScale={xScale}
              innerHeight={innerHeight}
              tickFormat={xAxisTickFormat}
              tickOffSet={3}
            />
              <text
              className="axis-label"
              textAnchor="middle"
              transform={`translate(${-yAxisLabelOffset} ${innerHeight/2}) rotate(-90)`}
              style={{fontSize:'12px'}}
            >
              {yAxisLabel}
            </text>
            <AxisLeft yScale={yScale} innerWidth={innerWidth} />
            <text
              className="axis-label"
              x={innerWidth / 2}
              y={innerHeight+25}
              textAnchor="middle"
              tickOffset={3}
              style={{fontSize:'12px'}}
            >
              {xAxisLabel}
            </text>
            <Marks
              binnedData={binnedData}
              xScale={xScale}
              yScale={yScale}
              tooltipFormat={d => d}
              circleRadius={3.5}
              innerHeight={innerHeight}
            />
          </g>
        </svg>
    </>
  )

}