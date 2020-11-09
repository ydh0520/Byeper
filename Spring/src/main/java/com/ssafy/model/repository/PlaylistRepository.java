package com.ssafy.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ssafy.model.dto.PlaylistDto;

public interface PlaylistRepository extends JpaRepository<PlaylistDto, Integer> {

}
