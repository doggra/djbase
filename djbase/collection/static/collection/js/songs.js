var songs_table_body = $("table#songs tbody");

$(document).ready(function() {

	$.ajax({
		method: 'GET',
		url: 'api/?format=json'
	}).done(function(data) {
		for (var i=0;i<data.length;i++) {
			var row = data[i];
			var entry = '<tr>'+
							'<td>'+row.artists.join(", ")+'</td>'+
							'<td>'+row.name+'</td>'+
							'<td>'+row.bpm+'</td>'+
							'<td>'+row.genres.join(", ")+'</td>'+
							'<td>'+row.tags.join(", ")+'</td>'+
						'</tr>'
			songs_table_body.append(entry);
		}
		console.log(data);
	});

});