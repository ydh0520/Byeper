package com.ssafy.model.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.ssafy.model.dto.Video;

public interface VideoRepository extends JpaRepository<Video, String> {
	@Query(value = "select b.* from ssafy.play as a, ssafy.video as b where a.video_id = b.video_id and a.playlist_id =:playlist_id", nativeQuery = true)
	public List<Video> findVideoByPlaylist(@Param("playlist_id") int playlistId);

}
