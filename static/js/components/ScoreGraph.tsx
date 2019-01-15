import React, { Component, Suspense } from 'react';

const Plot = React.lazy(() => /** webpackPrefetch: true */ import('react-plotly.js'));

interface ScoreGraphProps {
  scoreList: string[];
  currentScore?: string;
  name: string;
  type: 'box';
};

export default class ScoreGraph extends Component<ScoreGraphProps,{}> {
  public render() : React.ReactNode {
    const data = {
      name: this.props.name,
      type: this.props.type,
      x: this.props.scoreList.map(score => Number(score)),
    };
    const config = {
      displayModeBar: false,
      responsive: true,
    };
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <Plot data={[data]} config={config} layout={{}}/>
      </Suspense>
    )
  }
}