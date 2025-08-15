
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="sec" uri="http://www.springframework.org/security/tags" %>
<html><head><title>Home</title></head><body>
<h1>Home</h1>
<c:if test="${not empty jwtToken}"><p><strong>JWT:</strong> <small>${jwtToken}</small></p></c:if>
<p><a href="/public">Public Page</a></p>
<sec:authorize access="hasAnyRole('ROLE_USER','ROLE_ADMIN')"><p><a href="/user">User Page</a></p></sec:authorize>
<sec:authorize access="hasRole('ROLE_ADMIN')"><p><a href="/admin">Admin Page</a></p></sec:authorize>
<p><a href="/login">Login</a></p>
</body></html>
