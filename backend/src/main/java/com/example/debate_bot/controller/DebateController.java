package com.example.debate_bot.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:3000") // For React frontend
public class DebateController {

    @GetMapping("/test")
    public String test() {
        return "Debate Bot API is running!";
    }

    @PostMapping("/startDebate")
    public String startDebate(@RequestBody String topic) {
        // TODO: Implement debate initialization
        return "Starting debate on: " + topic;
    }

    @PostMapping("/sendMessage")
    public String sendMessage(@RequestBody String message) {
        // TODO: Implement message processing and bot response
        return "Bot response to: " + message;
    }
}
