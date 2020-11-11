package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dto.ProblemDto;
import com.ssafy.model.repository.ProblemRepository;

@Service
public class ProblemServiceImpl implements ProblemService {
	@Autowired
	private ProblemRepository problemRepository;

	@Override
	public List<ProblemDto> FindProblemByVideo(String videoId) {
		// TODO Auto-generated method stub
		return problemRepository.findByVideoId(videoId);
	}

}
