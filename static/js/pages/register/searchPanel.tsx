import * as React from 'react';
import { Component } from 'react';
import M from 'materialize-css';

import SearchResults from './SearchResults';

export default class SearchPanel extends Component {
    public state;
    constructor(props) {
        super(props);
        this.state = {
            studentList: [],
            studentId: '',
        }
        this.onChange = this.onChange.bind(this);
        this.onClick = this.onClick.bind(this);
    }

    onChange(event: Event) {
        const studentId: String = event.target.value;
        this.setState({ studentId });
    }

    onClick(event: Event) {
        event.preventDefault();
        const searchStudent = this.fetchSearchResults(this.state.studentId);
        searchStudent
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                if (data.status == 'success') {
                    const { student } = data;
                    this.setState({ studentList: [student]});
                } else {
                    M.toast({ html: data.message, classes: 'red' });
                }
            })
            .catch((err) => {
                M.toast({ html: '錯誤', classes: 'red' });
            });
    }

    fetchSearchResults(studentId: String) : Promise<Response>{
        const requestUrl = `/course/${this.props.courseId}/studentsearch?student=${studentId}`;
        const headers = new Headers();
        headers.append('Content-type', 'application/json');
        headers.append('Accept', 'application/json');

        const init = {
            method: 'GET',
            headers,
        };

        return fetch(requestUrl, init);
    }

    render() {
        return (
            <div className="col m6 s12">
                <input id="student-number" 
                type="text" 
                value={this.state.studentId} 
                placeholder="輸入學生編號" 
                onChange={this.onChange}
                />
                <button id="search" className="btn" onClick={this.onClick}>搜尋</button>
                <SearchResults 
                    fetchedList={this.state.studentList}
                    studentList={this.props.studentList}
                    addToList={this.props.addToList}
                    fetchManageStudentResults={this.props.fetchManageStudentResults}
                />
            </div>
        )
    }
}