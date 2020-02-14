function changeTextareaHeightDynamically() {
  var target = event.target;
  var dynamicHeight = target.scrollHeight;
  target.style.height = dynamicHeight + "px";
}

function tableRowBlurHandler() {
  var target = event.target;
  console.log(target);
  var parentClass = ".tr-block";
  var classWhenEmpty = "empty";
  var parentBlock = target.closest(parentClass);
  if (!target.value.trim()) {
    parentBlock.classList.add(classWhenEmpty);
    return;
  } else {
    parentBlock.classList.remove(classWhenEmpty);
  }
}

function manageTableRow() {
  var target = event.target;
  var cloneTableRow = document.querySelector("[data-clone]").cloneNode(true);
  cloneTableRow.classList.add("empty");
  cloneTableRow.classList.remove("d-none");
  cloneTableRow.removeAttribute("data-clone");
  var rowClass = ".tr-block";
  if (event.key === "Enter") {
    insertSiblingRow(rowClass, target, cloneTableRow);
  }
  if (event.key === "Backspace" && !target.value) {
    removeSiblingRow(rowClass, target);
  }
}

function insertSiblingRow(rowClass, targetBlock, newRow) {
  if (!targetBlock.closest(rowClass).nextElementSibling) {
    targetBlock.closest(rowClass).insertAdjacentElement("afterend", newRow);
  }
}

function removeSiblingRow(rowClass, targetBlock) {
  var targetRowBlock = targetBlock.closest(rowClass);
  var siblingElement = targetRowBlock.nextElementSibling;
  if (siblingElement && siblingElement.classList.contains("empty")) {
    targetRowBlock.parentNode.removeChild(siblingElement);
    return;
  }
}
