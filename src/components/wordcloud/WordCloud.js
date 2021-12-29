import React from "react"
import WordCloud from 'react-d3-cloud';

export const WordCloudWrapper = ({ data }) => {

  return (
    <>
      Word Cloud
        <WordCloud 
          data={data} 
          fontWeight="bold"
          fontSize={(word) => Math.log2(word.value) * 2}
          random={Math.random}
          width={250} 
          height={250}
          />
    </>
  )
}

