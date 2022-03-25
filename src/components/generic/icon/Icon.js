import React from 'react'

import './Icon.css'


export const Icon = ({ is, src, alt, onClick }) => {


    return (
        <button
            type="button"
            className="theme-button"
            onClick={onClick}
        >
            <img src={src} alt={alt} className="icon">
                {children}
            </img>
        </button>
    )


}