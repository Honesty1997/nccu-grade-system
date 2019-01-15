import $ from 'jquery';
import M from 'materialize-css';


export default class Document {
  constructor() {
    this.initMaterializeUI();
  }

  private initMaterializeUI(): void {
    $(document).ready(function(){
      $('select').formSelect();
    });
    const textareas = document.querySelectorAll('textarea');
    Array.prototype.forEach.call(textareas, (textarea: HTMLTextAreaElement)=> {
      textarea.classList.add('materialize-textarea');
    });
    const element = document.getElementsByClassName('tabs')[0];
    if (element) {
      M.Tabs.init(element);
    }
    $('.dropdown-trigger').dropdown();
    $(document).ready(function(){
        $('.modal').modal();
      });
  }
}