import M from 'materialize-css';

export default class ChangePassword {
  constructor() {
    const form = document.getElementById('change-password') as HTMLFormElement;
    if (form) {
      form.addEventListener('submit', this.comparePassword);
    }
  }
  private comparePassword(evt: Event) {
      evt.preventDefault();
      const password = document.getElementById('id_password') as HTMLInputElement;
      const validatePassword = document.getElementById('passowrd-check') as HTMLInputElement;
      if (password && password.value && password.value !== validatePassword.value) {
          M.toast({html: '密碼不一致', classes: 'red'});
          validatePassword.value = '';
      } else if (evt.target){
        const target = evt.target as HTMLFormElement;
        target.submit();
      }
    }
}
