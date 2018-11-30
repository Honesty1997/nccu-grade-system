import getCSRFToken from '../../utils/getCSRFToken';

export default function deleteRegister(model: string) {
  $(`#${model}-delete`).click(function(){
    const headers = new Headers()
    headers.append('Accept', 'application/json');
    headers.append('X-CSRFToken', getCSRFToken());
    const url = $(this).data('url');
    const init : RequestInit = {
        method: 'DELETE',
        credentials: 'include',
        headers,
    };
    const deleteEvent = fetch(url, init);
    deleteEvent
        .then(res => {
            if (res.ok) {
                return res.json()
            }
            M.toast({ html: '錯誤', classes: 'red'});
        })
        .then(res => {
            window.location.href = res.success_url;
        });
  });
  
}