import React from 'react';
import ScoreGraph from '../../components/ScoreGraph';
import { ScoreResult } from '../../declaration/models/Score';

interface StudentCourseSubjectListState {
  subjects: ScoreResult[];
};

export default class StudentCourseSubjectList extends React.PureComponent<{},StudentCourseSubjectListState> {
  constructor(props: any) {
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
      .then(data => {
        this.setState({ subjects: data.results });
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

  public render(): React.ReactNode {
    const subjectItems = this.state.subjects.map((subject, index) => (
      <li key={index}>
        <div className='collapsible-header'>
          {subject.title}
          <span className='badge'>{subject.subject_type}</span>
        </div>
        <div className='collapsible-body'>
          <div>我的成績 {subject.current_score}</div>
            <ScoreGraph name={subject.title} scoreList={subject.score_list} type='box' />
        </div>
      </li>)
    );
    return (
      <ul className='collapsible'>
        {subjectItems.length && subjectItems}
      </ul>
    );
  }
}
