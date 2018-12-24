import React from 'react';
interface StudentCourseSubjectListState {
  subjects: Object[];
};
export default class StudentCourseSubjectList extends React.PureComponent {
  public state: StudentCourseSubjectListState;
  constructor(props) {
    super(props);
    this.state = {
      subjects: []
    };
  }
  componentDidMount() {
    this.fetchSubjectsAndScore()
      .then(res => {
        return res.json();
      })
      .then(subjects => {
        this.setState({ subjects: subjects.results });
      });
    $(document).ready(function () {
      $('.collapsible').collapsible();
    });
  }

  public fetchSubjectsAndScore(): Promise<Response> {
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

  public render(): ReactNode {
    const subjectItems = this.state.subjects.map(subject => (
      <li>
        <div className='collapsible-header'>
          {subject.title}
          <span className="badge">{subject.subject_type}</span>
        </div>
        <div className='collapsible-body'>我的成績: {subject.current_score}</div>
      </li>)
    );
    return (
      <ul className='collapsible'>
        {subjectItems.length && subjectItems}
      </ul>
    );
  }
}
