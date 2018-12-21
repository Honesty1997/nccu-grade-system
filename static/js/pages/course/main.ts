import Register from './register/entry';
import CourseDetail from './course_detail';
import Subject from './subject';

export default class Course {
  constructor() {
    const register = new Register();
    const courseDetail = new CourseDetail();
    const subject = new Subject();
  }
}