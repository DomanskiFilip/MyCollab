

document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.getElementById('searchBar');
    searchBar.addEventListener('input', function() {
        const selectedTags = Array.from(document.querySelectorAll('input[type="checkbox"][name="tags"]:checked')).map(checkbox => checkbox.value);
        let searchUrl;
        if(selectedTags.length > 0) {
            const tagsQueryString = selectedTags.join('&');
            searchUrl = `/collabs/collab_list/?search=${searchBar.value}&tags=${tagsQueryString}`;
        } else {
            searchUrl = `/collabs/collab_list/?search=${searchBar.value}`;
        }
        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {
                const collabs = typeof data.collabs_withImg_list === 'string' ? JSON.parse(data.collabs_withImg) : data.collabs_withImg;
                document.getElementById('collabListWrapper').innerHTML = '';
                collabs.forEach(collab => {        
                    const collabElement = document.createElement('a');
                    collabElement.href = `/collabs/${collab.pk}`;
                    collabElement.id = "collabInfoBar";
                    collabElement.innerHTML = `
                    <section id="collabInfoBarHeader">
                        <h2>${collab.title}</h2>
                    </section>
                    <section class="collabInfoBarWrapper">
                        <img src="${collab.main_image.src}" alt="" onerror="this.style.display='none'">
                        <span> ${collab.introduction} </span>
                    </section>
                    <section class="collabInfoBarWrapper" id="tagsBox">
                        <h2>Tags:</h2>
                        <ul>
                            ${collab.tags.map(tag => `<li>${tag}</li>`).join('')}
                        </ul>
                    </section>
                    <p>Created: ${collab.created_at}</p>
                    `;
                    document.getElementById('collabListWrapper').appendChild(collabElement);
                });
            }).catch(error => console.error('Error fetching data:', error));
    });
});
//tag list
function showTagList() {
    let verticalLists = document.querySelectorAll('.vertical_list');
        verticalLists.forEach(function(verticalLists) {
            if (verticalLists.classList.contains('open')) {
                verticalLists.classList.remove('open');
            } else {
                verticalLists.classList.add('open');
            }
    });
}

function removeDuplicateTags() {
    // Select all vertical lists
    let verticalLists = document.querySelectorAll('.vertical_list');
    verticalLists.forEach(function(verticalList) {
        let seenTags = {}; // Object to keep track of tags that have been seen
        let tags = verticalList.querySelectorAll('span'); // Assuming each tag is wrapped in a <span>
        tags.forEach(function(tag) {
            let tagLabel = tag.querySelector('label').textContent; // Get the text content of the label
            if (seenTags[tagLabel]) {
                // If the tag has been seen, remove the current tag span
                tag.remove();
            } else {
                // If the tag hasn't been seen, mark it as seen
                seenTags[tagLabel] = true;
            }
        });
    });
}

removeDuplicateTags();


var checkbox_tags = document.querySelectorAll('.vertical_list input[type="checkbox"]');

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

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        fetchCollabsWithSelectedTags();
    });

    document.querySelectorAll('input[type="checkbox"][name="tags"]').forEach(checkbox => {
        checkbox.addEventListener('change', fetchCollabsWithSelectedTags);
    });

    function fetchCollabsWithSelectedTags() {
        let checkedBoxes = document.querySelectorAll('input[type="checkbox"][name="tags"]:checked');
        let queryString = Array.from(checkedBoxes).map(checkbox => `tags=${checkbox.value}`).join('&');
        let searchQuery = document.getElementById('searchBar').value;
        if (searchQuery) {
            queryString += (queryString ? '&' : '') + `search=${encodeURIComponent(searchQuery)}`;
        }
        let fetchUrl = queryString ? `/collabs/collab_list/?${queryString}` : `/collabs/collab_list/`;

        fetch(fetchUrl)
            .then(response => response.json())
            .then(data => {
                const collabs = typeof data.collabs_withImg === 'string' ? JSON.parse(data.collabs_withImg) : data.collabs_withImg;
                document.getElementById('collabListWrapper').innerHTML = '';
                collabs.forEach(collab => {
                    const collabElement = document.createElement('a');
                    collabElement.href = `/collabs/${collab.pk}`;
                    collabElement.id = "collabInfoBar";
                    collabElement.innerHTML = `
                    <section id="collabInfoBarHeader">
                        <h2>${collab.title}</h2>
                    </section>
                    <section class="collabInfoBarWrapper">
                        <img src="${collab.main_image.src}" alt="" onerror="this.style.display='none'">
                        <span> ${collab.introduction} </span>
                    </section>
                    <section class="collabInfoBarWrapper" id="tagsBox">
                        <h2>Tags:</h2>
                        <ul>
                            ${collab.tags.map(tag => `<li>${tag}</li>`).join('')}
                        </ul>
                    </section>
                    <p>Created: ${collab.created_at}</p>
                    `;
                    document.getElementById('collabListWrapper').appendChild(collabElement);
                });
            }).catch(error => console.error('Error fetching data:', error));
    }
});