import * as React from 'react';
import {
	Component
} from 'react';
import $ from 'jquery';

import { Student } from '../../../declaration/models/Student';

import getCSRFToken from '../../../utils/getCSRFToken';

import SearchPanel from './SearchPanel';
import ManagePanel from './ManagePanel';

const courseId: string = $("#course-pk").data('id');

interface RegisterState {
	studentList: Student[];
}

export default class Register extends Component<{}, RegisterState> {
	constructor(props: any) {
		super(props);
		this.state = {
			studentList: [],
		};
		this.manageStudent = this.manageStudent.bind(this);
		this.addToList = this.addToList.bind(this);
		this.removeFromList = this.removeFromList.bind(this);
	}

	public componentDidMount(): void {
		const fetchStudentList = this.fetchStudentList();
		fetchStudentList
			.then((res) => {
				return res.json();
			})
			.then((data) => {
				this.setState({
					studentList: data.studentList
				});
			})
			.catch(() => {
				M.toast({
					html: '錯誤',
					classes: 'red'
				});
			});
	}

	/**
	 * 
	 * @param {Array<Student>} students List of students which need to be registered to
	 *  the course. 
	 */
	public addToList(students: Student[]): void {
		const {
			studentList
		} = this.state;
		for (let student of students) {
			studentList.push(student);
		}
		this.setState({
			studentList
		});
	}

	/**
	 * 
	 * @param {Array<Student>} students List of students which need to be removed.
	 */
	public removeFromList(students: Student[]): void {
		const {
			studentList
		} = this.state;
		let newStudentList = studentList.filter((student) => (!students.includes(student)));
		this.setState({
			studentList: newStudentList
		});
	}

	/**
	 * 
	 * @param {String} type Specify the type of method "add" or "delete"
	 * @param {String} studentId The student's id.
	 * @return {Promise<Response>}
	 */
	public manageStudent(type: String, studentId: String): Promise < Response > {
		const requestUrl = `/course/student/${courseId}`;
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
	public fetchStudentList(): Promise < Response > {
		const requestUrl = `/course/student/${courseId}`;
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

	public render() {
		return ( 
		<div className = "row" >
			<SearchPanel
			addToList = {this.addToList}
			fetchManageStudentResults={this.manageStudent}
			studentList = {this.state.studentList}
			courseId = {courseId}	/> 
			<ManagePanel 
			removeFromList = {this.removeFromList}
			fetchManageStudentResults={this.manageStudent}
			studentList = {this.state.studentList}/>
			</div>
		);
	}
}
