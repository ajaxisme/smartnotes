$(onClickSubmit() {
      $('#addTranscript').click(function() {
          var pass = $('#transcript').val();
          $.ajax({
              url: '/addTranscript',
              data: $('form').serialize(),
              type: 'POST',
              success: function(response) {
                  console.log(response);
              },
              error: function(error) {
                  console.log(error);
              }
          });
      });
    });