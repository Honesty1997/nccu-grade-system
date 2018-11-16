import * as React from 'react';
import { Component } from 'react';
import ReactDOM from 'react-dom';
import M from 'materialize-css';
import $ from 'jquery';

import getCSRFToken from '../../utils/getCSRFToken';

import SearchPanel from './SearchPanel';
import ManagePanel from './ManagePanel';

const courseId = $("#course-pk").data('id');

class Register extends Component {
    constructor(props) {
        super(props);
        this.state = {
            studentList: [],
        };
        this.fetchManageStudentResults = this.fetchManageStudentResults.bind(this);
        this.addToList = this.addToList.bind(this);
        this.removeFromList = this.removeFromList.bind(this);
    }

    componentDidMount(){
        const fetchStudentList = this.fetchStudentList();
        fetchStudentList
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                this.setState({ studentList: data.studentList });
            })
            .catch((err) => {
                M.toast({ html: '錯誤', classes: 'red' });
            });
    }

    /**
     * 
     * @param {Array<Student>} students List of students which need to be registered to
     *  the course. 
     */
    addToList(students) {
        const { studentList } = this.state;
        for(let student of students) {
            studentList.push(student);
        }
        this.setState({ studentList });
    }

    /**
     * 
     * @param {Array<Student>} students List of students which need to be removed.
     */
    removeFromList(students) {
        const { studentList } = this.state;
        let newStudentList = studentList.filter((student) => (!students.includes(student)));
        this.setState({ studentList: newStudentList});
    }

    /**
     * 
     * @param {String} type Specify the type of method "add" or "delete"
     * @param {String} studentId The student's id.
     * @return {Promise<Response>}
     */
    fetchManageStudentResults(type: String, studentId: String) : Promise<Response>{
        const requestUrl = `/course/${courseId}/student`;
        const method = type === 'add' ? 'POST' : 'DELETE';
        const csrfToken = getCSRFToken();
        const headers = new Headers();
        headers.append('Content-type', 'application/json');
        headers.append('Accept', 'application/json');
        headers.set('X-CSRFToken', csrfToken);

        const body = JSON.stringify({
            student: studentId,
        });

        const init = {
            method,
            headers,
            body,
        };

        return fetch(requestUrl, init);
    }

    /**
     * Initialize the component's student list.
     * @return {Promise<Response>}
     */
    fetchStudentList(): Promise<Response> {
        const requestUrl = `/course/${courseId}/student`;
        const method = 'GET';
        const headers = new Headers();
        headers.append('Content-type', 'application/json');
        headers.append('Accept', 'application/json');
        
        const init = {
            method,
            headers,
        };

        return fetch(requestUrl, init);
    }
    render() {
        return (
            <div className="row">
                <SearchPanel 
                addToList={this.addToList} 
                fetchManageStudentResults={this.fetchManageStudentResults}
                studentList={this.state.studentList}
                courseId={courseId} />
                <ManagePanel 
                 removeFromList={this.removeFromList}
                 fetchManageStudentResults={this.fetchManageStudentResults}
                 studentList={this.state.studentList}
                 />
            </div>
        );
    }
}

ReactDOM.render(<Register />, document.getElementById('test'));
