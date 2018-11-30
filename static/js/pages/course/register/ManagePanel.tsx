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
                M.toast({ html: '錯誤', classes: 'red' });
            });
    }

    render() {
        const studentList = this.props.studentList.map((student) => {
            return (
                <li key={student.pk} className="collection-item" style={{ padding: '20px'}}>
                    { student.name }
                    <button className="secondary-content btn-small student-add-button"
                        onClick={() => { this.onClick(student) }}
                    >移除</button>
                </li>
            );
        });

        return (
            <div className="col m6 s12">
                <ul className="collection with-header">
                    <li className="collection-item">
                        <h4>已經註冊的學生</h4>
                    </li>
                    { studentList.length == 0 ? '沒有學生': studentList }
                </ul>
            </div>
        )
    }
}