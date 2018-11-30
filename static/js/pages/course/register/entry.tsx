import React from 'react';
import ReactDOM from 'react-dom';

import RegisterView from './Register';

class Register {
    constructor() {
        const container = document.getElementById('test');
        if (container) {
            ReactDOM.render(<RegisterView />, container);
        }
    }
}
export default Register;