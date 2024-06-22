document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.getElementById('searchBar');
    // Prevent the form from submitting traditionally
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        // Trigger the search functionality
        searchBar.dispatchEvent(new Event('input'));
    });

    searchBar.addEventListener('input', function() {
        // Assuming you have a way to get the correct URL for the fetch call
        const searchUrl = `/collabs/collab_list/?search=${searchBar.value}`;
        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {
                // Check if data.collabs_withImg is a string that needs parsing
                const collabs = typeof data.collabs_withImg_list === 'string' ? JSON.parse(data.collabs_withImg) : data.collabs_withImg;
                document.getElementById('collabListWrapper').innerHTML = '';
                collabs.forEach(collab => {        
                const collabElement = document.createElement('a');
                // Ensure the URL is correctly formed
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
