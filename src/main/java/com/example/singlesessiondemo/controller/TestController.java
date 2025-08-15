
package com.example.singlesessiondemo.controller;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

@RestController
public class TestController {
    @GetMapping("/api/test/user")
    @PreAuthorize("hasAnyRole('USER','ADMIN')")
    public Map<String, Object> user() { return Map.of("ok", true, "scope", "USER"); }

    @GetMapping("/api/test/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public Map<String, Object> admin() { return Map.of("ok", true, "scope", "ADMIN"); }
}
