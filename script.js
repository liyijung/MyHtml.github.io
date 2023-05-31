function sendRequest() {
  var function_options = document.getElementById("function_options").value;
  var inputText = document.getElementById("inputText").value;

  $.ajax({
    type: "POST",
    url: "https://ac31-2001-b011-5c00-1a21-60eb-9439-a5ff-3b66.ngrok-free.app/sendrequest",
    data: { function_options: function_options, inputText: inputText },
    success: function(response) {
      var result = response.result;
      var formattedResult = result.replace(/\n/g, "<br>");
      document.getElementById("outputText").innerHTML = formattedResult;
    },
    error: function() {
      alert("請求失敗");
    }
  });
}
