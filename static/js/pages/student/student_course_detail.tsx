import  React, { Suspense } from 'react';
import ReactDOM from 'react-dom';

export default class StudentCourseDetail {
  constructor() {
    const container = document.getElementById('student-course-detail');
    const StudentCourseSubjectList = React.lazy(() => import('./StudentCourseSubjectList'));
    if (container) {
      ReactDOM.render(<Suspense fallback={<div>載入中</div>}><StudentCourseSubjectList /></Suspense>, container);
    }
  }
}
