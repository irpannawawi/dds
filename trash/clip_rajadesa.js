    document.getElementById('provinsi').value = "JAWA BARAT"

    axios.post("https://bos.polri.go.id/laporan/buat-laporan/kota", {id: 32})
    .then(function (response) {
        $('#kabupaten').empty()
        $('#kabupaten').append(`<option value="">-- pilih kota/kabupaten -- </option>`)
        $.each(response.data, function (id, name) {
            $('#kabupaten').append(`<option value='${name}' id='${id}'> ${name} </option>`)
        })
    })

    axios.post("https://bos.polri.go.id/laporan/buat-laporan/kecamatan", {id: 3207})
    .then(function (response) {
        $('#kecamatan').empty()
        if(""){
            let append = `<option value="">-- pilih kecamatan --</option>`
            $('#kecamatan').append(append)
        }
        else{
            let append = `<option value="">-- pilih kecamatan --</option>`;
            $('#kecamatan').append(append);
        }
        $.each(response.data, function (id, name) {
            $('#kecamatan').append(`<option value='${name}' id='${id}'> ${name} </option>`)
        })
    })

    axios.post("https://bos.polri.go.id/laporan/buat-laporan/desa", {id: 320713})
    .then(function (response) {
        $('#desa').empty();
        $('#desa').append(`<option value="">-- pilih kelurahan/desa -- </option>`)
        $.each(response.data, function (id, name) {
            $('#desa').append(`<option value='${name}' id='${id}'> ${name} </option>`)
        })
    }).then(function(){
            setTimeout(function(){

                document.getElementById('provinsi').value = "JAWA BARAT"
                document.getElementById('kabupaten').value = "KABUPATEN CIAMIS"
                document.getElementById('kecamatan').value = "RAJADESA"
                document.getElementById('desa').value = "Sukaharja"
                $("#uraian-informasi").val($("#uraian-keluhan").val())            
            }, 2000)
    })
                    