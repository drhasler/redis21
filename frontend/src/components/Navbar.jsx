import React, { useState, useEffect } from 'react';
import Search from './Search';

import './Navbar.css';

function Navbar() {
  return (
  <div className="Navbar">
    <div className="brand">
    <img src="/movify-sm.png" alt="logo"/>
    <div>Movify</div>
    </div>
    <Search/>
  </div>
  )
}

export default Navbar;
