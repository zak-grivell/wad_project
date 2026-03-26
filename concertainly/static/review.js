let artist_id = document.getElementById("id_artist_id");

function artist_has_been_selected(on) {
  document.getElementById("setlist").disabled = on;
  document.getElementById("tour_select").disabled = on;
}

/**
@param {string} name
@param {bool} required
*/
function searchDataList(name, required) {
  const element = document.getElementById(`${name}_select`);
  const datalist = document.getElementById(`${name}_select_list`);
  const id_feild = document.getElementById(`id_${name}_id`)

  let valid_names = {};

  element.addEventListener("blur", () => {
    if (element.value == "") return;

    element.classList.add('was-validated')
    if (!id_feild.value && required) {

      element.setCustomValidity("Option not selected")
    } else {
      element.setCustomValidity("")
    }

    element.reportValidity();
  })

  const buffer_time = 250;
  let timer = null;

  const onStall = (text) => {
    if (text.length < 3 || element.dataset.id) { return }

    const params = new URLSearchParams({
      keyword: text,
    });

    if (artist_id.value) {
      params.set("artist_id", artist_id.value)
    }

    let url = new URL(`api/${name}_search`, window.location.origin);
    url.search = params;

    fetch(url)
      .then(res => res.json())
      .then(options => {
        options.items.forEach((option /** @type {string} */) => {
          let e = document.createElement("option");

          e.value = option.name;
          e.dataset.id = option.id;

          valid_names[option.name.toLowerCase()] = option.id
          datalist.append(e);
        })

        if (element.value.toLowerCase() in valid_names) {
          id_feild.value = valid_names[element.value.toLowerCase()]
        }
      })
      .catch(e => console.error(e))
  }

  element.addEventListener("input", (event) => {
    if (!(event.target.value.toLowerCase() in valid_names)) {
      datalist.replaceChildren();
      element.dataset.id = "";
      valid_names = {};
      clearTimeout(timer);
      timer = setTimeout(() => onStall(event.target.value), buffer_time);
    } else {
      id_feild.value = valid_names[element.value.toLowerCase()]
      if (name == "artist") {
        artist_has_been_selected(false)
      }
    }
  })
}

searchDataList("artist", true);
searchDataList("tour", false);
searchDataList("venue", true);

Array.from(document.getElementsByClassName("setlist-button")).forEach((el) => {
  el.addEventListener("click", () => {
    el.remove()
  })
})

const song_search_field = document.getElementById("song_search");
const datalist = document.getElementById("song-select-list");
const out_list = document.getElementById("setlist")

let valid_names = {};

document.getElementById("search_add").addEventListener("click", () => {
  if (song_search_field.value.toLowerCase() in valid_names) {
    let id = valid_names[song_search_field.value.toLowerCase()]

    let li = document.createElement("option")

    li.value = `${id}|${song_search_field.value}`;

    li.innerText = song_search_field.value;

    li.selected = true;

    song_search_field.value = ""
    datalist.replaceChildren()

    out_list.append(li)
  }
});

const buffer_time = 250;
let timer = null;

const onStall = (text) => {
  if (text.length < 3) { return }

  const params = new URLSearchParams({
    keyword: text,
  });

  console.log(artist_id.value)

  if (artist_id.value) {
    params.set("artist", artist_id.value)
  }

  let url = new URL("api/song_search", window.location.origin);
  url.search = params;

  fetch(url)
    .then(res => res.json())
    .then(options => {
      options.items.forEach((option /** @type {string} */) => {
        let e = document.createElement("option");

        e.classList.add("setlist-button")

        e.value = option.title;
        e.dataset.id = option.id;

        valid_names[option.title.toLowerCase()] = option.id
        datalist.append(e);
      })

    })
    .catch(e => console.error(e))
}

document.getElementById("song_search").addEventListener("input", (event) => {
  if (!(event.target.value.toLowerCase() in valid_names)) {
    valid_names = {};
    clearTimeout(timer);
    timer = setTimeout(() => onStall(event.target.value), buffer_time);
  }
})
