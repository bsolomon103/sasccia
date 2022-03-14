import React from "react";
import { line, curveNatural } from "d3";

export const Marks = ({
    data,
    xScaleScatter,
    yScaleScatter,
    xValueScatter,
    yValueScatter,
    circleRadius
    
}) => (
<g className='mark'>
  <>
  <path 
    d={
    line().x(d => xScaleScatter(xValueScatter(d)))
    .y(d => yScaleScatter(yValueScatter(d)))
    .curve(curveNatural)(data)
    }
  
  />
        {data.map(d => (
            <circle
                
                cx={xScaleScatter(xValueScatter(d))}
                cy={yScaleScatter(yValueScatter(d))}
                r={circleRadius}>
                
                <title>{yValueScatter(d)}</title>
            </circle>
            ))
        }
</>
</g>
   
    )