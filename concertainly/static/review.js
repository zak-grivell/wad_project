/**
@param {string} name
@param {bool} required
*/
function searchDataList(name, required) {
  const element = document.getElementById(`${name}_select`);
  const datalist = document.getElementById(`${name}_options`);  
  let valid_names = {};

  element.addEventListener("blur", () => {
    if (element.value == "") return;

    element.classList.add('was-validated')
    if (!element.dataset.id && required) {
      element.setCustomValidity("Option not selected")
      element.reportValidity();
    } else {
      element.setCustomValidity("")
      element.reportValidity();
    }
  })

  const buffer_time = 1000;
  let timer = null;

  const onStall = (text) => {
    if (text.length < 3 || element.dataset.id) { return }

    const params = new URLSearchParams({
      keyword: text,
    });

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
          element.dataset.id = valid_names[element.value.toLowerCase()]
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
      element.dataset.id = valid_names[element.value.toLowerCase()]
    }
  })
}

searchDataList("artist", true);
searchDataList("tour", false);
searchDataList("venue", true);
