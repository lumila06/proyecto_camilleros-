new Vue({
    el: '#app',
    data: {
      scanning: false,
      patient: {
        firstName: '',
        lastName: '',
        gender: '',
        dni: '',
        age: null,
        code: ''
      },
      html5QrCode: null
    },
    methods: {
      startScan() {
        this.scanning = true;
  
        // Espera a que Vue haya mostrado el elemento "qr-reader"
        this.$nextTick(() => {
          if (!this.html5QrCode) {
            this.html5QrCode = new Html5Qrcode("qr-reader");
  
            // Configurar el escaneo
            this.html5QrCode.start(
              { facingMode: "environment" }, // o puedes usar facingMode: { exact: "environment" }
              {
                fps: 10,
                qrbox: 250
              },
              (decodedText, decodedResult) => {
                // Manejar el QR escaneado aquí
                alert(`QR Code scanned: ${decodedText}`);
                this.scanning = false;
                this.html5QrCode.stop().catch(err => console.error(err));
              },
              (errorMessage) => {
                // Ocurre cuando hay un error al escanear, ignóralo si no es crítico
                console.log(`Error scanning: ${errorMessage}`);
              }
            ).catch((err) => {
              console.error(`Error starting Html5Qrcode: ${err}`);
            });
          }
        });
      },
      submitForm() {
        // Aquí procesas los datos del paciente
        alert('Formulario enviado');
        console.log(this.patient);
      }
    }
  });
  