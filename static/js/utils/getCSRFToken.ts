import jQuery from 'jquery';

export default function getCSRFToken(): string {
  let cookieValue;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, 10) === ('csrftoken' + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  if (cookieValue == null) {
    throw new Error('User is not login.')
  }
  return cookieValue;
}
