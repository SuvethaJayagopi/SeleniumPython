
function validateEmail() {
    var email = document.getElementById("email").value;
    var pattern = /^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (pattern.test(email)) {
        var parts = email.split('@');
        var username = parts[0];
        var domainParts = parts[1].split('.');
        var domainName = domainParts[0];
        var topLevelDomain = domainParts[1];
        
        alert("Username: " + username + ", Domain Name: " + domainName + ", Top-level Domain: " + topLevelDomain);
    } else {
        alert("Invalid Email ID");
    }
}
