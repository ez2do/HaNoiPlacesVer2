const KEY = "AIzaSyCq6PXWt4ItkN9QXsJ372VRN5EqUTAgaDQ";

function getUrl(place, key){
	return "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + place + "&maxResult=50&type=video&key=" + key;
}

$(document).ready(function(){
	$('.update-button').on('click', function(){
		let place_id = $(this).attr('placeID');
		let point = $(this).attr('value');

		var req = $.ajax({
			url: '/update',
			type: 'POST',
			data: {id: place_id, point: point}
		}).done(function(data){
			$('#card' + place_id).fadeOut(500).fadeIn(500);
			$('#point-of-' + place_id).html(data.rating.toFixed(2));
		});
	});

	$('.video-trigger').on('click', function(){
		let place = $(this).parent().find('.place-name').html();
		let description_arr = $(this).parent().find(".place-description").html().split(/[\s,]+/);
		//take a number of range 5
		let range = Math.floor(Math.random() * 5);
		let start = Math.floor(Math.random() * description_arr.length);
		let end = description_arr.length;
		if(start + range < description_arr.length){
			end = start + range;
		}
		let search_keywords = description_arr.slice(start, end);
		let search_string = "\"" + place +"\"" + " điểm đến, " + search_keywords.join(" ");
		console.log(search_string);

		//query the place on youtube
		let url = getUrl(search_string, KEY);
		$.getJSON(url, function(data){
			console.log(data);
			//get 1 video of query list
			let length = data.items.length;
			let index = Math.floor(Math.random() * length);
			console.log("len " + length + ", index " + index);
			let video_id = data.items[index].id.videoId;
			$('.iframe-video').attr('src', "https://www.youtube.com/embed/" + video_id);
		});
	})
})

/* pure js */
/* scroll bar process */
window.addEventListener("scroll", () => {
	bar = document.getElementById("scroll-progress");
	let max = document.body.scrollHeight - innerHeight;
	bar.style.width = (pageYOffset / max) * 100 + '%';
})