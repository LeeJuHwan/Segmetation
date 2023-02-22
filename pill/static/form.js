const body = document.querySelector('body');
const modal = document.querySelector('.modal');
const btnOpenPopup = document.querySelector('.btn-open-popup');

btnOpenPopup.addEventListener('click', () => {
  modal.classList.toggle('show');

  if (modal.classList.contains('show')) {
    body.style.overflow = 'hidden';
  }
});

modal.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.classList.toggle('show');

    if (!modal.classList.contains('show')) {
      body.style.overflow = 'auto';
    }
  }
});

function fileUpload() {
    modal.class
}



window.onload = function() {
    $("#photoFile").on('change', function() {
        if(window.FileReader){  
          var filename = $(this)[0].files[0].name;
        } else {  
          var filename = $(this).val().split('/').pop().split('\\').pop();  // 파일명만 추출
        }

  
        LoadImg($("#photoFile")[0]);
      });
  }

function LoadImg(value) {
    if(value.files && value.files[0]) {

      var reader = new FileReader();
    
      reader.onload = function (e) {
        $('.camera-logo').attr('src', e.target.result);
        $('.camera-logo').show();
      }

      reader.readAsDataURL(value.files[0]);
    }
}

