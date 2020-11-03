package com.ssafy.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

import com.ssafy.model.dto.UserDto;

public interface UserRepository extends JpaRepository<UserDto, String> {
	@Modifying
	@Transactional
	@Query(value = "update ssafy.user set user_name = :user_name where user_id = :user_id", nativeQuery = true)
	public int updateUserName(@Param("user_id") String userId, @Param("user_name") String userName);

	@Modifying
	@Transactional
	@Query(value = "update ssafy.user set user_type = 2 where user_id = :user_id", nativeQuery = true)
	public int registTeacher(@Param("user_id") String userId);

}
