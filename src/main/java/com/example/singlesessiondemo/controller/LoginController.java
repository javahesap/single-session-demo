package com.example.singlesessiondemo.controller;

import com.example.singlesessiondemo.config.SessionConfig;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class LoginController {

    @GetMapping("/login")
    public String loginPage() {
        return "login";
    }

    @PostMapping("/login")
    public String doLogin(@RequestParam String username,
                          HttpServletRequest request,
                          Model model) {

        if (SessionConfig.isUserAlreadyLoggedIn(username)) {
            model.addAttribute("error", "Bu kullanıcı zaten giriş yapmış!");
            return "login";
        }

        HttpSession session = request.getSession(true);
        SessionConfig.registerSession(username, session.getId());
        session.setAttribute("username", username);
        return "redirect:/home";
    }

    @GetMapping("/home")
    public String homePage(HttpSession session, Model model) {
        String username = (String) session.getAttribute("username");
        if (username == null) {
            return "redirect:/login";
        }
        model.addAttribute("username", username);
        return "home";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        SessionConfig.removeSessionById(session.getId());
        session.invalidate();
        return "redirect:/login";
    }
}
