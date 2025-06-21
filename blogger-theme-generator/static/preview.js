// Simple drag and drop handler
window.addEventListener('DOMContentLoaded', function () {
  const dropZone = document.getElementById('dropZone');
  const customInput = document.getElementById('custom_xml');
  if (!dropZone) return;

  dropZone.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropZone.classList.add('drag-over');
  });

  dropZone.addEventListener('dragleave', function () {
    dropZone.classList.remove('drag-over');
  });

  dropZone.addEventListener('drop', function (e) {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        customInput.value = event.target.result;
      };
      reader.readAsText(file);
    }
  });
});
