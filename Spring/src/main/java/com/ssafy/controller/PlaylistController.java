package com.ssafy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;

import com.ssafy.model.dto.PlaylistDto;
import com.ssafy.model.dto.UserDto;
import com.ssafy.model.response.BasicResponse;
import com.ssafy.model.service.PlaylistService;

import io.swagger.models.Response;

@Controller
public class PlaylistController {
	@Autowired
	private RedisTemplate<String, Object> redisTemplate;
	@Autowired
	private PlaylistService playlistService;

	@GetMapping("/api/public/palylist/teacher")
	public Object FindAllPlaylist(@RequestParam int start) {
		BasicResponse response = new BasicResponse();

		response.data = playlistService.findAllPlaylistTeacher(start);

		if (response.data != null) {
			response.status = true;
			response.message = "조회에 성공하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.OK);
		} else {
			response.status = false;
			response.message = "조회에 실패하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
		}
	}

	@GetMapping("/api/public/palylist/user")
	public Object FindAllPlaylist(@RequestHeader("Authorization") String jwtToken) {
		BasicResponse response = new BasicResponse();
		UserDto user = (UserDto) redisTemplate.opsForValue().get(jwtToken);

		response.data = playlistService.findAllPlaylistUser(user.getUserId());

		if (response.data != null) {
			response.status = true;
			response.message = "조회에 성공하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.OK);
		} else {
			response.status = false;
			response.message = "조회에 실패하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
		}
	}

	@GetMapping("/api/public/palylist/detail")
	public Object FindDetailPlaylist(@RequestParam int playlistId) {
		BasicResponse response = new BasicResponse();

		response.data = playlistService.findPlaylistDetail(playlistId);

		if (response.data != null) {
			response.status = true;
			response.message = "조회에 성공하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.OK);
		} else {
			response.status = false;
			response.message = "조회에 실패하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
		}
	}

	@PutMapping("/api/private/playlist/save")
	public Object Saveplaylist(@RequestHeader("Authorization") String jwtToken, @RequestBody PlaylistDto playlist) {
		BasicResponse response = new BasicResponse();
		UserDto user = (UserDto) redisTemplate.opsForValue().get(jwtToken);

		playlist.setUserId(user.getUserId());

		response.data = playlistService.savePlaylist(playlist);

		if (response.data != null) {
			response.status = true;
			response.message = "저장에 성공하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.OK);
		} else {
			response.status = false;
			response.message = "저장에 실패하였습니다.";
			return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
		}
	}

	@DeleteMapping("/api/public/playlist/delete")
	public Object DeletePlaylist(@RequestHeader("Authorization") String jwtToken, @RequestBody PlaylistDto playlist) {
		return null;
	}

	@PutMapping("/api/public/playlist/update")
	public Object UpdatePlaylist() {
		return null;
	}

}
