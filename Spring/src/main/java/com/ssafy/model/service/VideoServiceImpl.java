package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dto.Video;
import com.ssafy.model.repository.VideoRepository;

@Service
public class VideoServiceImpl implements VideoService {

	@Autowired
	private VideoRepository videoRepository;

	@Override
	public List<Video> SaveAllVideo(List<Video> videos) {
		// TODO Auto-generated method stub
		return videoRepository.saveAll(videos);
	}

}
