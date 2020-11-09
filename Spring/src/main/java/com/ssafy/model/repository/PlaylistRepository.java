package com.ssafy.model.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.ssafy.model.dto.PlaylistDto;

public interface PlaylistRepository extends JpaRepository<PlaylistDto, Integer> {
	@Query(value = "select * from ssafy.playlist where playlist_type = :playlist_type limit :start ,10", nativeQuery = true)
	public List<PlaylistDto> findPlaylistTeacher(@Param("playlist_type") int playlistType,
			@Param("start") Integer start);

	public List<PlaylistDto> findbyUserId(String userId);
}
