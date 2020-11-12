package com.ssafy.model.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.ssafy.model.dto.PlaylistDto;

@Repository
public interface PlaylistRepository extends JpaRepository<PlaylistDto, Integer> {
	@Query(value = "select * from ssafy.playlist where playlist_type = 0 and playlist_id not in (select playlist_type from playlist where user_id = :user_id and playlist_type !=0) limit :start ,9", nativeQuery = true)
	public List<PlaylistDto> findPlaylistTeacher(@Param("user_id") String user_id, @Param("start") Integer start);

	@Query(value = "select * from ssafy.playlist where user_id = :user_id and playlist_type !=0", nativeQuery = true)
	public List<PlaylistDto> findbyUserid(@Param("user_id") String userId);

	@Query(value = "select * from ssafy.playlist where user_id =:user_id and playlist_type = 0", nativeQuery = true)
	public List<PlaylistDto> findByManagement(@Param("user_id") String userId);

}
