import M from 'materialize-css';
function initialize () {
}
export default class ChangePassword {
  constructor() {
    const form = document.getElementById('change-password');
    if (form) {
      form.addEventListener('submit', this.comparePassword);
    }
  }
  private comparePassword(evt: Event) {
      evt.preventDefault();
      const password = document.getElementById('id_password');
      const validatePassword = document.getElementById('passowrd-check');
      if (password.value !== validatePassword.value) {
          M.toast({html: '密碼不一致', classes: 'red'});
          validatePassword.value = '';
      } else {
          evt.target.submit();
      }
    }
}