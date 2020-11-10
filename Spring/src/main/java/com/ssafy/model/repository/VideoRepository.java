package com.ssafy.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ssafy.model.dto.Video;

public interface VideoRepository extends JpaRepository<Video, String> {

}
