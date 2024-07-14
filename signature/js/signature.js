$(document).ready(function () {
  $("#preview_signature-copy").click(function () {
    new Clipboard("#preview_signature-copy");
  });
});
