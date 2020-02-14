window.addEventListener("DOMContentLoaded", function() {
  initFunc();
});

function initFunc() {
  popupHandler();
}

function popupHandler() {
  var popupOpeners = document.querySelectorAll("[data-modal-target]");
  popupOpeners.forEach(opener => {
    opener.addEventListener("click", e => togglePopup(e, opener));
  });
}

function togglePopup(e, opener) {
  e.preventDefault();
  var popupId = opener.dataset.modalTarget;
  var popup = document.getElementById(popupId);
  popup.classList.toggle("popup-active");
}
