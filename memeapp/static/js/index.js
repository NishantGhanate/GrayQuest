
function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";"
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

function showCookieBanner(cookieMessage,username){
  document.getElementById('cookieName').innerText = username;
  $(cookieMessage).fadeTo(5000,1).fadeOut(500).hide(0);  
}


function deleteCookie(name) {
  document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

function checkCookie() {
    var username = getCookie("username");
    var cookieMessage = document.getElementById('cookieMessage');
    if (username != "") {
        showCookieBanner(cookieMessage,username);
    }
    else{
      console.log('Cookie not found');
    }
}


