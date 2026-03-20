let artist_options = document.getElementById("artist_options");

document.getElementById("artist_select").addEventListener("input", (event) => {  
  /** @type {string} */
  let text = event.target.value;
  
  artist_options.replaceChildren();

  if (text.length < 5) { return }

  const params = new URLSearchParams({
    q: text
  });

  fetch(`api/artist_search?${params}`)
    .then(res => res.json())
    .then(options => {
      options.artists.forEach((option /** @type {string} */) => {
        let e = document.createElement("option");

        e.value = option.name;
        e.dataset.id = option.id;

        artist_options.append(e);
      })
    })
    .catch(e => console.log(e))
})

let tour_options = document.getElementById("tour_options");
document.getElementById("tour_select").addEventListener("input", (event) => {  
  /** @type {string} */
  let text = event.target.value;
  
  tour_options.replaceChildren();

  if (text.length < 5) { return }

  const params = new URLSearchParams({
    q: text
  });

  fetch(`api/tour_search?${params}`)
    .then(res => res.json())
    .then(options => {
      options.artists.forEach((option /** @type {string} */) => {
        let e = document.createElement("option");

        e.value = option.name;
        e.dataset.id = option.id;

        tour_options.append(e);
      })
    })
    .catch(e => console.log(e))
})

let venue_options = document.getElementById("tour_options");
document.getElementById("tour_select").addEventListener("input", (event) => {  
  /** @type {string} */
  let text = event.target.value;
  
  venue_options .replaceChildren();

  if (text.length < 5) { return }

  const params = new URLSearchParams({
    q: text
  });

  fetch(`api/tour_search?${params}`)
    .then(res => res.json())
    .then(options => {
      options.artists.forEach((option /** @type {string} */) => {
        let e = document.createElement("option");

        e.value = option.name;
        e.dataset.id = option.id;

        tour_options.append(e);
      })
    })
    .catch(e => console.log(e))
})
