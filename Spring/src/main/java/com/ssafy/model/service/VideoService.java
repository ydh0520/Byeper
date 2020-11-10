package com.ssafy.model.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.ssafy.model.dto.Video;

@Service
public interface VideoService {
	public List<Video> SaveAllVideo(List<Video> videos);
}
