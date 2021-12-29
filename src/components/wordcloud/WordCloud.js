import React from "react"
import WordCloud from 'react-d3-cloud';

export const WordCloudWrapper = ({ data }) => {

  return (
    <div>
        <WordCloud data={data} width={200} height={200}/>
    </div>
  )
}

