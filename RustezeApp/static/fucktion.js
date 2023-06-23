document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita el envío del formulario

    // Reiniciar mensajes de error
    document.getElementById('nameError').textContent = '';
    document.getElementById('emailError').textContent = '';
    document.getElementById('passwordError').textContent = '';

    // Obtener los valores de los campos
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Validar nombre
    if (name.trim() === '') {
      document.getElementById('nameError').textContent = 'El nombre es obligatorio.';
    }

    // Validar email
    if (email.trim() === '') {
      document.getElementById('emailError').textContent = 'El email es obligatorio.';
    } else if (!isValidEmail(email)) {
      document.getElementById('emailError').textContent = 'El email no es válido.';
    }

    // Validar contraseña
    if (password.trim() === '') {
      document.getElementById('passwordError').textContent = 'La contraseña es obligatoria.';
    } else if (password.length < 6) {
      document.getElementById('passwordError').textContent = 'La contraseña debe tener al menos 6 caracteres.';
    }

    // Si no hay errores, se puede enviar el formulario
    if (name.trim() !== '' && email.trim() !== '' && isValidEmail(email) && password.trim() !== '' && password.length >= 6) {
      document.getElementById('myForm').submit();
    }
  });

  // Función para validar el formato del email
  function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }