//Accediendo al input con id mensaje
const mensajeInput = document.querySelector("#mensaje");
/**
 * Asignando el focus por defecto al input con id mensaje
 */
mensajeInput.focus();

/**
 * Inicializando SocketIO
 */
const socket = io();

//Escuchando connect
socket.on("connect", function () {
  console.log("Socket Activo y escuchando.!");
});

//Escuchando disconnect
socket.on("disconnect", function () {
  console.log("Socket Desconectado.!");
});

const form_chat = document.querySelector("#formulario_chat");
if (form_chat) {
  form_chat.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Verificar si viene algun mensaje
    if (mensajeInput && mensajeInput.value.trim() === "") {
      console.log("formulario vacio");
      mensajeInput.style.border = "1px solid #ffb2a0";
      return; // Detener el envío del formulario
    }

    // Reproducir el archivo de audio después de recibir una respuesta exitosa
    const audio = new Audio("../static/audio/audio_chat.mp3");
    audio.play();

    //limpio el border del input mensaje
    mensajeInput.style.border = "";
    //console.log(`Mensaje ${mensajeInput.value}`);
    // Emitir el mensaje como cadena de texto
    socket.emit("mensaje_chat", mensajeInput.value);
    console.log(`Mensaje enviado`);
    mensajeInput.value = "";
  });
}

/**
 * Escuchando el evento "mensaje_chat" en el cliente JavaScript y recibiendo el mensaje enviado desde el servidor
 */
socket.on("mensaje_chat", (mensaje) => {
  //console.log(`Nuevo mensaje: ${mensaje}`);

  scroll_chat();
  const divContent = document.querySelector(".chat__content");
  divContent.innerHTML = "";
  divContent.innerHTML += mensaje;
});

/**
 * Manipular el scroll cuando existe un nuevo mensaje
 */
const scroll_chat = () => {
  const chatContent = document.querySelector(".chat__content");
  const scrollHeight = chatContent.scrollHeight;

  // Realiza la animación del scroll
  const scrollToBottom = () => {
    const scrollOptions = {
      top: scrollHeight,
      behavior: "smooth",
    };
    chatContent.scrollTo(scrollOptions);
  };

  // Llama a la función para realizar la animación después de un breve retraso
  setTimeout(scrollToBottom, 100); // Ajusta el valor del retraso según sea necesario
};
