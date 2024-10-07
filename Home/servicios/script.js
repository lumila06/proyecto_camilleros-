function loadServices() {
    fetch('servicios/service.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('content').innerHTML = data;
            document.getElementById('home-section').style.display = 'none';
            document.getElementById('service-section').style.display = 'block';
        })
        .catch(error => console.error('Error al cargar la pantalla de servicios:', error));
}

function goBackHome() {
    document.getElementById('service-section').style.display = 'none';
    document.getElementById('home-section').style.display = 'block';
}
