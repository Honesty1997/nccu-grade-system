import * as React from 'react';
import { Component } from 'react';
import M from 'materialize-css';
import $ from 'jquery';


export default class ManagePanel extends Component {
    constructor(props) {
        super(props);
        this.onClick = this.onClick.bind(this);
    }

    onClick(student) {
        const studentId = student.pk;
        const fetchRemoveResults = this.props.fetchManageStudentResults('delete', studentId);
        fetchRemoveResults
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                if (data.status == 'success') {
                    this.props.removeFromList([student]);
                }
            })
            .catch((err) => {
                M.toast({ html: 'error', classes: 'red' });
            });
    }

    render() {
        const studentList = this.props.studentList.map((student) => {
            return (
                <li key={student.pk} className="collection-item" style={{ padding: '20px'}}>
                    { student.name }
                    <button className="secondary-content btn-small student-add-button"
                        onClick={() => { this.onClick(student) }}
                    >remove</button>
                </li>
            );
        });

        return (
            <div className="col m6 s12">
                <ul className="collection with-header">
                    <li className="collection-item">
                        <h4>Registered Students</h4>
                    </li>
                    { studentList }
                </ul>
            </div>
        )
    }
}