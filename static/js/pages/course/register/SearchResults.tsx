import * as React from 'react';
import {
  Component
} from 'react';
import M from 'materialize-css';

import { Student } from '../../../declaration/models/Student';
interface SearchResultsProps {
  fetchedList: Student[];
  studentList: Student[];
  addToList: (studentList: Student[]) => void;
  fetchManageStudentResults: (type: string, studentId: string) => Promise<Response>;
}

export default class SearchResults extends Component<SearchResultsProps, {}> {
  constructor(props: SearchResultsProps) {
    super(props);
    this.onClick = this.onClick.bind(this);
  }
  public onClick(student: Student) {
    const {
      pk
    } = student;
    const fetchAddResults = this.props.fetchManageStudentResults('add', pk);
    fetchAddResults
      .then((res: Response) => {
        return res.json();
      })
      .then((data) => {
        if (data.status == 'success') {
          this.props.addToList([student]);
        }
      })
      .catch(() => {
        M.toast({
          html: '錯誤',
          classes: 'red'
        });
      });
  }

  render() {
    const studentList = this.props.fetchedList.map((student) => {
      let addButton;
      if (this.props.studentList.some((stu) => (stu.pk == student.pk))) { 
        addButton = (<button className = "secondary-content btn-small student-add-button" disabled> 新增 </button>);
      } else {
        addButton = ( <button className = "secondary-content btn-small student-add-button" onClick = {
            () => { this.onClick(student); } } > 新增 </button>
        );
      }
      return ( <div className = "collection-item" key={student.pk}> {student.name} { addButton } </div>
      );
    });
    return ( <div className = "collection with-header" style = {{marginTop: '25px'}} >
      <h4 className = "collection-header" > 搜尋結果 </h4>
      <div id = "results-container"
      style = { { padding: '5px'}} > 
        { studentList.length == 0 ? '沒有結果' : studentList} 
        </div>
      </div>
    );
  }
}