const inputName= document.getElementById('name');
const inputMessages= document.getElementById('messages');
const inputEmail= document.getElementById('email');
const inputPhone = document.getElementById('phone');


    
    inputName.addEventListener("input",function(event){
        if(inputName.validity.patternMismatch){
            inputName.setCustomValidity(gettext('Enter a string without using numbers and special characters!'));
            inputName.reportValidity;
            inputName.style.backgroundColor="rgba(224, 22, 22,0.2)";
        }else{
            inputName.setCustomValidity("");
            inputName.style.backgroundColor="rgba(73, 224, 22, 0.2)";
        }
    }) ;
    inputPhone.addEventListener("input",function(event){
            if(inputPhone.validity.patternMismatch){
                inputPhone.setCustomValidity(gettext('Example of correct input : +79232267770'));
                inputPhone.style.backgroundColor="rgba(224, 22, 22,0.2)";
                inputPhone.reportValidity;
            }else{
                inputPhone.setCustomValidity("");
                inputPhone.style.backgroundColor="rgba(73, 224, 22, 0.2)";
                
            }
        });
    

     inputEmail.addEventListener("input",function(event){
                if(inputEmail.validity.patternMismatch){
                    inputEmail.setCustomValidity(gettext('Example of correct input : hello@example.com'));
                    inputEmail.style.backgroundColor="rgba(224, 22, 22,0.2)";
                    inputEmail.reportValidity;
                    console.log(gettext('email not valid'));

                }else{
                    inputEmail.setCustomValidity("");
                    inputEmail.style.backgroundColor="rgba(73, 224, 22, 0.2)";
                }
    });
    

      

document.getElementById("submit_contact").addEventListener('submit', function(event){
    if(!inputEmail.validity.valid || !inputFirstName.validity.valid || !inputPhone.validity.valid || !inputLastName.validity.valid){
        alert(gettext('Incorrect data entry!'));
        
    }else{
        alert("Ok"); 
        
    }

}
);
/*
window.addEventListener( "load", function () {
    function sendData() {
      const XHR = new XMLHttpRequest();
  
      // Bind the FormData object and the form element
      const FD = new FormData( form );
  
      // Define what happens on successful data submission
      XHR.addEventListener( "load", function(event) {
        alert( event.target.responseText );
      } );
  
      // Define what happens in case of error
      XHR.addEventListener( "error", function( event ) {
        alert( 'Oops! Something went wrong.' );
      } );
  
      // Set up our request
      XHR.open( "POST", "https://api.telegram.org/bot5239076080:AAFCncumYGACzTLXqVM_dJ2YfHLb2pr_A3E/sendMessage?chat_id=-753755551/getMe");
  
      // The data sent is what the user provided in the form
      XHR.send( FD );
    }
  
    // Access the form element...
    const form = document.getElementById( "btn" );
  
    // ...and take over its submit event.
    form.addEventListener( "submit", function ( event ) {
      event.preventDefault();
      if(!inputEmail.validity.valid || !inputFirstName.validity.valid || !inputPhone.validity.valid || !inputLastName.validity.valid){
        alert("Некорректный ввод данных!");
        
    }else{
        sendData();
        
    }
      
    } );
  } );*/