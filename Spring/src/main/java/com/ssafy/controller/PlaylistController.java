package com.ssafy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.ssafy.model.service.PlaylistService;

@Controller
public class PlaylistController {
	@Autowired
	private RedisTemplate<String, Object> redisTemplate;
	@Autowired
	private PlaylistService playlistService;

	@GetMapping("/api/public/palylist/list")
	public Object FindAllPlayList() {
		return null;
	}

	@GetMapping("/api/public/palylist/detail")
	public Object FindPlaylist() {
		return null;
	}

	@PutMapping("/api/public/playlist/save")
	public Object Saveplaylist() {
		return null;
	}

	@DeleteMapping("/api/public/playlist/delete")
	public Object DeletePlaylist() {
		return null;
	}

	@PutMapping("/api/public/playlist/update")
	public Object UpdatePlaylist() {
		return null;
	}

}
