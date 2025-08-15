
package com.example.singlesessiondemo.config;

import com.example.singlesessiondemo.entity.Role;
import com.example.singlesessiondemo.entity.User;
import com.example.singlesessiondemo.repo.RoleRepository;
import com.example.singlesessiondemo.repo.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.HashSet;
import java.util.Set;

@Configuration
public class DataInitializer {

    @Bean
    CommandLineRunner init(RoleRepository roleRepo, UserRepository userRepo, PasswordEncoder encoder) {
        return args -> {
            Role rUser = roleRepo.findByName("ROLE_USER").orElseGet(() -> roleRepo.save(new Role("ROLE_USER")));
            Role rAdmin = roleRepo.findByName("ROLE_ADMIN").orElseGet(() -> roleRepo.save(new Role("ROLE_ADMIN")));

            if (!userRepo.existsByUsername("admin")) {
                User admin = new User();
                admin.setUsername("admin");
                admin.setPassword(encoder.encode("admin123"));
                admin.setEnabled(true);
                Set<Role> rs = new HashSet<>();
                rs.add(rUser); rs.add(rAdmin);
                admin.setRoles(rs);
                userRepo.save(admin);
            }
            if (!userRepo.existsByUsername("user")) {
                User user = new User();
                user.setUsername("user");
                user.setPassword(encoder.encode("user123"));
                user.setEnabled(true);
                Set<Role> rs = new HashSet<>();
                rs.add(rUser);
                user.setRoles(rs);
                userRepo.save(user);
            }
        };
    }
}
