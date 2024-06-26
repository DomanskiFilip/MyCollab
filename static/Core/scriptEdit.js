
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

        var previewElementId = '#preview' + input.name.replace(/\D/g, '');
        var previewElement = document.querySelector(previewElementId);
        var existingImg = previewElement.querySelector('img');
        if (existingImg) {
          // If an img tag exists, update its src attribute
          existingImg.src = dataUrl;
        } else {
          // If no img tag exists, create a new img tag and set its src attribute
          previewElement.innerHTML = '<img src="' + dataUrl + '">';
        }
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  });
});

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