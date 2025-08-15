package com.example.singlesessiondemo.config;

import jakarta.servlet.http.HttpSessionEvent;
import jakarta.servlet.http.HttpSessionListener;
import org.springframework.context.annotation.Configuration;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Configuration
public class SessionConfig implements HttpSessionListener {

    private static final Map<String, String> userSessionMap = new ConcurrentHashMap<>();

    public static boolean isUserAlreadyLoggedIn(String username) {
        return userSessionMap.containsKey(username);
    }

    public static void registerSession(String username, String sessionId) {
        userSessionMap.put(username, sessionId);
    }

    public static void removeSessionById(String sessionId) {
        userSessionMap.values().removeIf(id -> id.equals(sessionId));
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        removeSessionById(se.getSession().getId());
    }
}
