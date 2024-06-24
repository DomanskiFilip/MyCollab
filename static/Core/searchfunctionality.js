function fetchCollabs(page) {
    if (!page) {
        page = 1;
    }
    let searchBar = document.getElementById('searchBar');
    let selectedTags = Array.from(document.querySelectorAll('input[type="checkbox"][name="tags"]:checked')).map(checkbox => checkbox.value);
    let queryString = selectedTags.map(tag => `tags=${tag}`).join('&');
    let searchQuery = searchBar.value;
    if (searchQuery) {
        queryString += (queryString ? '&' : '') + `search=${encodeURIComponent(searchQuery)}`;
    }
    let fetchUrl = queryString ? `/collabs/collab_list/?${queryString}&page=${page}` : `/collabs/collab_list/?page=${page}`;
    console.log(fetchUrl);
    fetch(fetchUrl)
        .then(response => response.json())
        .then(data => {
            const collabs = typeof data.collabs_withImg === 'string' ? JSON.parse(data.collabs_withImg) : data.collabs_withImg;
            document.getElementById('collabListWrapper').innerHTML = '';
            if (collabs && collabs.length > 0) {
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
                const totalPages = data.total_pages;
                const paginationContainer = document.getElementById('paginationContainer');
                paginationContainer.innerHTML = '';
                for (let i = 1; i <= totalPages; i++) {
                    if(totalPages == 1){
                        break;
                    }

                    if(i > 1){
                        const buttonBack = document.createElement('button');
                        buttonBack.classList.add('btn');
                        buttonBack.id = 'button_back';
                        buttonBack.textContent = '<';
                        buttonBack.addEventListener('click', () => {
                            fetchCollabs(page-1);
                        });paginationContainer.appendChild(buttonBack);

                        const buttonCurrent = document.createElement('button');
                        buttonCurrent.classList.add('btn');
                        buttonCurrent.id = 'button_current';
                        buttonCurrent.textContent = `${page}`;
                        buttonCurrent.classList.add('active'); 
                        buttonCurrent.addEventListener('click', () => {
                            page = i; 
                            fetchCollabs(i);
                        });paginationContainer.appendChild(buttonCurrent);

                        const buttonNext = document.createElement('button');
                        buttonNext.classList.add('btn');
                        buttonNext.id = 'button_next';
                        buttonNext.textContent = '>';
                        buttonNext.addEventListener('click', () => {
                            fetchCollabs(page+1);
                        });paginationContainer.appendChild(buttonNext);

                        const buttonlast = document.createElement('button');
                        buttonlast.classList.add('btn');
                        buttonlast.id = 'last';
                        buttonlast.textContent = `${totalPages}`;
                        buttonlast.addEventListener('click', () => {
                            fetchCollabs(totalPages);
                        });paginationContainer.appendChild(buttonlast);

                        if(page == 1){
                            buttonCurrent.style.display = 'none';
                            buttonBack.style.display = 'none';
                            
                            if(page+1 < totalPages){
                                buttonNext.style.display = 'inline-block';
                            }
                            if(totalPages > 1){
                                buttonlast.style.display = 'inline-block';
                            }
                        }else if(page+1 < totalPages){
                            buttonNext.style.display = 'inline-block';
                            buttonCurrent.style.display = 'inline-block';
                            buttonBack.style.display = 'inline-block'; 
                        }else if(page+2 == totalPages){
                            buttonNext.style.display = 'none';
                            buttonlast.style.display = 'none';
                        }else if(page == totalPages){
                            buttonCurrent.style.display = 'none';
                            buttonNext.style.display = 'none';
                            buttonBack.style.display = 'inline-block'; 
                        }
                        break;
                    }

                    

                    const button = document.createElement('button');
                    button.classList.add('btn');
                    button.textContent = `${i}`;
                    button.addEventListener('click', () => {
                        page = i; 
                        fetchCollabs(i);
                    });
                    paginationContainer.appendChild(button);
                }
            } else { 
                document.getElementById('collabListWrapper').innerHTML = 'no collabs found';
        }

        }).catch(error => console.error('Error fetching data:', error));
}

document.addEventListener("DOMContentLoaded", function() {
    fetchCollabs(1);
    document.getElementById('searchBar').addEventListener('input', function() {
        fetchCollabs(1);
    });

    document.querySelectorAll('input[type="checkbox"][name="tags"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            fetchCollabs(1);
        });
    });

    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        fetchCollabs(1); 
    });
});

function createPaginationButton(pageNumber) {
    const button = document.createElement('button');
    button.classList.add('btn');
    button.textContent = `${pageNumber}`;
    button.addEventListener('click', () => {
        fetchCollabs(pageNumber);
    });
    paginationContainer.appendChild(button);
}


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
    let verticalLists = document.querySelectorAll('.vertical_list');
    verticalLists.forEach(function(verticalList) {
        let seenTags = {}; 
        let tags = verticalList.querySelectorAll('span');
        tags.forEach(function(tag) {
            let tagLabel = tag.querySelector('label').textContent; 
            if (seenTags[tagLabel]) {
                tag.remove();
            } else {
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
