function validateForm() {
	//Program by Fadhil Aweim
  var username = document.getElementById("username").value; //mengambil data input dari field
  var password = document.getElementById("password").value;

  var pola_username = / ^[a - z] + $ /; // pola huruf kecil semua
  var max_username = 5;

  var pola_password = / ^([0 - 9] {2, 2}) + (@ || &)([A - Z] {4, 4})$ /; // pola angka 2 digit + @/& + Kapital 4 karakter

  
  if (!username.match(pola_username)) { // Jika username ada yang tidak huruf kecil
    alert('nama huruf kecil semuanya');
    return false;
  }
  if (username.length < max_username) { // Jika jumlah karakter username lebih dari batas
    alert('Nama minimal 5 huruf')
    return (false);
  }
  if (!password.match(pola_password)) { // Jika password tidak sesuai pola
    alert ('Password kombinasi dari 2 digit angka diikuti  “@” atau  “&” dan diikuti 4 huruf besar');
    return (false);
  }
  else
  {
    return (true);
  }
}
