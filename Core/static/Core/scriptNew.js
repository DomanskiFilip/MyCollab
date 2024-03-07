
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
  
          // Set the canvas dimensions to the desired size
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
  
          // Draw the image on the canvas
          ctx.drawImage(img, 0, 0, width, height);
  
          // Get the data URL of the resized image
          var dataUrl = canvas.toDataURL('image/jpeg');
  
          // Display the resized image
          document.querySelector('#preview' + input.name.replace(/\D/g, '')).innerHTML = '<img src="' + dataUrl + '">';
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(input.files[0]);
  });
});


  