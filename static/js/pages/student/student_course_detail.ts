export default class StudentCourseDetail {
  constructor() {
    const container = document.getElementById('student-course-detail');
    if (container) {
      this.fetchSubjectInfo()
      .then(res => {
        return res.json();
      })
      .then(data => {
        console.log(data);
      });
    }
  }
  public fetchSubjectInfo(): Promise<Response> {
    const url = window.location.pathname;
    const headers = new Headers;
    headers.append('Accept', 'application/json')
    const init: RequestInit = {
      method: 'GET',
      credentials: 'include',
      headers,
    };
    return fetch(url, init);
  }
}