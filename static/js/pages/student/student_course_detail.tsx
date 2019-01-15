import  React from 'react';
import ReactDOM from 'react-dom';

import StudentCourseSubjectList from './StudentCourseSubjectList';

export default class StudentCourseDetail {
  constructor() {
    const container = document.getElementById('student-course-detail');
    if (container) {
      ReactDOM.render(<StudentCourseSubjectList />, container);
    }
  }
}
