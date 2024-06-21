window.onload = function() {
  document.getElementById("CollabForm").addEventListener("submit", function(e){
      let checkboxes = document.querySelectorAll('.checkbox_tags');
      let checkedOne = Array.prototype.slice.call(checkboxes).some(x => x.checked);
      let tags_error_msg = document.getElementById("tags_error_msg");

      let title = document.getElementById("id_title");
      let title_error_msg = document.getElementById("title_error_msg");

      let introduction = document.getElementById("id_introduction");
      let introduction_error_msg = document.getElementById("introduction_error_msg");

      if (title.value.trim() === "") {
          e.preventDefault();
          title_error_msg.innerHTML = "Title is required!";
          tags_error_msg.innerHTML = "";
          introduction_error_msg.innerHTML = "";
          return;
      } else {
        title_error_msg.innerHTML = "";
        tags_error_msg.innerHTML = "";
        introduction_error_msg.innerHTML = "";
      }

      if (!checkedOne) {
          e.preventDefault();
          tags_error_msg.innerHTML = "Please select at least one tag!";
          title_error_msg.innerHTML = "";
          introduction_error_msg.innerHTML = "";
          return;
      } else {
        title_error_msg.innerHTML = "";
        tags_error_msg.innerHTML = "";
        introduction_error_msg.innerHTML = "";
      }

      if (introduction.value.trim() === "") {
          e.preventDefault();
          introduction_error_msg.innerHTML = "Introduction is required!";
          title_error_msg.innerHTML = "";
          tags_error_msg.innerHTML = "";
          return;
      } else {
        title_error_msg.innerHTML = "";
        tags_error_msg.innerHTML = "";
        introduction_error_msg.innerHTML = "";
      }
  });
};

// Get all checkboxes
var checkboxes = document.querySelectorAll('.checkbox_is_main');

// Add event listener to each checkbox
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        // When a checkbox is checked
        if (this.checked) {
            // Uncheck all other checkboxes
            checkboxes.forEach(function(otherCheckbox) {
                if (otherCheckbox !== checkbox) {
                    otherCheckbox.checked = false;
                }
            });
        }
    });
});


document.querySelectorAll('input[type="file"]').forEach(function(input) {
  input.addEventListener('change', function() {
      var reader = new FileReader();
      reader.onload = function(e) {
        var img = new Image();
        img.onload = function() {
          var canvas = document.createElement('canvas');
          var ctx = canvas.getContext('2d');
  
          var MAX_WIDTH = 200;
          var MAX_HEIGHT = 150;
          var width = img.width;
          var height = img.height;
  
          if (width > height) {
            if (width > MAX_WIDTH) {
              height *= MAX_WIDTH / width;
              width = MAX_WIDTH;
            }
          } else {
            if (height > MAX_HEIGHT) {
              width *= MAX_HEIGHT / height;
              height = MAX_HEIGHT;
            }
          }
  
          canvas.width = width;
          canvas.height = height;
  
          ctx.drawImage(img, 0, 0, width, height);
  
          var dataUrl = canvas.toDataURL('image/jpeg');
  
          document.querySelector('#preview' + input.name.replace(/\D/g, '')).innerHTML = '<img src="' + dataUrl + '">';
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(input.files[0]);
  });
});
