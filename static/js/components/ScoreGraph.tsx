import React, { Component } from 'react';
import Plot from 'react-plotly.js';

interface ScoreGraphProps {
  scoreList: string[];
  currentScore?: string;
  name: string;
};

export default class ScoreGraph extends Component<ScoreGraphProps,{}> {
  public render() : React.ReactNode {
    const data = {
      name: this.props.name,
      type: 'box',
      x: this.props.scoreList.map(score => Number(score)),
    };
    const config = {
      displayModeBar: false,
      responsive: true,
    };
    return (
      <Plot data={[data]} config={config} />
    )
  }
}