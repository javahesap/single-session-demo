
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html><head><title>Login</title></head><body>
<h1>Login</h1>
<form method="post" action="/login">
  <label>Kullanıcı Adı: <input type="text" name="username" /></label><br/>
  <label>Şifre: <input type="password" name="password" /></label><br/>
  <button type="submit">Giriş</button>
</form>
<c:if test="${not empty error}"><p style="color:red">${error}</p></c:if>
<p><a href="/home">Home</a></p>
</body></html>
