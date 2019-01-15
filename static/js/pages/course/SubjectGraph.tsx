import React, { Component } from 'react';

import { ScoreResult } from '../../declaration/models/Score';
import ScoreGraph from '../../components/ScoreGraph';

interface SubjectGraphsProps {
  subject: ScoreResult;
}

export default class SubjectGraphs extends Component<SubjectGraphsProps, {}> {
  public render(): React.ReactNode {
    return (
      <div className="row">
        <div className="col m6 s12">
          <ScoreGraph name={this.props.subject.title} scoreList={this.props.subject.score_list} type='box' />
        </div>
      </div>
    );
  }
}