import React from 'react'

import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

import './NavBar.css'

export const NavBar = () => {

    return (
        <Navbar bg="light" expand="lg">
            <div className="nav-bar">
                <Navbar.Brand href="#home">Mel Liow</Navbar.Brand>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="nav-items">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <NavDropdown title="Projects" id="basic-nav-dropdown">
                            <NavDropdown.Item href="#action/3.1">NLP</NavDropdown.Item>
                            <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </div>
        </Navbar>
    )


}