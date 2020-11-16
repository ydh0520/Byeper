package com.ssafy.model.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.ssafy.model.dto.ProblemDto;

@Repository
public interface ProblemRepository extends JpaRepository<ProblemDto, Integer> {
	List<ProblemDto> findByVideoId(String videoId);
}

