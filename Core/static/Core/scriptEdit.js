
window.onload = function() {
    var fileInputs = document.querySelectorAll('input[type="file"]');
    for (var i = 0; i < fileInputs.length; i++) {
        fileInputs[i].dataset.index = i;  // Set the dataset.index to match the img id
        fileInputs[i].addEventListener('change', function(e) {
            if (e.target.files && e.target.files[0]) {
                var reader = new FileReader();
                reader.onload = function(event) {
                    var img = document.querySelectorAll('#preview' + e.target.dataset.index);
                    img.src = event.target.result;
                }
                reader.readAsDataURL(e.target.files[0]);
            }
        });
    }
}


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

// a solution if images are required (in forms.py set to True)
/*
document.addEventListener('DOMContentLoaded', (event) => {
  var errorList = document.querySelectorAll(".errorlist");
  errorList.forEach(function(item) {
      item.innerHTML = '<li>Description cannot be added without an image!</li>';
  });
});
*/