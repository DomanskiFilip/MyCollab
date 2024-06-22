
// Get all checkboxes
var checkboxes_main = document.querySelectorAll('.checkbox_is_main');

// Add event listener to each checkbox
checkboxes_main .forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        // When a checkbox is checked
        if (this.checked) {
            // Uncheck all other checkboxes
            checkboxes_main .forEach(function(otherCheckbox) {
                if (otherCheckbox !== checkbox) {
                    otherCheckbox.checked = false;
                }
            });
        }
    });
});



var checkbox_tags = document.querySelectorAll('input[type="checkbox"].checkbox_tags');

checkbox_tags.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        if (this.checked) {
          var label = document.querySelector('label[for="' + this.id + '"]');
          if (label) {
            label.classList.add('checked');
          } else {
            console.log('Label not found for:', this.id);
          }
        } else {
          var label = document.querySelector('label[for="' + this.id + '"]');
          if (label) {
            label.classList.remove('checked');
          }
        }
    });
});

    let buttons = document.querySelectorAll('.addSection');
    buttons.forEach(function(button, index) {
        button.setAttribute('onclick', `addsection(${index + 2})`);
        console.log('added onclick to button:', button);
    });


function addsection(sectionNumber) {
        let section = document.querySelector(".new:nth-of-type(" + sectionNumber + ")");
        let button = document.querySelector(".addSection:nth-of-type(" + sectionNumber + ")");
        let currentButton = document.querySelector(".addSection:nth-of-type(" + (sectionNumber - 1) + ")");
        if (section) {
            section.style.display = "flex";
            currentButton.style.display = "none";
            if(sectionNumber <= 2){
                button.style.display = "initial";
            }
        } 
}