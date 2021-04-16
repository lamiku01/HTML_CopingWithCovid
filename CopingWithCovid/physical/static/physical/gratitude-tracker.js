// Gratitude-tracker
const gratitude_tracker            = document.getElementById("gratitude-tracker");
const gratitude_tracker_storage    = document.getElementById("gratitude-tracker-storage");
const gratitude_tracker_text_input = document.getElementById("gratitude-tracker-storage");

// Creates and inserts new element.
function addGratitudeElement() {
	var li = document.createElement("li");
	var inputValue = document.getElementById("gratitude-tracker-text-input").value;
	var t = document.createTextNode(inputValue);
	li.appendChild(t);
	if (inputValue === '') {
		alert("Please write something!");
	} else {
		document.getElementById("gratitude-tracker-storage").appendChild(li);
	}
	document.getElementById("gratitude-tracker-text-input").value = "";

	var span = document.createElement("SPAN");
	var txt = document.createTextNode("\u00D7");
	span.className = "close";
	span.appendChild(txt);
	li.appendChild(span);

	span.parentElement.onclick = function () {
		this.style.display = "none";
	}
}
