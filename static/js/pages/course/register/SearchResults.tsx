import * as React from 'react';
import { Component } from 'react';
import M from 'materialize-css';

export default class SearchResults extends Component {
    constructor(props) {
        super(props);
        this.onClick = this.onClick.bind(this);
    }
    onClick(student) {
        const studentId = student.pk;
        const fetchAddResults = this.props.fetchManageStudentResults('add', studentId);
        fetchAddResults
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                if (data.status == 'success') {
                    this.props.addToList([student]);
                }
            })
            .catch((err) => {
                M.toast({ html: '錯誤', classes: 'red' });
            });
    }

    render() {
        const studentList = this.props.fetchedList.map((student) => {
            let button;
            if (this.props.studentList.some((stu) => (stu.pk == student.pk))) {
                button = (<button className="secondary-content btn-small student-add-button" disabled>
                    新增
                </button>
                );
            } else {
                button = (
                <button className="secondary-content btn-small student-add-button"
                    onClick={() => {this.onClick(student)}}
                >
                    新增
                </button>
                );
            }
            return (
                <div className="collection-item" key={student.pk}>
                    { student.name }
                    { button }
                </div>
            );
        });
        return (
            <div className="collection with-header" style={{ marginTop: '25px' }}>
                <h4 className="collection-header">搜尋結果</h4>
                <div id="results-container" style={{ padding: '5px' }}>
                    {studentList.length == 0 ? '沒有結果' : studentList }
                </div>
            </div>
        );
    }
}