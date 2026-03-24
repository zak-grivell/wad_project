let artist_id = document.getElementById("id_artist_id");

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

  const buffer_time = 1000;
  let timer = null;

  const onStall = (text) => {
    if (text.length < 3 || element.dataset.id) { return }

    const params = new URLSearchParams({
      keyword: text,
    });

    if (artist_id.value) {
      params.artist_id = artist_id.value
    }

    fetch(`api/${name}_search?${params}`)
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
    }
  })
}

searchDataList("artist", true);
searchDataList("tour", false);
searchDataList("venue", true);
