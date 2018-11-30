import M from 'materialize-css';
import getCSRFToken from '../../utils/getCSRFToken';
import deleteRegister from '../common/delete';

export default class Subject {
	constructor() {
		deleteRegister('subject');
		$('td').on('click', '.edit-score', this.editScore);
		$('td').on('click', '.submit-score',this.submitScore);
	}

	public editScore(event: Event): void {
		event.preventDefault();
		const editId = $(event.target).data('id');
		const score = parseFloat($(`.score[data-id="${editId}"]`).html());
		$(event.target).toggleClass('submit-score edit-score').html('submit');
		$(`.score[data-id="${editId}"]`).html(`<input data-id="${editId}" type="number" value=${score} max="100" min="0" step="0.01">`);
	}

	public submitScore(event: Event): void {
		event.preventDefault();
		const editId = $(event.target).data('id');
		const newScore = $(`input[data-id="${editId}"]`).val();

		if (!newScore) {
			M.toast({
				html: 'input is not a number.',
				classes: 'red'
			});
			return false;
		}
		if (newScore > 100 || newScore < 0) {
			M.toast({
				html: 'input out of range.',
				classes: 'red'
			});
			return false;
		}

		const csrfToken = getCSRFToken();

		const body = JSON.stringify({
			score: newScore,
			pk: editId,
		});

		const headers = new Headers();
		headers.set('Content-Type', 'application/x-www-form-urlencoded');
		headers.set('X-CSRFToken', csrfToken);

		const postNewGrade = fetch('/grade/edit/', {
			headers,
			method: 'POST',
			body,
		});

		postNewGrade
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				M.toast({
					html: data.status,
					classes: 'card-panel teal lighten-2'
				});
				$(`.score[data-id="${editId}"]`).html(data.score);
				$(event.target).toggleClass('submit-score edit-score').html('edit');
				$('#subject-average').html(data.new_average);
			})
			.catch((error) => {
				M.toast({
					html: error,
					classes: 'red'
				});
			});
	}
}