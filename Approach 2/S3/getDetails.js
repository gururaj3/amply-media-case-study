var chatHistory = [];
var apigClient = null;
// const AWS =require('aws-sdk');
var url_string = window.location.href;

function callChatbotLambda() {
  // var itext = document.getElementById('user-input-text').value.trim()
  // var inputText = itext.toLowerCase();
  // document.getElementById('user-input-text').value = "";
  // if(inputText == "") {
  //   alert("Please enter some text");
  //   return false;
  // }else {
  //   chatHistory.push("User: " + itext);
  //   document.getElementById('chat-output').innerHTML = "";
  //   chatHistory.forEach((element) => {
  //     document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
  //   });
//   console.log("Hello")
    setTimeout(chatbotResponse, 500);
    return false;
  // }
}


function chatbotResponse() {
  // return AWS.config.credentials.getPromise()
  // .then(()=>{
  //   console.log('Successfully logged!');
  apigClient = apigClientFactory.newClient({
  //     accessKey: AWS.config.credentials.accessKeyId,
  //     secretKey: AWS.config.credentials.secretAccessKey,
  //     // sessionToken: AWS.config.credentials.sessionToken
     });
    var params = {};
    var body = {
      // "message":inputText,
      // "userId":"lf0c"
      // "identityID":AWS.config.credentials._identityId
    };
    var additionalParams = {
      // headers: {
      //   'x-api-key': 'Your API KEY'
      // },
      // queryParams: {}
    };
    // console.log("body")
    return apigClient.rootGet(params,body,additionalParams)
  // })
   .then((result) =>{

    console.log(result);
     console.log("type of result: ", typeof(result))
      var response = result.data.body;
      console.log(typeof(response));

      var message=JSON.stringify(response)
      console.log("message", message)

    //   r=JSON.stringify(result);
      const obj = JSON.parse(result.data.body);
    //   r1 = response[city];
      console.log(obj)
      console.log("type of obj: ", typeof(obj))
      console.log(obj.city)
      console.log(obj.state)
      console.log(obj.description)
      console.log(obj.next3DaysInfo)
      document.getElementById("city").innerHTML = "<p> City: " + obj.city + "</p>";
      document.getElementById("state").innerHTML = "<p> State: " + obj.state + "</p>";
      document.getElementById("description").innerHTML = "<p> Description: " + obj.description + "</p>";
      document.getElementById("l1").innerHTML = "<p> Low Temperature: " + obj.next3DaysInfo[0]["Low Temperature"] + "</p>";
      document.getElementById("h1").innerHTML = "<p> High Temperature: " + obj.next3DaysInfo[0]["High Temperature"] + "</p>";
      document.getElementById("d1").innerHTML = "<p> Description: " + obj.next3DaysInfo[0]["description"] + "</p>";
      document.getElementById("l2").innerHTML = "<p> Low Temperature: " + obj.next3DaysInfo[1]["Low Temperature"] + "</p>";
      document.getElementById("h2").innerHTML = "<p> High Temperature: " + obj.next3DaysInfo[1]["High Temperature"] + "</p>";
      document.getElementById("d2").innerHTML = "<p> Description: " + obj.next3DaysInfo[1]["description"] + "</p>";
      document.getElementById("l3").innerHTML = "<p> Low Temperature: " + obj.next3DaysInfo[2]["Low Temperature"] + "</p>";
      document.getElementById("h3").innerHTML = "<p> High Temperature: " + obj.next3DaysInfo[2]["High Temperature"] + "</p>";
      document.getElementById("d3").innerHTML = "<p> Description: " + obj.next3DaysInfo[2]["description"] + "</p>";


    //   r1 = result["data"];
    //   r2 = JSON.stringify(r1);
    //   r3 = r2.substring(3, r2.length-3);
    //   console.log("r3", r3)
    //   r1 = result["data"];
    //   console.log("r1", r1)
      // r2 = JSON.stringify(r1);
      // r3 = r2.substring(3, r2.length-3);

      // chatHistory.push("Bot: " + r3);
      // document.getElementById('chat-output').innerHTML = "";
      // // console.log(message)
      // chatHistory.forEach((element) => {
      //   document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
      // });
  })
  .catch((err) =>{
    console.log(err);
  });
 }