$(document).ready(function(){
    // $(".signup-form").on("change", "#id_username", function () {
    $("#id_username").keyup(function () {
        var username = $(this).val();
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
          url: 'http://127.0.0.1:8000/user-check',
          type: 'POST',
          data: {
            'username': username,
             csrfmiddlewaretoken: csrftoken
          }, 
          dataType: 'json',
          success: function (data) {
            if (data.is_exist) {
              document.getElementById('user_check').innerHTML = data.error_message;
              document.getElementById('user_check').className = "text-danger";
              document.getElementById('user_check').style.display = "block";
        
            }
            else if(!data.is_exist){
              document.getElementById('user_check').innerHTML = data.success_message;
              document.getElementById('user_check').className = "text-success";
            }
          }
        });
        if(username === " "){
          document.getElementById('user_check').style.display="none";
        }
        else{
          document.getElementById('user_check').style.display = "block";
        }
    
      });
})

