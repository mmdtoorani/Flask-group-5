$.ajax({
    url: "http://127.0.0.1:5000/tags-list/",
    type: "GET",

    success: function (response) {
        console.log(response);

        for (let i = 0; i < response.length; i++) {
            let login = 'login';
            console.log(response[i])
            let tr_elem = $('<tr></tr>').appendTo('#table_tag')
            tr_elem.append(`<td onclick="redirectTo('${response[i].id}');" style="color: red" style="color: red">${response[i].name}</td>`);
        }

    }
})

$.ajax({
    url: "http://127.0.0.1:5000/categories-list/",
    type: "GET",

    success: function (response) {
        console.log(response);

        for (let i = 0; i < response.length; i++) {
            console.log(response[i])
            let tr_elem = $('<tr></tr>').appendTo('#table_cat')
            tr_elem.append(`<td onclick="redirectToCat('${response[i].id}');">${response[i].name}</td>`);
            for (let j = 0; j < response[i].children.length; j++) {
                console.log(response[i].children[j])
                let tr_elem = $('<tr></tr>').appendTo('#table_cat')
                tr_elem.append(`<td onclick="redirectToCat('${response[i].children[j].id}');" style="color: red">${response[i].children[j].name}</td>`);
            }
        }
    }
})

function redirectTo(id) {
    window.location.href = "http://127.0.0.1:5000/tag-posts/" + id;
}

function redirectToCat(id) {
    window.location.href = "http://127.0.0.1:5000/category-posts/" + id;
}