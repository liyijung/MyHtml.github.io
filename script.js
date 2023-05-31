function sendRequest() {
  var function_options = document.getElementById("function_options").value;
  var inputText = document.getElementById("inputText").value;

  $.ajax({
    type: "POST",
    url: "/sendrequest",
    data: { function_options: function_options, inputText: inputText },
    success: function(response) {
      document.getElementById("outputText").value = response.result;
    },
    error: function() {
      alert("请求失败");
    }
  });
}
